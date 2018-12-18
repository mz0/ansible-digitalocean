```
$ time ansible-playbook launch-A.yml 

PLAY [provisioner] **************************************************************

TASK [Ensure server is like new - reinit (re-image) from current template - ETA 3-20 minutes]
changed: [provisioner]

TASK [Print result] *************************************************************
ok: [provisioner] => {
    "r1": {
        "changed": true, 
        "failed": false, 
        "srv": {
            "MAC": "00:50:56:9e:a9:50", 
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

TASK [Delete existing SSH host key] *********************************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [Wait for SSH connection to VM (some 4-5 seconds is OK)] *******************
ok: [do1]

TASK [Add ssh pubkey to ~root/.ssh/authorized_keys] *****************************
changed: [do1]

TASK [disable root password] ****************************************************
changed: [do1]

TASK [Write swap file] **********************************************************
changed: [do1]

TASK [Set swapfile permissions] *************************************************
changed: [do1]

TASK [Create swapfile] **********************************************************
changed: [do1]

TASK [Enable swapfile] **********************************************************
changed: [do1]

TASK [Add swapfile to /etc/fstab] ***********************************************
changed: [do1]

TASK [Configure vm.swappiness] **************************************************
changed: [do1]

TASK [Configure vm.vfs_cache_pressure] ******************************************
changed: [do1]

TASK [Install updates] **********************************************************
changed: [do1]

TASK [Install essential packages] ***********************************************
changed: [do1]

TASK [Ensure service is enabled and running] ************************************
ok: [do1] => (item=openntpd)

TASK [Ensure sudoers.d is enabled] **********************************************
ok: [do1]

TASK [Set up password-less sudo for admin users] ********************************
changed: [do1]

TASK [Strict SSH access] ********************************************************
ok: [do1] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [do1] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'PermitRootLogin', u'value': u'without-password'})
changed: [do1] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'MaxAuthTries', u'value': u'2'})
changed: [do1] => (item={u'key': u'LoginGraceTime', u'value': u'6'})
changed: [do1] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do1] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})
ok: [do1] => (item={u'key': u'Port', u'value': 22})

TASK [Create admin user] ********************************************************
changed: [do1]

TASK [Copy my ssh pubkey to $USERNAME on the new droplet] ***********************
changed: [do1]

RUNNING HANDLER [restart sshd] **************************************************
changed: [do1]

RUNNING HANDLER [Reload sysctl] *************************************************
changed: [do1]

PLAY RECAP **********************************************************************
do1                        : ok=20   changed=17   unreachable=0    failed=0   
provisioner                : ok=4    changed=1    unreachable=0    failed=0

real	4m10,904s
user	0m24,266s
sys	0m5,690s
```
