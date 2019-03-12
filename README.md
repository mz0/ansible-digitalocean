Uniform cloud server environments
=======================

This is unfinished monolithik playbook transformation to a role-based one. Not much is working now!

Installation
------------

* Install Ansible 2.7.8 or newer (e.g. `pip install --user -r requirements.txt`).

* Check do1.yml/ar1.yml and change the variables to your need.

* Install `sshpass` for ArubaCloud (in Ubuntu enable `universe` repo & `apt install sshpass`).

Playbooks
=========

This Playbook should:

- create/rebuild a VM (droplet in DO parlance), currently only Debian 8 x64 is the target.
- replace systemd with sysvinit (Debian supports it, but not Ubuntu/Fedora)
- change SSH port 22 -> 2222 (to lower script-kiddies generated noise)
- configure swap file
- install openntpd
- configure sshd (PasswordAuthentication=no etc.)
- configure sudoers
- trim packages (leave only needed ones)
- add 3rd-party repos for LEMP stack (Nginx, PHP5.6-7.3, MariaDB 10.x)
- install the .EMP parts


DigitalOcean users, please note:
----------

* your [API key](https://cloud.digitalocean.com/api_access) should be
in the file referenced by `do_api_token` in `do1.yml`.

* register SSH key in DO (link TBD).

ArubaCloud users, please note:
----------

* This palybook (role) works only with ["Smart" VMs](https://www.arubacloud.com/vps/virtual-private-server-range.aspx). They are billed monthly - you
do not want them killed and re-created without second thought, and if you pay for current one 1Euro/mo but the same new one will cost 2.79 likely
you don't want them deleted at all.

* put your username & password in a file like [doc/aruba-secrets.ini](doc/aruba-secrets.ini)

* `listsrv-A.yml` lets you check ArubaCloud server status, queued task and its progress.

* "Smart server" has Swap space pre-allocated as LVMs LV. We [reclaim this space](TBD)

Checked with Ansible 2.7 & 2.8dev0 on Ubuntu 18.04/18.10.
Last update March 5, 2019.
