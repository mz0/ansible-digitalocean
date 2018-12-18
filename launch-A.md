Requirements
------------

# get modules: *ANSIBLEDEVDIR=/foo/bar; git clone git@github.com:mz0/ansible.git $ANSIBLEDEVDIR*
# activate & check it:
```
$ pushd $ANSIBLEDEVDIR
$ . /hacking/env-setup
$ popd

$ ansible --version
ansible 2.8.0.dev0 (aruba-smart 96456eea13) last updated ...
  config file = $ANSIBLEDEVDIR/ansible.cfg
  configured module search path = ['~/.ansible/plugins/modules', ...]
  ansible python module location = $ANSIBLEDEVDIR/lib/ansible
  executable location = $ANSIBLEDEVDIR/bin/ansible
  python version = ...
``` 
