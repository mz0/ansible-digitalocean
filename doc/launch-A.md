Requirements
------------

* get modules (set proper ~/foo :wink:):
```
$ ANSIBLEDEVDIR=~/foo
$ mkdir $ANSIBLEDEVDIR && git clone git@github.com:mz0/ansible.git $ANSIBLEDEVDIR
```

* activate & check it:
```
$ source $ANSIBLEDEVDIR/hacking/env-setup
  running egg_info ... Setting up Ansible to run out of checkout... Done!

$ ansible --version
ansible 2.8.0.dev0 (aruba-smart 96456eea13) last updated ...
  config file = $ANSIBLEDEVDIR/ansible.cfg
  configured module search path = ['~/.ansible/plugins/modules', ...]
  ansible python module location = $ANSIBLEDEVDIR/lib/ansible
  executable location = $ANSIBLEDEVDIR/bin/ansible
  python version = ...
``` 
