```
$ time ansible-playbook launch-DO.yml

PLAY [provisioner] **************************************************************

TASK [Gather facts about SSH key (fingerprint look-up)] *************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner]

TASK [digital_ocean_sshkey_facts] ***********************************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner] => (item={u'public_key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyQ5wJKkduGWq7Q1Ar46F+gc61pQiuy6YXKI623/lnz1xVV8y58NSGI5AYs1e5thygB72ZWgZO1w7tXVxyJ3jGS1c1vHAG8myqcu5ZZYdX6rzZ7+HXpcsLTDuqPs8VUhTzDf8kUGwaiMEsG0sHsy98jupxF1iTojBjEmA7rixnVM+EA94Z7KrHmAS9yOYa9P6P0KrnwK4tAz3GtrxyEOGGs9kXQ9B88kQHvQvTTMVG26zbln0Yt3jSqvBIo4nD6gWiKtCsN0Y/2bSrCdy33C/HKr4uHizgHumruDsbECYtga/k7VOQrr3+uc5t7MpXLUxNdGBNN4hnBSrt/DVSSwm/ mz0@nb13', u'id': 23550519, u'name': u'ansible', u'fingerprint': u'04:39:43:86:22:6b:e6:fa:c0:22:38:2d:b2:91:13:9c'})

TASK [Find or create Droplet, then register in-memory] **************************
changed: [provisioner]

TASK [debug] ********************************************************************
ok: [provisioner] => {
    "msg": "Droplet de.x302.net 104.248.137.215 2a03:b0c0:3:e0::ee:5001"
}

TASK [Add droplet to in-memory (dynamic) inventory] *****************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [Check port 22 is open] ****************************************************
ok: [do1 -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [do1]

TASK [Confirm host connection works] ********************************************
ok: [do1]

TASK [Replace systemd (stage 1 - install sysvinit-core etc.)] *******************
changed: [do1]

TASK [Reboot to replace systemd (ETA 23 seconds) if sysvinit just installed] ****
changed: [do1]

TASK [Replace systemd (stage 2 - uninstall systemd)] ****************************
changed: [do1]

TASK [fail] *********************************************************************
skipping: [do1]

TASK [Check port 22 is open] ****************************************************
ok: [do1 -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [do1]

TASK [Check SSH port 2222, skip if 22 is OK] ************************************
skipping: [do1]

TASK [Set SSH port 2222 if check OK.] *******************************************
skipping: [do1]

TASK [Fail if neither SSH port is open] *****************************************
skipping: [do1]

TASK [Confirm host connection works] ********************************************
ok: [do1]

TASK [Setup SSH Port 2222 ; no UseDNS, AcceptEnv.] ******************************
changed: [do1] => (item={u'key': u'Port', u'value': 2222})
changed: [do1] => (item={u'key': u'UseDNS', u'value': u'no'})
changed: [do1] => (item={u'key': u'AcceptEnv', u'value': u''})

TASK [Restart sshd] *************************************************************
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
ok: [do1] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'MaxAuthTries', u'value': u'2'})
changed: [do1] => (item={u'key': u'LoginGraceTime', u'value': u'6'})
changed: [do1] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do1] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})

TASK [Create admin user] ********************************************************
changed: [do1]

TASK [Copy my ssh pubkey to $USERNAME on the new host] **************************
changed: [do1]

RUNNING HANDLER [restart sshd] **************************************************
ok: [do1]

RUNNING HANDLER [Reload sysctl] *************************************************
ok: [do1]

PLAY RECAP **********************************************************************
do1                        : ok=28   changed=17   unreachable=0    failed=0
provisioner                : ok=7    changed=1    unreachable=0    failed=0


real	3m46,814s
user	0m31,846s
sys	0m9,913s

$ time ansible-playbook destroy-DO.yml
Name of server to destroy:

PLAY [provisioner] **************************************************************

TASK [Gathering Facts] **********************************************************
ok: [provisioner]

TASK [Delete droplet] ***********************************************************
changed: [provisioner]

PLAY RECAP **********************************************************************
provisioner                : ok=2    changed=1    unreachable=0    failed=0

real	0m4,308s
user	0m1,784s
sys	0m0,398s
```
