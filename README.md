Uniform cloud server environments
=======================

![launch.yml playbook starts](/doc/do1-start.png?raw=true)
![launch.yml playbook finishes](/doc/do1-finish.png?raw=true)

Installation
------------

* Install [Ansible 2.7.5](http://docs.ansible.com/ansible/intro_installation.html) or newer.

* Check do1.yml/ar1.yml and change the variables to your need.

Playbooks
=========

launch-DO.yml / destroy-DO.yml
----------

Launch / destroy a Debian 8.11 x64 droplet on Digital Ocean.

```
$ ansible-playbook launch-DO.yml
```

This Playbook will:

- replace systemd with sysvinit
- change SSH port 22 -> 2222 (set in do1.yml & hosts.ini)
- configure swap file
- install openntpd
- configure sshd (PasswordAuthentication=no etc.)
- configure sudoers
- trim packages (leave only needed ones)
- add 3rd-party repos for LEMP stack (Nginx, PHP5.6-7.3, MariaDB 10.x)
- install the .EMP parts

See install and run example: doc/do1-log.md

Note: your [API key](https://cloud.digitalocean.com/api_access) should be
in the file referenced by `do_api_token` in `do1.yml`.

relaunch-A.yml / listsrv-A.yml
----------

Re-launch a Debian 8.11 x64 "Smart" VM on
[Aruba Cloud](https://www.arubacloud.com/vps/virtual-private-server-range.aspx).
Configuration is very much alike the one above.

Note:

* "Smart" VMs are billed monthly - you do not want them killed and re-created
without second thought, and if you pay for them 1Euro/mo you likely don't want them deleted at all ;)

* put your username & password in a file like [doc/aruba-secrets.ini](doc/aruba-secrets.ini)

* `listsrv-A.yml` lets you check ArubaCloud server status, queued task and its progress.

* "Smart server" has Swap space pre-allocated as LVMs LV. We [reclaim this space](tasks/reclaim-swrsvd.yml)

Issues:
-----

launch-DO - If SSH key is not registered on DO this playbook will fail (FIXME).

The launch-DO.yml playbook was not "idempotent" - on the second attempt it failed on prohibited root-login.
(AllowGroups sudo) - sshd_config loosened a bit (AllowGroups line commented out, RootLogin enabled) until better solution is found.

If playbook failed on timeout you may restart it but do not use launch.retry (may need dynamic inventory - FIXME).
Re-running from the start is the only option now.
There's very little time lost in case of `launch-DO` in that case, `relaunch-A` is a different story ;)

Checked with Ansible 2.7 from PPA & 2.8dev0 on Ubuntu 18.04/18.10 with Python 2.7
Last update Dec 27, 2018.
