```
$ ansible-playbook launch.yml

PLAY [DigitalOcean] *********************************************************************

TASK [Ensure DO has SSH key 'ansible' registered] ***************************************
ok: [DigitalOcean]

TASK [Find or create Droplet, then register in-memory] **********************************
changed: [DigitalOcean]

TASK [debug] ****************************************************************************
ok: [DigitalOcean] => {
    "msg": "Droplet de.x302.net 178.128.198.20"
}

TASK [Add droplet to in-memory inventory] ***********************************************
ok: [DigitalOcean]

TASK [Wait for SSH connection] **********************************************************
 [WARNING]: Reset is not implemented for this connection

ok: [DigitalOcean]

PLAY [dohosts] **************************************************************************

TASK [Gathering Facts] ******************************************************************
ok: [de.x302.net]

TASK [Write swap file] ******************************************************************
changed: [de.x302.net]

TASK [Set swapfile permissions] *********************************************************
changed: [de.x302.net]

TASK [Create swapfile] ******************************************************************
changed: [de.x302.net]

TASK [Enable swapfile] ******************************************************************
changed: [de.x302.net]

TASK [Add swapfile to /etc/fstab] *******************************************************
changed: [de.x302.net]

TASK [Configure vm.swappiness] **********************************************************
changed: [de.x302.net]

TASK [Configure vm.vfs_cache_pressure] **************************************************
changed: [de.x302.net]

TASK [Install essential packages] *******************************************************
changed: [de.x302.net]

TASK [Ensure service is enabled and running] ********************************************
ok: [de.x302.net] => (item=openntpd)

TASK [Ensure sudoers.d is enabled] ******************************************************
ok: [de.x302.net]

TASK [Set up password-less sudo for admin users] ****************************************
changed: [de.x302.net]

TASK [Strict SSH access] ****************************************************************
ok: [de.x302.net] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [de.x302.net] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [de.x302.net] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [de.x302.net] => (item={u'key': u'MaxAuthTries', u'value': u'5'})
changed: [de.x302.net] => (item={u'key': u'LoginGraceTime', u'value': u'60'})
changed: [de.x302.net] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [de.x302.net] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})
ok: [de.x302.net] => (item={u'key': u'Port', u'value': 22})

TASK [Create admin user] ****************************************************************
changed: [de.x302.net]

TASK [Deploy ssh public key] ************************************************************
changed: [de.x302.net]

RUNNING HANDLER [restart sshd] **********************************************************
changed: [de.x302.net]

RUNNING HANDLER [Reload sysctl] *********************************************************
changed: [de.x302.net]

PLAY RECAP ******************************************************************************
DigitalOcean               : ok=5    changed=1    unreachable=0    failed=0
de.x302.net                : ok=17   changed=14   unreachable=0    failed=0

```
