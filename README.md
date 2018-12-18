Cloud server Bootstrap
=======================

![launch.yml playbook starts](/doc/do1-start.png?raw=true)
![launch.yml playbook finishes](/doc/do1-finish.png?raw=true)

Digital Ocean configuration
---------------------------

Create a new API key on the [API access page](https://cloud.digitalocean.com/api_access). 
Add the api_token to the file referenced in `vars.yml`.

Installation
------------

* Install [Ansible 2](http://docs.ansible.com/ansible/intro_installation.html)

* Check vars.yml and change the variables to your need.

Playbooks
=========

launch-DO.yml
----------

Launch and provision a new Debian 8.11 x64 droplet on Digital Ocean.

```
$ ansible-playbook launch-DO.yml
```

This Playbook will:

- configure swap file
- install openntpd
- configure sshd (PasswordAuthentication=no etc.)
- configure sudoers

See example output: doc/do1-log.md

destroy.yml
-----------

Destroy your droplet.

```
$ ansible-playbook destroy.yml
```

launch-A.yml
----------

Re-launch Debian 8.11 x64 "Smart" VM on
[Aruba Cloud](https://www.arubacloud.com/vps/virtual-private-server-range.aspx).
See requirements in [launch-A.md](launch-A.md).
Note: "Smart" VMs are billed monthly - you do not want them killed and re-created
without second thought, especially if you have them for €1/mo :wink:

Issues:
-----

If SSH key is not registered on DO this playbook will fail (FIXME).

The launch.yml playbook was not "idempotent" - on the second attempt it failed on prohibited root-login.
(AllowGroups sudo) - sshd_config loosened a bit (AllowGroups line commented out, RootLogin enabled) until better solution is found.

If playbook failed on timeout you may restart it but do not use launch.retry (may need dynamic inventory - FIXME).
Start launch.yml again and input the same name as before so in-memory inventory is recreated by quering DO with API.

Checked with Ansible 2.7 from PPA on Ubuntu 18.04/18.10 with Python 2.7
Last update Dec 17, 2018.
