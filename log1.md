```
$ ansible-playbook launch.yml 
Name of server: do0

PLAY [localhost] **********************************************************************

TASK [Gathering Facts] ****************************************************************
ok: [localhost]

TASK [Register SSH key] ***************************************************************
ok: [localhost]

TASK [Find or create Droplet, then temp. register] ************************************
changed: [localhost]

TASK [debug] **************************************************************************
ok: [localhost] => {
    "msg": "IP is 104.248.249.127"
}

TASK [Add droplet to temp. inventory] *************************************************
changed: [localhost]

TASK [Wait 300 seconds for ssh connection, but only start checking after 10 seconds] **
 [WARNING]: Reset is not implemented for this connection

ok: [localhost]

PLAY [dohosts] ************************************************************************

TASK [Gathering Facts] ****************************************************************
The authenticity of host '104.248.249.127 (104.248.249.127)' can't be established.
ECDSA key fingerprint is SHA256:/DaFq6gZ7ffY0afEVnJWaeGJqg0mJQKkW/dKoShm7fA.
Are you sure you want to continue connecting (yes/no)? yes
ok: [do0]

TASK [Write swap file] ****************************************************************
changed: [do0]

TASK [Set swapfile permissions] *******************************************************
changed: [do0]

TASK [Create swapfile] ****************************************************************
changed: [do0]

TASK [Enable swapfile] ****************************************************************
changed: [do0]

TASK [Add swapfile to /etc/fstab] *****************************************************
changed: [do0]

TASK [Configure vm.swappiness] ********************************************************
changed: [do0]

TASK [Configure vm.vfs_cache_pressure] ************************************************
changed: [do0]

TASK [Install updates] ****************************************************************
changed: [do0]

TASK [Install essential packages] *****************************************************
changed: [do0]

TASK [Ensure services is running and enabled] *****************************************
ok: [do0] => (item=ntp)

TASK [Ensure sudoers.d is enabled] ****************************************************
ok: [do0]

TASK [Set up password-less sudo for admin users] **************************************
changed: [do0]

TASK [Strict SSH access] **************************************************************
changed: [do0] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [do0] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [do0] => (item={u'key': u'PermitRootLogin', u'value': u'no'})
ok: [do0] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do0] => (item={u'key': u'AllowGroups', u'value': u'sudo'})
changed: [do0] => (item={u'key': u'MaxAuthTries', u'value': u'5'})
changed: [do0] => (item={u'key': u'LoginGraceTime', u'value': u'60'})
changed: [do0] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do0] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})
changed: [do0] => (item={u'key': u'Port', u'value': 22})

TASK [Create admin user] **************************************************************
changed: [do0]

TASK [Deploy ssh public key] **********************************************************
changed: [do0]

RUNNING HANDLER [restart sshd] ********************************************************
changed: [do0]

RUNNING HANDLER [Reload sysctl] *******************************************************
changed: [do0]

PLAY RECAP ****************************************************************************
do0                        : ok=18   changed=15   unreachable=0    failed=0   
localhost                  : ok=6    changed=2    unreachable=0    failed=0
```
