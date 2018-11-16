```
mz0@nb13:/shr/bemigot/do1$ ansible-playbook launch.yml

PLAY [provisioner] **************************************************************

TASK [Ensure DO has SSH key 'ansible' registered] *******************************
ok: [provisioner]

TASK [Find or create Droplet, then register in-memory] **************************
ok: [provisioner]

TASK [Add droplet to in-memory (dynamic) inventory] *****************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [Gathering Facts] **********************************************************
ok: [do1]

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
changed: [do1] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'MaxAuthTries', u'value': u'5'})
changed: [do1] => (item={u'key': u'LoginGraceTime', u'value': u'60'})
changed: [do1] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do1] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})
ok: [do1] => (item={u'key': u'Port', u'value': 22})

TASK [Create admin user] ********************************************************
changed: [do1]

TASK [Deploy ssh public key] ****************************************************
changed: [do1]

RUNNING HANDLER [restart sshd] **************************************************
changed: [do1]

RUNNING HANDLER [Reload sysctl] *************************************************
changed: [do1]

PLAY RECAP **********************************************************************
do1                        : ok=17   changed=14   unreachable=0    failed=0   
provisioner                : ok=3    changed=0    unreachable=0    failed=0   

mz0@nb13:/shr/bemigot/do1$ ansible-playbook destroy.yml 
Name of server to destroy: de1.x302.net

PLAY [provisioner] **************************************************************

TASK [Gathering Facts] **********************************************************
ok: [provisioner]

TASK [Delete droplet] ***********************************************************
changed: [provisioner]

PLAY RECAP **********************************************************************
provisioner                : ok=2    changed=1    unreachable=0    failed=0   

mz0@nb13:/shr/bemigot/do1$
```
