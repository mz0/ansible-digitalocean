```
$ time ansible-playbook launch.yml

PLAY [provisioner] **************************************************************

TASK [Gather facts about SSH key (fingerprint look-up)] *************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner]

TASK [digital_ocean_sshkey_facts] ***********************************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner] => (item={u'public_key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyQ5wJKkduGWq7Q1Ar46F+gc61pQiuy6YXKI623/lnz1xVV8y58NSGI5AYs1e5thygB72ZWgZO1w7tXVxyJ3jGS1c1vHAG8myqcu5ZZYdX6rzZ7+HXpcsLTDuqPs8VUhTzDf8kUGwaiMEsG0sHsy98jupxF1iTojBjEmA7rixnVM+EA94Z7KrHmAS9yOYa9P6P0KrnwK4tAz3GtrxyEOGGs9kXQ9B88kQHvQvTTMVG26zbln0Yt3jSqvBIo4nD6gWiKtCsN0Y/2bSrCdy33C/HKr4uHizgHumruDsbECYtga/k7VOQrr3+uc5t7MpXLUxNdGBNN4hnBSrt/DVSSwm/ mz0@nb13', u'id': 23550519, u'name': u'ansible', u'fingerprint': u'04:39:43:86:22:6b:e6:fa:c0:22:38:2d:b2:91:13:9c'})

TASK [debug] ********************************************************************
ok: [provisioner] => {
    "msg": "SSH key 04:39:43:86:22:6b:e6:fa:c0:22:38:2d:b2:91:13:9c found, id=23550519, name=ansible"
}

TASK [Find or create Droplet, then register in-memory] **************************
changed: [provisioner]

TASK [Add droplet to in-memory (dynamic) inventory] *****************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [Wait for SSH connection to a new droplet (some 4-5 seconds is OK)] ********
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

TASK [Copy my ssh pubkey to $USERNAME on the new droplet] ***********************
changed: [do1]

RUNNING HANDLER [restart sshd] **************************************************
changed: [do1]

RUNNING HANDLER [Reload sysctl] *************************************************
changed: [do1]

PLAY RECAP **********************************************************************
do1                        : ok=17   changed=14   unreachable=0    failed=0
provisioner                : ok=7    changed=1    unreachable=0    failed=0


real	1m53,327s
user	0m18,626s
sys	0m6,611s

$ time ansible-playbook destroy.yml
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
