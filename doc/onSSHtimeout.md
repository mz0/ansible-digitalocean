fatal: [do1]: UNREACHABLE! => {"changed": false, "msg": "Failed to connect to the host via ssh: ssh: connect to host 46.101.236.62 port 22: Connection refused\r\n", "unreachable": true}

after priv_key removal
no timeout changes where effective
looks like a problem with net routes then ssh problem
restored "wait for ssh connection" task to mitigate this
