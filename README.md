Digital Ocean Bootstrap
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

launch.yml
----------

Launch and provision a new Debian 8.11 x64 droplet on Digital Ocean.

```
$ ansible-playbook launch.yml
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

Issues:
-----

If SSH key is not registered on DO this playbook will fail (FIXME).

The launch.yml playbook was not "idempotent" - on the second attempt it failed on prohibited root-login.
(AllowGroups sudo) - sshd_config loosened a bit (2 lines commented out) until better solution is found.

If playbook failed on timeout you may restart it but do not use launch.retry (TODO: check if still true).
Start launch.yml again and input the same name as before so in-memory inventory is recreated by quering DO with API.

Checked with Ansible 2.7 from PPA on Ubuntu 18.04 with Python 2.7
Last update Nov 21, 2018.
