#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# a copy of digital_ocean_domain.py by @mgregson added in 1.6

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'status': ['preview'],
                    'supported_by': 'community',
                    'metadata_version': '1.1'}


DOCUMENTATION = '''
---
module: digital_ocean_droplet
short_description: Create/find/delete your DigitalOcean VM
description:
     - Create/find/delete your DigitalOcean droplet.
version_added: "2.?"
author: "Michael Gregson (@mgregson)"
options:
  state:
    description:
     - Indicate desired state of the target.
    default: present
    choices: ['present', 'absent']
  id:
    description:
     - Numeric, the droplet id you want to operate on.
    aliases: ['droplet_id']
  name:
    description:
     - String, this is the name of the droplet - may be a FQDN or just a hostname.
extends_documentation_fragment: digital_ocean.documentation
notes:
  - Environment variable DO_OAUTH_TOKEN can be used for the oauth_token.
  - Since Ansible 1.9.5 and 2.0, DigitalOcean APIv2 is used, removes C(client_id) and C(api_key) options in favor of C(oauth_token).

requirements:
  - "python >= 2.6"
'''


EXAMPLES = '''
- digital_ocean_droplet:
    oauth_token: "{{ my_do_key }}"
    state: present
    name: do1 # or do1.example.net
    region_id: fra1 # TODO find regions how?
    size_id: 1gb
    image_id: debian-8-x64
    ssh_key_ids: 23550519
    unique_name: yes
    ipv6: no
    private_networking: no
   #wait_timeout: 240 # default is 300 (5 minutes), usually it's under 2 minutes.
   register: my_droplet

- debug:
    msg: "Droplet named: {{ my_droplet.droplet.name }} has IP: {{ my_droplet.droplet.ip_address }}"
'''


RETURN = '''
# Digital Ocean API info https://developers.digitalocean.com/documentation/v2/#list-all-keys
data:
    description: List of SSH keys on DigitalOcean
    returned: success and no resource constraint
    type: dict
    sample: {
      "ssh_keys": [
        {
          "id": 512189,
          "fingerprint": "3b:16:bf:e4:8b:00:8b:b8:59:8c:a9:d3:f0:19:45:fa",
          "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAAAQQDDHr/jh2Jy4yALcK4JyWbVkPRaWmhck3IgCoeOO3z1e2dBowLh64QAM+Qb72pxekALga2oi4GvT+TlWNhzPH4V example",
          "name": "My SSH Public Key"
        }
      ],
      "links": {
      },
      "meta": {
        "total": 1
      }
    }
'''

import traceback
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.digital_ocean import DigitalOceanHelper
from ansible.module_utils._text import to_native


class DoManager(DigitalOceanHelper, object):
    def __init__(self, module):
        super(DoManager, self).__init__(module)
        self.domain_name = module.params.get('name', None)
        self.domain_ip = module.params.get('ip', None)
        self.domain_id = module.params.get('id', None)

    @staticmethod
    def jsonify(response):
        return response.status_code, response.json

    def all_domains(self):
        resp = self.get('domains/')
        return resp

    def find(self):
        if self.domain_name is None and self.domain_id is None:
            return False

        domains = self.all_domains()
        status, json = self.jsonify(domains)
        for domain in json['domains']:
            if domain['name'] == self.domain_name:
                return True
        return False

    def add(self):
        params = {'name': self.domain_name, 'ip_address': self.domain_ip}
        resp = self.post('domains/', data=params)
        status = resp.status_code
        json = resp.json
        if status == 201:
            return json['domain']
        else:
            return json

    def all_domain_records(self):
        resp = self.get('domains/%s/records/' % self.domain_name)
        return resp.json

    def domain_record(self):
        resp = self.get('domains/%s' % self.domain_name)
        status, json = self.jsonify(resp)
        return json

    def destroy_domain(self):
        resp = self.delete('domains/%s' % self.domain_name)
        status, json = self.jsonify(resp)
        if status == 204:
            return True
        else:
            return json

    def edit_domain_record(self):
        params = {'name': self.domain_name}
        resp = self.put('domains/%s/records/%s' % (self.domain_name, self.domain_id), data=params)
        status, json = self.jsonify(resp)
        return json['domain_record']

#def core(module):
#    rest = DigitalOceanHelper(module)
#    response = rest.get("account/keys")
#    status_code = response.status_code
#    json = response.json
#    if status_code == 200:
#        module.exit_json(changed=False, ansible_facts=json)
#    else:
#        module.fail_json(msg='Error fetching facts [{0}: {1}]'.format(
#            status_code, response.json['message']))

def core(module):
    do_manager = DoManager(module)
    state = module.params.get('state')

    domain = do_manager.find()
    if state == 'present':
        if not domain:
            domain = do_manager.add()
            if 'message' in domain:
                module.fail_json(changed=False, msg=domain['message'])
            else:
                module.exit_json(changed=True, domain=domain)
        else:
            records = do_manager.all_domain_records()
            at_record = None
            for record in records['domain_records']:
                if record['name'] == "@" and record['type'] == 'A':
                    at_record = record

            if not at_record['data'] == module.params.get('ip'):
                do_manager.edit_domain_record()
                module.exit_json(changed=True, domain=do_manager.find())
            else:
                module.exit_json(changed=False, domain=do_manager.domain_record())

    elif state == 'absent':
        if not domain:
            module.exit_json(changed=False, msg="Domain not found")
        else:
            delete_event = do_manager.destroy_domain()
            if not delete_event:
                module.fail_json(changed=False, msg=delete_event['message'])
            else:
                module.exit_json(changed=True, event=None)
        delete_event = do_manager.destroy_domain()
        module.exit_json(changed=delete_event)


def main():
    argument_spec = DigitalOceanHelper.digital_ocean_argument_spec()
    argument_spec.update(
        state=dict(choices=['present', 'absent'], default='present'),
        name=dict(type='str'),
        id=dict(aliases=['droplet_id'], type='int'),
        ip=dict(type='str')
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
        required_one_of=(
            ['id', 'name'],
        ),
        supports_check_mode=False,
    )

    try:
        core(module)
    except Exception as e:
        module.fail_json(msg=to_native(e), exception=traceback.format_exc())


if __name__ == '__main__':
    main()
