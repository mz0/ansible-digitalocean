```
$ ansible-playbook --version
ansible-playbook 2.7.5
  config file = ./ansible.cfg
  configured module search path = []
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible-playbook
  python version = 2.7.15+ (default, Oct  2 2018, 22:12:08) [GCC 8.2.0]

$ time ansible-playbook relaunch-A.yml

PLAY [provisioner] **************************************************************

TASK [Ensure server is like new - re-image from current template - ETA 3-20 minutes]
changed: [provisioner]

TASK [Print result] *************************************************************
ok: [provisioner] => {
    "vm": {
        "changed": true,
        "failed": false,
        "srv": {
            "MAC": "00:50:56:9e:ae:44",
            "busy": false,
            "created": "2018-04-04T11:46:10",
            "dc": 1,
            "id": 292659,
            "ip4": "212.237.9.140",
            "ip6": "2a00:6d40:0060:928c:0000:0000:0000:0001",
            "isON": true,
            "jobs": [],
            "name": "La",
            "password0": "668a55c627579b903486ad91e998d288",
            "recharge": "2018-12-30T11:00:00",
            "size": "S",
            "templateId": 1723,
            "tplateName": "debian8_x64_1_0"
        }
    }
}

TASK [Add VM to in-memory (dynamic) inventory] **********************************
ok: [provisioner]

TASK [Delete existing SSH host keys] ********************************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [fail] *********************************************************************
skipping: [lab]

TASK [Check SSH port 22] ********************************************************
ok: [lab -> localhost]

TASK [Set ansible_port 22 if open] **********************************************
ok: [lab]

TASK [Check host connection] ****************************************************
ok: [lab]

TASK [Add ssh pubkey to ~root/.ssh/authorized_keys] *****************************
changed: [lab]

TASK [disable root password] ****************************************************
changed: [lab]

TASK [fix /etc/network/interfaces - set IPv6 address (if defined)] **************
changed: [lab]

TASK [Restart all (but 'lo') interfaces (ETA 3.25 seconds)] *********************
ok: [lab]

TASK [Check port 22 is open] ****************************************************
ok: [lab -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [lab]

TASK [Confirm host connection works] ********************************************
ok: [lab]

TASK [Replace systemd (stage 1 - install sysvinit-core etc.)] *******************
changed: [lab]

TASK [Reboot to replace systemd (ETA 23 seconds) if sysvinit just installed] ****
changed: [lab]

TASK [Replace systemd (stage 2 - uninstall systemd)] ****************************
changed: [lab]

TASK [fail] *********************************************************************
skipping: [lab]

TASK [Check port 22 is open] ****************************************************
ok: [lab -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [lab]

TASK [Check SSH port 2222, skip if 22 is OK] ************************************
skipping: [lab]

TASK [Set SSH port 2222 if check OK.] *******************************************
skipping: [lab]

TASK [Fail if neither SSH port is open] *****************************************
skipping: [lab]

TASK [Confirm host connection works] ********************************************
ok: [lab]

TASK [Setup SSH Port 2222 ; no UseDNS, AcceptEnv.] ******************************
changed: [lab] => (item={u'key': u'Port', u'value': 2222})
ok: [lab] => (item={u'key': u'UseDNS', u'value': u'no'})
changed: [lab] => (item={u'key': u'AcceptEnv', u'value': u''})

TASK [Restart sshd] *************************************************************
ok: [lab]

TASK [Write swap file] **********************************************************
changed: [lab]

TASK [Set swapfile permissions] *************************************************
changed: [lab]

TASK [Create swapfile] **********************************************************
changed: [lab]

TASK [Enable swapfile] **********************************************************
changed: [lab]

TASK [Add swapfile to /etc/fstab] ***********************************************
changed: [lab]

TASK [Configure vm.swappiness] **************************************************
changed: [lab]

TASK [Configure vm.vfs_cache_pressure] ******************************************
changed: [lab]

TASK [Install updates] **********************************************************
changed: [lab]

TASK [Install essential packages] ***********************************************
changed: [lab]

TASK [Ensure service is enabled and running] ************************************
ok: [lab] => (item=openntpd)

TASK [Ensure sudoers.d is enabled] **********************************************
ok: [lab]

TASK [Set up password-less sudo for admin users] ********************************
changed: [lab]

TASK [Strict SSH access] ********************************************************
ok: [lab] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [lab] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [lab] => (item={u'key': u'PermitRootLogin', u'value': u'without-password'})
changed: [lab] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [lab] => (item={u'key': u'MaxAuthTries', u'value': u'2'})
changed: [lab] => (item={u'key': u'LoginGraceTime', u'value': u'6'})
changed: [lab] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [lab] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})

TASK [Create admin user] ********************************************************
changed: [lab]

TASK [Copy my ssh pubkey to $USERNAME on the new host] **************************
changed: [lab]

RUNNING HANDLER [restart sshd] **************************************************
ok: [lab]

RUNNING HANDLER [Reload sysctl] *************************************************
ok: [lab]

PLAY RECAP **********************************************************************
lab                        : ok=35   changed=20   unreachable=0    failed=0
provisioner                : ok=4    changed=1    unreachable=0    failed=0

real	6m36,783s
user	0m48,147s
sys	0m14,362s
```
