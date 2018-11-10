```
$ time ansible-playbook launch.yml
Name of server: do1

PLAY [localhost] *****************************************************************

TASK [Gathering Facts] ***********************************************************
ok: [localhost]

TASK [Register SSH key] **********************************************************
ok: [localhost]

TASK [Find or create Droplet, then temp. register] *******************************
changed: [localhost]

TASK [debug] *********************************************************************
ok: [localhost] => {
    "msg": "IP is 68.183.64.13"
}

TASK [Add droplet to in-memory inventory] ****************************************
changed: [localhost]

TASK [Wait for SSH connection] ***************************************************
 [WARNING]: Reset is not implemented for this connection

ok: [localhost]

PLAY [dohosts] *******************************************************************

TASK [Gathering Facts] ***********************************************************
ok: [do1]

TASK [Write swap file] ***********************************************************
changed: [do1]

TASK [Set swapfile permissions] **************************************************
changed: [do1]

TASK [Create swapfile] ***********************************************************
changed: [do1]

TASK [Enable swapfile] ***********************************************************
changed: [do1]

TASK [Add swapfile to /etc/fstab] ************************************************
changed: [do1]

TASK [Configure vm.swappiness] ***************************************************
changed: [do1]

TASK [Configure vm.vfs_cache_pressure] *******************************************
changed: [do1]

TASK [Install updates] ***********************************************************
changed: [do1]

TASK [Install essential packages] ************************************************
changed: [do1]

TASK [Ensure services is running and enabled] ************************************
ok: [do1] => (item=ntp)

TASK [Ensure sudoers.d is enabled] ***********************************************
ok: [do1]

TASK [Set up password-less sudo for admin users] *********************************
changed: [do1]

TASK [Strict SSH access] *********************************************************
changed: [do1] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [do1] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'PermitRootLogin', u'value': u'no'})
ok: [do1] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'AllowGroups', u'value': u'sudo'})
changed: [do1] => (item={u'key': u'MaxAuthTries', u'value': u'5'})
changed: [do1] => (item={u'key': u'LoginGraceTime', u'value': u'60'})
changed: [do1] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do1] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})
changed: [do1] => (item={u'key': u'Port', u'value': 22})

TASK [Create admin user] *********************************************************
changed: [do1]

TASK [Deploy ssh public key] *****************************************************
changed: [do1]

RUNNING HANDLER [restart sshd] ***************************************************
changed: [do1]

RUNNING HANDLER [Reload sysctl] **************************************************
changed: [do1]

PLAY RECAP ***********************************************************************
do1                        : ok=18   changed=15   unreachable=0    failed=0   
localhost                  : ok=6    changed=2    unreachable=0    failed=0   


real	4m12,104s
user	0m32,541s
sys	0m8,726s
```
