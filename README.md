Digital Ocean Bootstrap
=======================


```
$ pip install dopy==0.3.5
$ ansible-playbook launch.yml 
```

![launch.yml playbook starts](/doc/do1-start.png?raw=true)
![launch.yml playbook finishes](/doc/do1-finish.png?raw=true)

Bootstrap Digital Ocean droplets using Ansible to:

* Configure SSH key
* Launch a droplet
* Destroy droplet

Inspired by [hostmaster/ansible-digitalocean-bootstrap](https://github.com/hostmaster/ansible-digitalocean-bootstrap).


Installation
------------

* Install [Ansible 2](http://docs.ansible.com/ansible/intro_installation.html)

* Install dopy-0.3.5

* Check vars.yml and change the variables to your need.


Digital Ocean configuration
---------------------------

Create a new API key on the [API access page](https://cloud.digitalocean.com/api_access). 
Add the api_token to the file referenced in `vars.yml`.


Playbooks
=========

launch.yml
----------

Launch and provision a new Ububntu droplet on Digital Ocean.

```
$ ansible-playbook launch.yml
```

What this Playbook does for you?

- configure swap file
- install ntp, ...
- make sshd more secure: 
  - PermitRootLogin=no
  - PasswordAuthentication=no
  - AllowGroups=sudo
- config sudoers

destroy.yml
-----------

Destroys a server on Digital Ocean.

```
$ ansible-playbook destroy.yml
```

Issues:
-----

If SSH key is already registered on DO with different name this playbook will fail. You may rename the key in launch.yml or remove it in DO to overcome this.

The launch.yml playbook is not "idempotent" - on second attempt it fails on prohibited root-login.

Checked with Ansible 2.7 from PPA on Ubuntu 18.04 notebook with Python 2.7
Last update Fri Nov 9, 2018.
