#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

import json

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.six.moves.urllib.parse import urlencode
from ansible.module_utils._text import to_native, to_text
from ansible.module_utils.urls import fetch_url


def lowercase_string(param):
    if not isinstance(param, str):
        return param
    return param.lower()


class CloudflareAPI(object):

    cf_api_endpoint = 'https://api.cloudflare.com/client/v4'
    changed = False

    def __init__(self, module):
        self.module = module
        self.account_api_token = module.params['account_api_token']
        self.account_email = module.params['account_email']
        self.record = lowercase_string(module.params['record'])
        self.state = module.params['state']
        self.timeout = module.params['timeout']
        self.ttl = module.params['ttl']
        self.type = module.params['type']
        self.value = module.params['value']
        self.zone = lowercase_string(module.params['zone'])

        if self.record == '@':
            self.record = self.zone

        if (self.type in ['CNAME', 'NS', 'MX', 'SRV']) and (self.value is not None):
            self.value = self.value.rstrip('.').lower()

        if (self.type == 'AAAA') and (self.value is not None):
            self.value = self.value.lower()

        if (self.type == 'SRV'):
            if (self.proto is not None) and (not self.proto.startswith('_')):
                self.proto = '_' + self.proto
            if (self.service is not None) and (not self.service.startswith('_')):
                self.service = '_' + self.service

        if (self.type == 'TLSA'):
            if (self.proto is not None) and (not self.proto.startswith('_')):
                self.proto = '_' + self.proto
            if (self.port is not None):
                self.port = '_' + str(self.port)

        if not self.record.endswith(self.zone):
            self.record = self.record + '.' + self.zone

        if (self.type == 'DS'):
            if self.record == self.zone:
                self.module.fail_json(msg="DS records only apply to subdomains.")

    def _cf_simple_api_call(self, api_call, method='GET', payload=None):
        headers = {'X-Auth-Email': self.account_email,
                   'X-Auth-Key': self.account_api_token,
                   'Content-Type': 'application/json'}
        data = None
        if payload:
            try:
                data = json.dumps(payload)
            except Exception as e:
                self.module.fail_json(msg="Failed to encode payload as JSON: %s " % to_native(e))

        resp, info = fetch_url(self.module,
                               self.cf_api_endpoint + api_call,
                               headers=headers,
                               data=data,
                               method=method,
                               timeout=self.timeout)

        if info['status'] not in [200, 304, 400, 401, 403, 429, 405, 415]:
            self.module.fail_json(msg="Failed API call {0}; got unexpected HTTP code {1}".format(api_call, info['status']))

        error_msg = ''
        if info['status'] == 401:
            # Unauthorized
            error_msg = "API user does not have permission; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)
        elif info['status'] == 403:
            # Forbidden
            error_msg = "API request not authenticated; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)
        elif info['status'] == 429:
            # Too many requests
            error_msg = "API client is rate limited; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)
        elif info['status'] == 405:
            # Method not allowed
            error_msg = "API incorrect HTTP method provided; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)
        elif info['status'] == 415:
            # Unsupported Media Type
            error_msg = "API request is not valid JSON; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)
        elif info['status'] == 400:
            # Bad Request
            error_msg = "API bad request; Status: {0}; Method: {1}: Call: {2}".format(info['status'], method, api_call)

        result = None
        try:
            content = resp.read()
        except AttributeError:
            if info['body']:
                content = info['body']
            else:
                error_msg += "; The API response was empty"

        if content:
            try:
                result = json.loads(to_text(content, errors='surrogate_or_strict'))
            except (getattr(json, 'JSONDecodeError', ValueError)) as e:
                error_msg += "; Failed to parse API response with error {0}: {1}".format(to_native(e), content)

        # Without a valid/parsed JSON response no more error processing can be done
        if result is None:
            self.module.fail_json(msg=error_msg)

        if not result['success']:
            error_msg += "; Error details: "
            for error in result['errors']:
                error_msg += "code: {0}, error: {1}; ".format(error['code'], error['message'])
                if 'error_chain' in error:
                    for chain_error in error['error_chain']:
                        error_msg += "code: {0}, error: {1}; ".format(chain_error['code'], chain_error['message'])
            self.module.fail_json(msg=error_msg)

        return result, info['status']

    def _cf_api_call(self, api_call, method='GET', payload=None):
        result, status = self._cf_simple_api_call(api_call, method, payload)

        data = result['result']

        if 'result_info' in result:
            pagination = result['result_info']
            if pagination['total_pages'] > 1:
                next_page = int(pagination['page']) + 1
                parameters = ['page={0}'.format(next_page)]
                # strip "page" parameter from call parameters (if there are any)
                if '?' in api_call:
                    raw_api_call, query = api_call.split('?', 1)
                    parameters += [param for param in query.split('&') if not param.startswith('page')]
                else:
                    raw_api_call = api_call
                while next_page <= pagination['total_pages']:
                    raw_api_call += '?' + '&'.join(parameters)
                    result, status = self._cf_simple_api_call(raw_api_call, method, payload)
                    data += result['result']
                    next_page += 1

        return data, status

    def _get_zone_id(self, zone=None):
        if not zone:
            zone = self.zone

        zones = self.get_zones(zone)
        if len(zones) > 1:
            self.module.fail_json(msg="More than one zone matches {0}".format(zone))

        if len(zones) < 1:
            self.module.fail_json(msg="No zone found with name {0}".format(zone))

        return zones[0]['id']

    def get_zones(self, name=None):
        if not name:
            name = self.zone
        param = ''
        if name:
            param = '?' + urlencode({'name': name})
        zones, status = self._cf_api_call('/zones' + param)
        return zones

    def get_dns_records(self, zone_name=None, type=None, record=None, value=''):
        if not zone_name:
            zone_name = self.zone
        if not type:
            type = self.type
        if not record:
            record = self.record
        # necessary because None as value means to override user
        # set module value
        if (not value) and (value is not None):
            value = self.value

        zone_id = self._get_zone_id()
        api_call = '/zones/{0}/dns_records'.format(zone_id)
        query = {}
        if type:
            query['type'] = type
        if record:
            query['name'] = record
        if value:
            query['content'] = value
        if query:
            api_call += '?' + urlencode(query)

        records, status = self._cf_api_call(api_call)
        return records

    def delete_dns_records(self, **kwargs):
        params = {}
        for param in ['port', 'proto', 'service', 'solo', 'type', 'record', 'value', 'weight', 'zone',
                      'algorithm', 'cert_usage', 'hash_type', 'selector', 'key_tag']:
            if param in kwargs:
                params[param] = kwargs[param]
            else:
                params[param] = getattr(self, param)

        records = []
        content = params['value']
        search_record = params['record']
        if params['type'] == 'SRV':
            if not (params['value'] is None or params['value'] == ''):
                content = str(params['weight']) + '\t' + str(params['port']) + '\t' + params['value']
            search_record = params['service'] + '.' + params['proto'] + '.' + params['record']
        elif params['type'] == 'DS':
            if not (params['value'] is None or params['value'] == ''):
                content = str(params['key_tag']) + '\t' + str(params['algorithm']) + '\t' + str(params['hash_type']) + '\t' + params['value']
        elif params['type'] == 'SSHFP':
            if not (params['value'] is None or params['value'] == ''):
                content = str(params['algorithm']) + '\t' + str(params['hash_type']) + '\t' + params['value']
        elif params['type'] == 'TLSA':
            if not (params['value'] is None or params['value'] == ''):
                content = str(params['cert_usage']) + '\t' + str(params['selector']) + '\t' + str(params['hash_type']) + '\t' + params['value']
            search_record = params['port'] + '.' + params['proto'] + '.' + params['record']
        if params['solo']:
            search_value = None
        else:
            search_value = content

        records = self.get_dns_records(params['zone'], params['type'], search_record, search_value)

        for rr in records:
            if params['solo']:
                if not ((rr['type'] == params['type']) and (rr['name'] == search_record) and (rr['content'] == content)):
                    self.changed = True
                    if not self.module.check_mode:
                        result, info = self._cf_api_call('/zones/{0}/dns_records/{1}'.format(rr['zone_id'], rr['id']), 'DELETE')
            else:
                self.changed = True
                if not self.module.check_mode:
                    result, info = self._cf_api_call('/zones/{0}/dns_records/{1}'.format(rr['zone_id'], rr['id']), 'DELETE')
        return self.changed

    def ensure_dns_record(self, **kwargs):
        params = {}
        for param in ['port', 'priority', 'proto', 'proxied', 'service', 'ttl', 'type', 'record', 'value', 'weight', 'zone',
                      'algorithm', 'cert_usage', 'hash_type', 'selector', 'key_tag']:
            if param in kwargs:
                params[param] = kwargs[param]
            else:
                params[param] = getattr(self, param)

        search_value = params['value']
        search_record = params['record']
        new_record = None
        if (params['type'] is None) or (params['record'] is None):
            self.module.fail_json(msg="You must provide a type and a record to create a new record")

        if (params['type'] in ['A', 'AAAA', 'CNAME', 'TXT', 'MX', 'NS', 'SPF']):
            if not params['value']:
                self.module.fail_json(msg="You must provide a non-empty value to create this record type")

            # there can only be one CNAME per record
            # ignoring the value when searching for existing
            # CNAME records allows us to update the value if it
            # changes
            if params['type'] == 'CNAME':
                search_value = None

            new_record = {
                "type": params['type'],
                "name": params['record'],
                "content": params['value'],
                "ttl": params['ttl']
            }

        if (params['type'] in ['A', 'AAAA', 'CNAME']):
            new_record["proxied"] = params["proxied"]

        if params['type'] == 'MX':
            for attr in [params['priority'], params['value']]:
                if (attr is None) or (attr == ''):
                    self.module.fail_json(msg="You must provide priority and a value to create this record type")
            new_record = {
                "type": params['type'],
                "name": params['record'],
                "content": params['value'],
                "priority": params['priority'],
                "ttl": params['ttl']
            }

        if params['type'] == 'SRV':
            for attr in [params['port'], params['priority'], params['proto'], params['service'], params['weight'], params['value']]:
                if (attr is None) or (attr == ''):
                    self.module.fail_json(msg="You must provide port, priority, proto, service, weight and a value to create this record type")
            srv_data = {
                "target": params['value'],
                "port": params['port'],
                "weight": params['weight'],
                "priority": params['priority'],
                "name": params['record'][:-len('.' + params['zone'])],
                "proto": params['proto'],
                "service": params['service']
            }
            new_record = {"type": params['type'], "ttl": params['ttl'], 'data': srv_data}
            search_value = str(params['weight']) + '\t' + str(params['port']) + '\t' + params['value']
            search_record = params['service'] + '.' + params['proto'] + '.' + params['record']

        if params['type'] == 'DS':
            for attr in [params['key_tag'], params['algorithm'], params['hash_type'], params['value']]:
                if (attr is None) or (attr == ''):
                    self.module.fail_json(msg="You must provide key_tag, algorithm, hash_type and a value to create this record type")
            ds_data = {
                "key_tag": params['key_tag'],
                "algorithm": params['algorithm'],
                "digest_type": params['hash_type'],
                "digest": params['value'],
            }
            new_record = {
                "type": params['type'],
                "name": params['record'],
                'data': ds_data,
                "ttl": params['ttl'],
            }
            search_value = str(params['key_tag']) + '\t' + str(params['algorithm']) + '\t' + str(params['hash_type']) + '\t' + params['value']

        if params['type'] == 'SSHFP':
            for attr in [params['algorithm'], params['hash_type'], params['value']]:
                if (attr is None) or (attr == ''):
                    self.module.fail_json(msg="You must provide algorithm, hash_type and a value to create this record type")
            sshfp_data = {
                "fingerprint": params['value'],
                "type": params['hash_type'],
                "algorithm": params['algorithm'],
            }
            new_record = {
                "type": params['type'],
                "name": params['record'],
                'data': sshfp_data,
                "ttl": params['ttl'],
            }
            search_value = str(params['algorithm']) + '\t' + str(params['hash_type']) + '\t' + params['value']

        if params['type'] == 'TLSA':
            for attr in [params['port'], params['proto'], params['cert_usage'], params['selector'], params['hash_type'], params['value']]:
                if (attr is None) or (attr == ''):
                    self.module.fail_json(msg="You must provide port, proto, cert_usage, selector, hash_type and a value to create this record type")
            search_record = params['port'] + '.' + params['proto'] + '.' + params['record']
            tlsa_data = {
                "usage": params['cert_usage'],
                "selector": params['selector'],
                "matching_type": params['hash_type'],
                "certificate": params['value'],
            }
            new_record = {
                "type": params['type'],
                "name": search_record,
                'data': tlsa_data,
                "ttl": params['ttl'],
            }
            search_value = str(params['cert_usage']) + '\t' + str(params['selector']) + '\t' + str(params['hash_type']) + '\t' + params['value']

        zone_id = self._get_zone_id(params['zone'])
        records = self.get_dns_records(params['zone'], params['type'], search_record, search_value)
        # in theory this should be impossible as cloudflare does not allow
        # the creation of duplicate records but lets cover it anyways
        if len(records) > 1:
            self.module.fail_json(msg="More than one record already exists for the given attributes. That should be impossible, please open an issue!")
        # record already exists, check if it must be updated
        if len(records) == 1:
            cur_record = records[0]
            do_update = False
            if (params['ttl'] is not None) and (cur_record['ttl'] != params['ttl']):
                do_update = True
            if (params['priority'] is not None) and ('priority' in cur_record) and (cur_record['priority'] != params['priority']):
                do_update = True
            if ('proxied' in new_record) and ('proxied' in cur_record) and (cur_record['proxied'] != params['proxied']):
                do_update = True
            if ('data' in new_record) and ('data' in cur_record):
                if (cur_record['data'] != new_record['data']):
                    do_update = True
            if (params['type'] == 'CNAME') and (cur_record['content'] != new_record['content']):
                do_update = True
            if do_update:
                if self.module.check_mode:
                    result = new_record
                else:
                    result, info = self._cf_api_call('/zones/{0}/dns_records/{1}'.format(zone_id, records[0]['id']), 'PUT', new_record)
                self.changed = True
                return result, self.changed
            else:
                return records, self.changed
        if self.module.check_mode:
            result = new_record
        else:
            result, info = self._cf_api_call('/zones/{0}/dns_records'.format(zone_id), 'POST', new_record)
        self.changed = True
        return result, self.changed


def main():
    module = AnsibleModule(
        argument_spec=dict(
            account_api_token=dict(type='str', required=True, no_log=True),
            account_email=dict(type='str', required=True),
            record=dict(type='str', default='@', aliases=['name']),
            state=dict(type='str', default='present', choices=['absent', 'present']),
            timeout=dict(type='int', default=30),
            ttl=dict(type='int', default=1),
            type=dict(type='str', choices=['A', 'AAAA', 'CNAME', 'DS', 'MX', 'NS', 'SPF', 'SRV', 'SSHFP', 'TLSA', 'TXT']),
            value=dict(type='str', aliases=['content']),
            zone=dict(type='str', required=True, aliases=['domain']),
        ),
        supports_check_mode=True,
        required_if=([
            ('state', 'present', ['record', 'type', 'value']),
            ('state', 'absent', ['record']),
        ],
        ),
    )


    changed = False
    cf_api = CloudflareAPI(module)

    # sanity checks
    if cf_api.is_solo and cf_api.state == 'absent':
        module.fail_json(msg="solo=true can only be used with state=present")

    # perform add, delete or update (only the TTL can be updated) of one or
    # more records
    if cf_api.state == 'present':
        # delete all records matching record name + type
        if cf_api.is_solo:
            changed = cf_api.delete_dns_records(solo=cf_api.is_solo)
        result, changed = cf_api.ensure_dns_record()
        if isinstance(result, list):
            module.exit_json(changed=changed, result={'record': result[0]})

        module.exit_json(changed=changed, result={'record': result})
    else:
        # force solo to False, just to be sure
        changed = cf_api.delete_dns_records(solo=False)
        module.exit_json(changed=changed)


if __name__ == '__main__':
    main()
