```
$ ansible-playbook --version
ansible-playbook 2.7.5
  config file = ./ansible.cfg
  configured module search path = []
  ansible python module location = /usr/lib/python2.7/dist-packages/ansible
  executable location = /usr/bin/ansible-playbook
  python version = 2.7.15+ (default, Oct  2 2018, 22:12:08) [GCC 8.2.0]
$ time ansible-playbook relaunch-A.yml

PLAY [provisioner] **************************************************************

TASK [Ensure server is like new - re-image from current template - ETA 3-20 minutes]
changed: [provisioner]

TASK [Print result] *************************************************************
ok: [provisioner] => {
    "vm": {
        "changed": true,
        "failed": false,
        "srv": {
            "MAC": "00:50:56:9e:ae:44",
            "busy": false,
            "created": "2018-04-04T11:46:10",
            "dc": 1,
            "id": 292659,
            "ip4": "212.237.9.140",
            "ip6": "2a00:6d40:0060:928c:0000:0000:0000:0001",
            "isON": true,
            "jobs": [],
            "name": "La",
            "password0": "668a55c627579b903486ad91e998d288",
            "recharge": "2018-12-30T11:00:00",
            "size": "S",
            "templateId": 1723,
            "tplateName": "debian8_x64_1_0"
        }
    }
}

TASK [Add VM to in-memory (dynamic) inventory] **********************************
ok: [provisioner]

TASK [Delete existing SSH host keys] ********************************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [fail] *********************************************************************
skipping: [lab]

TASK [Check SSH port 22] ********************************************************
ok: [lab -> localhost]

TASK [Set ansible_port 22 if open] **********************************************
ok: [lab]

TASK [Check host connection] ****************************************************
ok: [lab]

TASK [Add ssh pubkey to ~root/.ssh/authorized_keys] *****************************
changed: [lab]

TASK [disable root password] ****************************************************
changed: [lab]

TASK [fix /etc/network/interfaces - set IPv6 address (if defined)] **************
changed: [lab]

TASK [Restart all (but 'lo') interfaces (ETA 3.25 seconds)] *********************
ok: [lab]

TASK [Check port 22 is open] ****************************************************
ok: [lab -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [lab]

TASK [Confirm host connection works] ********************************************
ok: [lab]

TASK [Replace systemd (stage 1 - install sysvinit-core etc.)] *******************
changed: [lab]

TASK [Reboot to replace systemd (ETA 23 seconds) if sysvinit just installed] ****
changed: [lab]

TASK [Replace systemd (stage 2 - uninstall systemd)] ****************************
changed: [lab]

TASK [fail] *********************************************************************
skipping: [lab]

TASK [Check port 22 is open] ****************************************************
ok: [lab -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [lab]

TASK [Check SSH port 2222, skip if 22 is OK] ************************************
skipping: [lab]

TASK [Set SSH port 2222 if check OK.] *******************************************
skipping: [lab]

TASK [Fail if neither SSH port is open] *****************************************
skipping: [lab]

TASK [Confirm host connection works] ********************************************
ok: [lab]

TASK [Setup SSH Port 2222 ; no UseDNS, AcceptEnv.] ******************************
changed: [lab] => (item={u'key': u'Port', u'value': 2222})
ok: [lab] => (item={u'key': u'UseDNS', u'value': u'no'})
changed: [lab] => (item={u'key': u'AcceptEnv', u'value': u''})

TASK [Restart sshd] *************************************************************
ok: [lab]

TASK [check presence of /dev/vg/lv_swap] ****************************************
ok: [lab]

TASK [Set flag if swap space was found] *****************************************
ok: [lab]

TASK [Set skip flag when swap space not found] **********************************
skipping: [lab]

TASK [turn-off swap] ************************************************************
changed: [lab]

TASK [delete swap from /etc/fstab] **********************************************
changed: [lab]

TASK [delete LV] ****************************************************************
changed: [lab]

TASK [extend LV lv_root] ********************************************************
changed: [lab]

TASK [extend lv_root's / filesystem] ********************************************
changed: [lab]

TASK [Install updates] **********************************************************
changed: [lab]

TASK [Install essential packages] ***********************************************
changed: [lab]

TASK [Ensure service is enabled and running] ************************************
ok: [lab] => (item=openntpd)

TASK [Ensure sudoers.d is enabled] **********************************************
ok: [lab]

TASK [Set up password-less sudo for admin users] ********************************
changed: [lab]

TASK [Strict SSH access] ********************************************************
ok: [lab] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [lab] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [lab] => (item={u'key': u'PermitRootLogin', u'value': u'without-password'})
changed: [lab] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [lab] => (item={u'key': u'MaxAuthTries', u'value': u'2'})
changed: [lab] => (item={u'key': u'LoginGraceTime', u'value': u'6'})
changed: [lab] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [lab] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})

TASK [Create admin user] ********************************************************
changed: [lab]

TASK [Copy my ssh pubkey to $USERNAME on the new host] **************************
changed: [lab]

TASK [Purge unused packages] ****************************************************
changed: [lab]

TASK [debug] ********************************************************************
ok: [lab] => {
    "uninstall": {
        "changed": true,
        "diff": {},
        "failed": false,
        "stderr": "",
        "stderr_lines": [],
        "stdout_lines": [
            "Reading package lists...",
            "Building dependency tree...",
            "Reading state information...",
            "The following extra packages will be installed:",
            "  pinentry-curses",
            "Suggested packages:",
            "  pinentry-doc",
            "The following packages will be REMOVED:",
            "  acpi* apt-listchanges* aptitude* aptitude-common* aptitude-doc-en* arping*",
            "  at* bash-completion* bind9-host* console-setup* console-setup-linux* dbus*",
            "  debconf-i18n* debian-faq* dictionaries-common* discover* discover-data*",
            "  dmidecode* dnsutils* doc-debian* docutils-common* docutils-doc* eject*",
            "  emacsen-common* ethtool* fail2ban* firmware-linux-free* fontconfig*",
            "  fontconfig-config* fonts-dejavu-core* ftp* gcc-4.8-base* geoip-database*",
            "  hicolor-icon-theme* host* iamerican* ibritish* ienglish-common* info*",
            "  install-info* installation-report* irqbalance* isc-dhcp-client*",
            "  isc-dhcp-common* iso-codes* ispell* keyboard-configuration* krb5-locales*",
            "  laptop-detect* libalgorithm-c3-perl* libatk1.0-0* libatk1.0-data*",
            "  libauthen-sasl-perl* libavahi-client3* libavahi-common-data*",
            "  libavahi-common3* libbind9-90* libcairo2* libcap-ng0* libcgi-fast-perl*",
            "  libcgi-pm-perl* libclass-accessor-perl* libclass-c3-perl*",
            "  libclass-c3-xs-perl* libclass-isa-perl* libcups2* libcwidget3*",
            "  libdata-optlist-perl* libdata-section-perl* libdatrie1* libdbus-1-3*",
            "  libdiscover2* libdns-export100* libdns100* libdumbnet1*",
            "  libencode-locale-perl* libevent-2.0-5* libfcgi-perl* libfile-listing-perl*",
            "  libfont-afm-perl* libfontconfig1* libgc1c2* libgdk-pixbuf2.0-0*",
            "  libgdk-pixbuf2.0-common* libgeoip1* libglib2.0-0* libglib2.0-data*",
            "  libgpgme11* libgpm2* libgraphite2-3* libgtk2.0-0* libgtk2.0-bin*",
            "  libgtk2.0-common* libharfbuzz0b* libhtml-form-perl* libhtml-format-perl*",
            "  libhtml-parser-perl* libhtml-tagset-perl* libhtml-tree-perl*",
            "  libhttp-cookies-perl* libhttp-daemon-perl* libhttp-date-perl*",
            "  libhttp-message-perl* libhttp-negotiate-perl* libintl-perl* libio-html-perl*",
            "  libio-socket-ip-perl* libio-socket-ssl-perl* libio-string-perl*",
            "  libirs-export91* libisc-export95* libisc95* libisccc90* libisccfg-export90*",
            "  libisccfg90* libjasper1* libjbig0* libjpeg62-turbo* liblcms2-2*",
            "  liblockfile1* liblwp-mediatypes-perl* liblwp-protocol-https-perl*",
            "  liblwres90* libmailtools-perl* libmro-compat-perl* libnet-http-perl*",
            "  libnet-smtp-ssl-perl* libnet-ssleay-perl* libnet1* libnfsidmap2* libnuma1*",
            "  libpango-1.0-0* libpangocairo-1.0-0* libpangoft2-1.0-0* libpaper-utils*",
            "  libpaper1* libparams-util-perl* libparse-debianchangelog-perl* libparted2*",
            "  libpcap0.8* libpci3* libpixman-1-0* libsensors4* libsigsegv2*",
            "  libsoftware-license-perl* libsub-exporter-perl* libsub-install-perl*",
            "  libsub-name-perl* libtext-template-perl* libtext-unidecode-perl*",
            "  libthai-data* libthai0* libtiff5* libtimedate-perl* libtirpc1*",
            "  libtokyocabinet9* liburi-perl* libuuid-perl* libwebp5* libwebpdemux1*",
            "  libwebpmux1* libwww-perl* libwww-robotrules-perl* libx11-6* libx11-data*",
            "  libxapian22* libxau6* libxcb-render0* libxcb-shm0* libxcb1* libxcomposite1*",
            "  libxcursor1* libxdamage1* libxdmcp6* libxext6* libxfixes3* libxi6*",
            "  libxinerama1* libxml-libxml-perl* libxml-namespacesupport-perl*",
            "  libxml-parser-perl* libxml-sax-base-perl* libxml-sax-expat-perl*",
            "  libxml-sax-perl* libxml2* libxmuu1* libxrandr2* libxrender1*",
            "  linux-image-3.16.0-4-amd64* linux-image-amd64* lrzsz* lsb-release* m4*",
            "  man-db* manpages* mutt* nano* nfs-common* open-vm-tools* os-prober* parted*",
            "  pciutils* pinentry-gtk2* procmail* python-cffi* python-chardet*",
            "  python-cryptography* python-debian* python-debianbts* python-defusedxml*",
            "  python-docutils* python-ndg-httpsclient* python-openssl* python-pil*",
            "  python-pkg-resources* python-ply* python-pyasn1* python-pycparser*",
            "  python-pygments* python-pyinotify* python-reportbug* python-requests*",
            "  python-roman* python-six* python-soappy* python-urllib3* python-wstools*",
            "  rename* reportbug* rpcbind* sgml-base* shared-mime-info* sysstat*",
            "  task-english* task-ssh-server* tasksel* tasksel-data* tcpd* texinfo*",
            "  util-linux-locales* vim* vim-runtime* w3m* wamerican* wget* xauth*",
            "  xdg-user-dirs* xkb-data* xml-core* zerofree*",
            "The following NEW packages will be installed:",
            "  pinentry-curses",
            "0 upgraded, 1 newly installed, 250 to remove and 0 not upgraded.",
            "Need to get 29.3 kB of archives.",
            "After this operation, 412 MB disk space will be freed.",
            "Get:1 http://mirror.unitedcolo.de/debian/ jessie/main pinentry-curses amd64 0.8.3-2 [29.3 kB]",
            "Fetched 29.3 kB in 0s (323 kB/s)",
            "(Reading database ... ",
            "(Reading database ... 5%",
            "(Reading database ... 10%",
            "(Reading database ... 15%",
            "(Reading database ... 20%",
            "(Reading database ... 25%",
            "(Reading database ... 30%",
            "(Reading database ... 35%",
            "(Reading database ... 40%",
            "(Reading database ... 45%",
            "(Reading database ... 50%",
            "(Reading database ... 55%",
            "(Reading database ... 60%",
            "(Reading database ... 65%",
            "(Reading database ... 70%",
            "(Reading database ... 75%",
            "(Reading database ... 80%",
            "(Reading database ... 85%",
            "(Reading database ... 90%",
            "(Reading database ... 95%",
            "(Reading database ... 100%",
            "(Reading database ... 39388 files and directories currently installed.)",
            "Removing acpi (1.7-1) ...",
            "Removing apt-listchanges (2.85.13+nmu1) ...",
            "Purging configuration files for apt-listchanges (2.85.13+nmu1) ...",
            "Removing aptitude (0.6.11-1+b1) ...",
            "Purging configuration files for aptitude (0.6.11-1+b1) ...",
            "Removing aptitude-common (0.6.11-1) ...",
            "Removing aptitude-doc-en (0.6.11-1) ...",
            "Removing arping (2.14-1) ...",
            "Purging configuration files for arping (2.14-1) ...",
            "Removing at (3.1.16-1) ...",
            "[....] Stopping deferred execution scheduler: atd\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for at (3.1.16-1) ...",
            "Removing bash-completion (1:2.1-4) ...",
            "Purging configuration files for bash-completion (1:2.1-4) ...",
            "Removing dnsutils (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing host (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing bind9-host (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing console-setup (1.123) ...",
            "Purging configuration files for console-setup (1.123) ...",
            "Removing console-setup-linux (1.123) ...",
            "Purging configuration files for console-setup-linux (1.123) ...",
            "Removing dbus (1.8.22-0+deb8u1) ...",
            "[....] Stopping system message bus: dbus\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for dbus (1.8.22-0+deb8u1) ...",
            "Removing debconf-i18n (1.5.56+deb8u1) ...",
            "Removing debian-faq (5.0.3) ...",
            "Removing ibritish (3.3.02-6) ...",
            "Purging configuration files for ibritish (3.3.02-6) ...",
            "Removing iamerican (3.3.02-6) ...",
            "Purging configuration files for iamerican (3.3.02-6) ...",
            "dpkg: warning: while removing iamerican, directory '/var/lib/ispell' not empty so not removed",
            "Removing ienglish-common (3.3.02-6) ...",
            "Removing ispell (3.3.02-6) ...",
            "Removing dictionaries-common (1.23.17) ...",
            "Removing 'diversion of /usr/share/dict/words to /usr/share/dict/words.pre-dictionaries-common by dictionaries-common'",
            "Purging configuration files for dictionaries-common (1.23.17) ...",
            "Removing discover (2.1.2-7) ...",
            "Purging configuration files for discover (2.1.2-7) ...",
            "Removing libdiscover2 (2.1.2-7) ...",
            "Purging configuration files for libdiscover2 (2.1.2-7) ...",
            "Removing discover-data (2.2013.01.11) ...",
            "Removing laptop-detect (0.13.7) ...",
            "Removing dmidecode (2.12-3) ...",
            "Removing doc-debian (6.2) ...",
            "Removing reportbug (6.6.3+deb8u2) ...",
            "Purging configuration files for reportbug (6.6.3+deb8u2) ...",
            "Removing python-reportbug (6.6.3+deb8u2) ...",
            "Removing python-debianbts (1.12) ...",
            "Removing python-soappy (0.12.22-1) ...",
            "Removing python-wstools (0.4.3-2) ...",
            "Removing python-docutils (0.12+dfsg-1) ...",
            "Removing docutils-common (0.12+dfsg-1) ...",
            "Purging configuration files for docutils-common (0.12+dfsg-1) ...",
            "Removing docutils-doc (0.12+dfsg-1) ...",
            "Removing eject (2.1.5+deb1+cvs20081104-13.1+deb8u1) ...",
            "Removing emacsen-common (2.0.8) ...",
            "Purging configuration files for emacsen-common (2.0.8) ...",
            "Removing ethtool (1:3.16-1) ...",
            "Purging configuration files for ethtool (1:3.16-1) ...",
            "Removing fail2ban (0.8.13-1) ...",
            "[....] Stopping authentication failure monitor: fail2ban\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for fail2ban (0.8.13-1) ...",
            "dpkg: warning: while removing fail2ban, directory '/etc/fail2ban' not empty so not removed",
            "Removing firmware-linux-free (3.3) ...",
            "Processing triggers for man-db (2.7.0.2-5) ...",
            "Processing triggers for libc-bin (2.19-18+deb8u10) ...",
            "Processing triggers for mime-support (3.58) ...",
            "Processing triggers for python-support (1.0.15) ...",
            "Processing triggers for shared-mime-info (1.3-1) ...",
            "Selecting previously unselected package pinentry-curses.",
            "(Reading database ... ",
            "(Reading database ... 5%",
            "(Reading database ... 10%",
            "(Reading database ... 15%",
            "(Reading database ... 20%",
            "(Reading database ... 25%",
            "(Reading database ... 30%",
            "(Reading database ... 35%",
            "(Reading database ... 40%",
            "(Reading database ... 45%",
            "(Reading database ... 50%",
            "(Reading database ... 55%",
            "(Reading database ... 60%",
            "(Reading database ... 65%",
            "(Reading database ... 70%",
            "(Reading database ... 75%",
            "(Reading database ... 80%",
            "(Reading database ... 85%",
            "(Reading database ... 90%",
            "(Reading database ... 95%",
            "(Reading database ... 100%",
            "(Reading database ... 36774 files and directories currently installed.)",
            "Preparing to unpack .../pinentry-curses_0.8.3-2_amd64.deb ...",
            "Unpacking pinentry-curses (0.8.3-2) ...",
            "Processing triggers for man-db (2.7.0.2-5) ...",
            "(Reading database ... ",
            "(Reading database ... 5%",
            "(Reading database ... 10%",
            "(Reading database ... 15%",
            "(Reading database ... 20%",
            "(Reading database ... 25%",
            "(Reading database ... 30%",
            "(Reading database ... 35%",
            "(Reading database ... 40%",
            "(Reading database ... 45%",
            "(Reading database ... 50%",
            "(Reading database ... 55%",
            "(Reading database ... 60%",
            "(Reading database ... 65%",
            "(Reading database ... 70%",
            "(Reading database ... 75%",
            "(Reading database ... 80%",
            "(Reading database ... 85%",
            "(Reading database ... 90%",
            "(Reading database ... 95%",
            "(Reading database ... 100%",
            "(Reading database ... 36783 files and directories currently installed.)",
            "Removing libgtk2.0-bin (2.24.25-3+deb8u2) ...",
            "Removing ftp (0.17-31) ...",
            "Removing gcc-4.8-base:amd64 (4.8.4-1) ...",
            "Removing geoip-database (20150317-1) ...",
            "Removing hicolor-icon-theme (0.13-1) ...",
            "Removing info (5.2.0.dfsg.1-6) ...",
            "Purging configuration files for info (5.2.0.dfsg.1-6) ...",
            "Removing nano (2.2.6-3) ...",
            "update-alternatives: using /usr/bin/vim.basic to provide /usr/bin/editor (editor) in auto mode",
            "Purging configuration files for nano (2.2.6-3) ...",
            "Removing install-info (5.2.0.dfsg.1-6) ...",
            "Removing installation-report (2.58) ...",
            "Purging configuration files for installation-report (2.58) ...",
            "Removing irqbalance (1.0.6-3+deb8u1) ...",
            "[....] Stopping SMP IRQ Balancer: irqbalance\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for irqbalance (1.0.6-3+deb8u1) ...",
            "Removing isc-dhcp-client (4.3.1-6+deb8u3) ...",
            "Purging configuration files for isc-dhcp-client (4.3.1-6+deb8u3) ...",
            "Removing isc-dhcp-common (4.3.1-6+deb8u3) ...",
            "Removing iso-codes (3.57-1) ...",
            "Removing keyboard-configuration (1.123) ...",
            "Purging configuration files for keyboard-configuration (1.123) ...",
            "Removing krb5-locales (1.12.1+dfsg-19+deb8u4) ...",
            "Removing libsoftware-license-perl (0.103010-3) ...",
            "Removing libdata-section-perl (0.200006-1) ...",
            "Removing libmro-compat-perl (0.12-1) ...",
            "Removing libclass-c3-perl (0.26-1) ...",
            "Removing libalgorithm-c3-perl (0.09-1) ...",
            "Removing libauthen-sasl-perl (2.1600-1) ...",
            "Removing libbind9-90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libbind9-90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libcap-ng0:amd64 (0.7.4-2) ...",
            "Purging configuration files for libcap-ng0:amd64 (0.7.4-2) ...",
            "Removing libcgi-fast-perl (1:2.04-1) ...",
            "Removing libcgi-pm-perl (4.09-1) ...",
            "Removing libparse-debianchangelog-perl (1.2.0-1.1) ...",
            "Removing libclass-accessor-perl (0.34-1) ...",
            "Removing libclass-c3-xs-perl (0.13-2+b1) ...",
            "Removing libclass-isa-perl (0.36-5) ...",
            "Removing libcwidget3:amd64 (0.5.17-2) ...",
            "Purging configuration files for libcwidget3:amd64 (0.5.17-2) ...",
            "Removing libsub-exporter-perl (0.986-1) ...",
            "Removing libdata-optlist-perl (0.109-1) ...",
            "Removing libirs-export91 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libirs-export91 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libdns-export100 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libdns-export100 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libisccfg90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libisccfg90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libdns100 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libdns100 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing open-vm-tools (2:9.4.6-1770165-8) ...",
            "[....] Stopping open-vm guest daemon: vmtoolsd\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for open-vm-tools (2:9.4.6-1770165-8) ...",
            "dpkg: warning: while removing open-vm-tools, directory '/etc/vmware-tools' not empty so not removed",
            "Removing libdumbnet1 (1.12-6) ...",
            "Purging configuration files for libdumbnet1 (1.12-6) ...",
            "Removing libxml-sax-expat-perl (0.40-2) ...",
            "update-perl-sax-parsers: Unregistering Perl SAX parser XML::SAX::Expat with priority 50...",
            "update-perl-sax-parsers: Updating overall Perl SAX parser modules info file...",
            "Replacing config file /etc/perl/XML/SAX/ParserDetails.ini with new version",
            "Removing libxml-parser-perl (2.41-3) ...",
            "Removing nfs-common (1:1.2.8-9) ...",
            "[....] Stopping NFS common utilities: idmapd statd\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for nfs-common (1:1.2.8-9) ...",
            "dpkg-statoverride: warning: no override present",
            "Removing libevent-2.0-5:amd64 (2.0.21-stable-2+deb8u1) ...",
            "Purging configuration files for libevent-2.0-5:amd64 (2.0.21-stable-2+deb8u1) ...",
            "Removing libfcgi-perl (0.77-1+deb8u1) ...",
            "Removing libhtml-format-perl (2.11-1) ...",
            "Removing libfont-afm-perl (1.20-1) ...",
            "Removing w3m (0.5.3-19+deb8u2) ...",
            "Purging configuration files for w3m (0.5.3-19+deb8u2) ...",
            "Removing libgc1c2:amd64 (1:7.2d-6.4) ...",
            "Purging configuration files for libgc1c2:amd64 (1:7.2d-6.4) ...",
            "Removing libgeoip1:amd64 (1.6.2-4) ...",
            "Purging configuration files for libgeoip1:amd64 (1.6.2-4) ...",
            "Removing libglib2.0-data (2.42.1-1) ...",
            "Removing mutt (1.5.23-3+deb8u1) ...",
            "Purging configuration files for mutt (1.5.23-3+deb8u1) ...",
            "Removing libgpgme11:amd64 (1.5.1-6) ...",
            "Purging configuration files for libgpgme11:amd64 (1.5.1-6) ...",
            "Removing vim (2:7.4.488-7+deb8u3) ...",
            "update-alternatives: using /usr/bin/vim.tiny to provide /usr/bin/vi (vi) in auto mode",
            "update-alternatives: using /usr/bin/vim.tiny to provide /usr/bin/view (view) in auto mode",
            "update-alternatives: using /usr/bin/vim.tiny to provide /usr/bin/ex (ex) in auto mode",
            "update-alternatives: using /usr/bin/vim.tiny to provide /usr/bin/editor (editor) in auto mode",
            "update-alternatives: using /usr/bin/vim.tiny to provide /usr/bin/rview (rview) in auto mode",
            "Removing libgpm2:amd64 (1.20.4-6.1+b2) ...",
            "Purging configuration files for libgpm2:amd64 (1.20.4-6.1+b2) ...",
            "Removing libhtml-form-perl (6.03-1) ...",
            "Removing libhttp-daemon-perl (6.01-1) ...",
            "Removing texinfo (5.2.0.dfsg.1-6) ...",
            "Purging configuration files for texinfo (5.2.0.dfsg.1-6) ...",
            "Removing libintl-perl (1.23-1+deb8u1) ...",
            "Removing libio-socket-ip-perl (0.32-1) ...",
            "Removing libmailtools-perl (2.13-1) ...",
            "Removing libnet-smtp-ssl-perl (1.01-3) ...",
            "Removing libio-string-perl (1.08-3) ...",
            "Removing libisccfg-export90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libisccfg-export90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libisc-export95 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libisc-export95 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libisccc90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libisccc90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libisc95 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for libisc95 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing python-pil:amd64 (2.6.1-2+deb8u3) ...",
            "Removing liblcms2-2:amd64 (2.6-3+deb8u2) ...",
            "Purging configuration files for liblcms2-2:amd64 (2.6-3+deb8u2) ...",
            "Removing liblockfile1:amd64 (1.09-6) ...",
            "Purging configuration files for liblockfile1:amd64 (1.09-6) ...",
            "Removing liblwres90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Purging configuration files for liblwres90 (1:9.9.5.dfsg-9+deb8u16) ...",
            "Removing libnet1:amd64 (1.1.6+dfsg-3) ...",
            "Purging configuration files for libnet1:amd64 (1.1.6+dfsg-3) ...",
            "Removing libnfsidmap2:amd64 (0.25-5) ...",
            "Purging configuration files for libnfsidmap2:amd64 (0.25-5) ...",
            "Removing libnuma1:amd64 (2.0.10-1) ...",
            "Purging configuration files for libnuma1:amd64 (2.0.10-1) ...",
            "Removing libpaper-utils (1.1.24+nmu4) ...",
            "Removing libpaper1:amd64 (1.1.24+nmu4) ...",
            "Purging configuration files for libpaper1:amd64 (1.1.24+nmu4) ...",
            "Removing libparams-util-perl (1.07-2+b1) ...",
            "Removing parted (3.2-7) ...",
            "Removing libparted2:amd64 (3.2-7) ...",
            "Purging configuration files for libparted2:amd64 (3.2-7) ...",
            "Removing libpcap0.8:amd64 (1.6.2-2) ...",
            "Purging configuration files for libpcap0.8:amd64 (1.6.2-2) ...",
            "Removing pciutils (1:3.2.1-3) ...",
            "Purging configuration files for pciutils (1:3.2.1-3) ...",
            "Removing libpci3:amd64 (1:3.2.1-3) ...",
            "Purging configuration files for libpci3:amd64 (1:3.2.1-3) ...",
            "Removing sysstat (11.0.1-1) ...",
            "Purging configuration files for sysstat (11.0.1-1) ...",
            "Removing libsensors4:amd64 (1:3.3.5-2) ...",
            "Purging configuration files for libsensors4:amd64 (1:3.3.5-2) ...",
            "Removing m4 (1.4.17-4) ...",
            "Removing libsigsegv2:amd64 (2.10-4+b1) ...",
            "Purging configuration files for libsigsegv2:amd64 (2.10-4+b1) ...",
            "Removing libsub-install-perl (0.928-1) ...",
            "Removing libsub-name-perl (0.12-1) ...",
            "Removing libtext-template-perl (1.46-1) ...",
            "Removing libtext-unidecode-perl (1.22-1) ...",
            "Removing rpcbind (0.2.1-6+deb8u2) ...",
            "[....] Stopping rpcbind daemon...\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
            "Purging configuration files for rpcbind (0.2.1-6+deb8u2) ...",
            "Removing libtirpc1:amd64 (0.2.5-1+deb8u2) ...",
            "Purging configuration files for libtirpc1:amd64 (0.2.5-1+deb8u2) ...",
            "Removing libtokyocabinet9:amd64 (1.4.48-3) ...",
            "Purging configuration files for libtokyocabinet9:amd64 (1.4.48-3) ...",
            "Removing libuuid-perl (0.05-1+b1) ...",
            "Removing libwebpmux1:amd64 (0.4.1-1.2+b2) ...",
            "Purging configuration files for libwebpmux1:amd64 (0.4.1-1.2+b2) ...",
            "Removing libwebpdemux1:amd64 (0.4.1-1.2+b2) ...",
            "Purging configuration files for libwebpdemux1:amd64 (0.4.1-1.2+b2) ...",
            "Removing libwebp5:amd64 (0.4.1-1.2+b2) ...",
            "Purging configuration files for libwebp5:amd64 (0.4.1-1.2+b2) ...",
            "Removing xauth (1:1.0.9-1) ...",
            "Removing libxapian22 (1.2.19-1+deb8u1) ...",
            "Purging configuration files for libxapian22 (1.2.19-1+deb8u1) ...",
            "Removing libxml-libxml-perl (2.0116+dfsg-1+deb8u2) ...",
            "update-perl-sax-parsers: Unregistering Perl SAX parser XML::LibXML::SAX::Parser with priority 50...",
            "update-perl-sax-parsers: Unregistering Perl SAX parser XML::LibXML::SAX with priority 50...",
            "update-perl-sax-parsers: Updating overall Perl SAX parser modules info file...",
            "Replacing config file /etc/perl/XML/SAX/ParserDetails.ini with new version",
            "Removing libxml-sax-perl (0.99+dfsg-2) ...",
            "update-perl-sax-parsers: Unregistering Perl SAX parser XML::SAX::PurePerl with priority 50...",
            "update-perl-sax-parsers: Updating overall Perl SAX parser modules info file...",
            "Purging configuration files for libxml-sax-perl (0.99+dfsg-2) ...",
            "Removing libxml-namespacesupport-perl (1.11-1) ...",
            "Removing libxml-sax-base-perl (1.07-1) ...",
            "Removing libxmuu1:amd64 (2:1.1.2-1) ...",
            "Purging configuration files for libxmuu1:amd64 (2:1.1.2-1) ...",
            "Removing linux-image-3.16.0-4-amd64 (3.16.51-3) ...",
            "/etc/kernel/postrm.d/initramfs-tools:",
            "update-initramfs: Deleting /boot/initrd.img-3.16.0-4-amd64",
            "/etc/kernel/postrm.d/zz-update-grub:",
            "Generating grub configuration file ...",
            "Found linux image: /boot/vmlinuz-3.16.0-7-amd64",
            "Found initrd image: /boot/initrd.img-3.16.0-7-amd64",
            "Found linux image: /boot/vmlinuz-3.16.0-5-amd64",
            "Found initrd image: /boot/initrd.img-3.16.0-5-amd64",
            "done",
            "Purging configuration files for linux-image-3.16.0-4-amd64 (3.16.51-3) ...",
            "Removing linux-image-amd64 (3.16+63+deb8u3) ...",
            "Removing lrzsz (0.12.21-7) ...",
            "Removing lsb-release (4.1+Debian13+nmu1) ...",
            "Purging configuration files for lsb-release (4.1+Debian13+nmu1) ...",
            "Removing man-db (2.7.0.2-5) ...",
            "Purging configuration files for man-db (2.7.0.2-5) ...",
            "  Removing catpages as well as /var/cache/man hierarchy.",
            "Removing manpages (3.74-1) ...",
            "Removing os-prober (1.65+deb8u1) ...",
            "Removing procmail (3.22-24+deb8u1) ...",
            "Removing python-ndg-httpsclient (0.3.2-1) ...",
            "Removing python-openssl (0.14-1) ...",
            "Removing python-cryptography (0.6.1-1+deb8u1) ...",
            "Removing python-cffi (0.8.6-1) ...",
            "Removing python-requests (2.4.3-6) ...",
            "Removing python-debian (0.1.27) ...",
            "Removing python-chardet (2.3.0-1) ...",
            "Removing python-defusedxml (0.4.1-2) ...",
            "Removing python-pkg-resources (5.5.1-1) ...",
            "Removing python-pycparser (2.10+dfsg-3) ...",
            "Removing python-ply (3.4-5) ...",
            "Removing python-pyasn1 (0.1.7-1) ...",
            "Removing python-pygments (2.0.1+dfsg-1.1+deb8u1) ...",
            "Purging configuration files for python-pygments (2.0.1+dfsg-1.1+deb8u1) ...",
            "Removing python-pyinotify (0.9.4-1) ...",
            "Removing python-roman (2.0.0-1) ...",
            "Removing python-urllib3 (1.9.1-3) ...",
            "Removing python-six (1.8.0-1) ...",
            "Removing rename (0.20-3) ...",
            "update-alternatives: using /usr/bin/prename to provide /usr/bin/rename (rename) in auto mode",
            "Removing xml-core (0.13+nmu2) ...",
            "Purging configuration files for xml-core (0.13+nmu2) ...",
            "dpkg: warning: while removing xml-core, directory '/etc/sgml' not empty so not removed",
            "Removing sgml-base (1.26+nmu4) ...",
            "Purging configuration files for sgml-base (1.26+nmu4) ...",
            "Removing task-english (3.31+deb8u1) ...",
            "Removing task-ssh-server (3.31+deb8u1) ...",
            "Removing tcpd (7.6.q-25) ...",
            "Removing util-linux-locales (2.25.2-6) ...",
            "Removing vim-runtime (2:7.4.488-7+deb8u3) ...",
            "Removing 'diversion of /usr/share/vim/vim74/doc/help.txt to /usr/share/vim/vim74/doc/help.txt.vim-tiny by vim-runtime'",
            "Removing 'diversion of /usr/share/vim/vim74/doc/tags to /usr/share/vim/vim74/doc/tags.vim-tiny by vim-runtime'",
            "Purging configuration files for vim-runtime (2:7.4.488-7+deb8u3) ...",
            "Removing wamerican (7.1-1) ...",
            "Purging configuration files for wamerican (7.1-1) ...",
            "Removing wget (1.16-1+deb8u5) ...",
            "Purging configuration files for wget (1.16-1+deb8u5) ...",
            "Removing xdg-user-dirs (0.15-2) ...",
            "Purging configuration files for xdg-user-dirs (0.15-2) ...",
            "Removing xkb-data (2.12-1) ...",
            "Removing zerofree (1.0.3-1) ...",
            "Removing liblwp-protocol-https-perl (6.06-2) ...",
            "Removing libwww-perl (6.08-1) ...",
            "Removing libhttp-negotiate-perl (6.00-2) ...",
            "Removing libfile-listing-perl (6.04-1) ...",
            "Removing libhtml-tree-perl (5.03-1) ...",
            "Removing libhtml-parser-perl (3.71-1+b3) ...",
            "Removing libhtml-tagset-perl (3.20-2) ...",
            "Removing libhttp-cookies-perl (6.01-1) ...",
            "Removing libnet-http-perl (6.07-1) ...",
            "Removing libio-socket-ssl-perl (2.002-2+deb8u3) ...",
            "Removing libnet-ssleay-perl (1.65-1+deb8u1) ...",
            "Removing libwww-robotrules-perl (6.01-1) ...",
            "Removing tasksel-data (3.31+deb8u1) ...",
            "Removing libhttp-message-perl (6.06-1) ...",
            "Removing libencode-locale-perl (1.03-1) ...",
            "Removing libhttp-date-perl (6.02-1) ...",
            "Removing libio-html-perl (1.001-1) ...",
            "Removing liblwp-mediatypes-perl (6.02-1) ...",
            "Removing libtimedate-perl (2.3000-2) ...",
            "Removing liburi-perl (1.64-1) ...",
            "Removing tasksel (3.31+deb8u1) ...",
            "Purging configuration files for tasksel (3.31+deb8u1) ...",
            "dpkg: libgtk2.0-0:amd64: dependency problems, but removing anyway as you requested:",
            " pinentry-gtk2 depends on libgtk2.0-0 (>= 2.10.0).",
            "",
            "Removing libgtk2.0-0:amd64 (2.24.25-3+deb8u2) ...",
            "Purging configuration files for libgtk2.0-0:amd64 (2.24.25-3+deb8u2) ...",
            "Removing libpangocairo-1.0-0:amd64 (1.36.8-3) ...",
            "Purging configuration files for libpangocairo-1.0-0:amd64 (1.36.8-3) ...",
            "Removing libpangoft2-1.0-0:amd64 (1.36.8-3) ...",
            "Purging configuration files for libpangoft2-1.0-0:amd64 (1.36.8-3) ...",
            "dpkg: libpango-1.0-0:amd64: dependency problems, but removing anyway as you requested:",
            " pinentry-gtk2 depends on libpango-1.0-0 (>= 1.14.0); however:",
            "  Package libpango-1.0-0:amd64 is to be removed.",
            "",
            "Removing libpango-1.0-0:amd64 (1.36.8-3) ...",
            "Purging configuration files for libpango-1.0-0:amd64 (1.36.8-3) ...",
            "Removing fontconfig (2.11.0-6.3+deb8u1) ...",
            "Purging configuration files for fontconfig (2.11.0-6.3+deb8u1) ...",
            "Removing libcairo2:amd64 (1.14.0-2.1+deb8u2) ...",
            "Purging configuration files for libcairo2:amd64 (1.14.0-2.1+deb8u2) ...",
            "Removing libfontconfig1:amd64 (2.11.0-6.3+deb8u1) ...",
            "Purging configuration files for libfontconfig1:amd64 (2.11.0-6.3+deb8u1) ...",
            "Removing fontconfig-config (2.11.0-6.3+deb8u1) ...",
            "Purging configuration files for fontconfig-config (2.11.0-6.3+deb8u1) ...",
            "Removing fonts-dejavu-core (2.34-1) ...",
            "Purging configuration files for fonts-dejavu-core (2.34-1) ...",
            "Removing libatk1.0-0:amd64 (2.14.0-1) ...",
            "Purging configuration files for libatk1.0-0:amd64 (2.14.0-1) ...",
            "Removing libatk1.0-data (2.14.0-1) ...",
            "Removing libcups2:amd64 (1.7.5-11+deb8u4) ...",
            "Purging configuration files for libcups2:amd64 (1.7.5-11+deb8u4) ...",
            "Removing libavahi-client3:amd64 (0.6.31-5) ...",
            "Purging configuration files for libavahi-client3:amd64 (0.6.31-5) ...",
            "Removing libavahi-common3:amd64 (0.6.31-5) ...",
            "Purging configuration files for libavahi-common3:amd64 (0.6.31-5) ...",
            "Removing libavahi-common-data:amd64 (0.6.31-5) ...",
            "Removing libthai0:amd64 (0.1.21-1) ...",
            "Purging configuration files for libthai0:amd64 (0.1.21-1) ...",
            "Removing libdatrie1:amd64 (0.2.8-1) ...",
            "Purging configuration files for libdatrie1:amd64 (0.2.8-1) ...",
            "Removing libdbus-1-3:amd64 (1.8.22-0+deb8u1) ...",
            "Purging configuration files for libdbus-1-3:amd64 (1.8.22-0+deb8u1) ...",
            "Removing libgdk-pixbuf2.0-0:amd64 (2.31.1-2+deb8u7) ...",
            "Purging configuration files for libgdk-pixbuf2.0-0:amd64 (2.31.1-2+deb8u7) ...",
            "Removing libgdk-pixbuf2.0-common (2.31.1-2+deb8u7) ...",
            "Removing shared-mime-info (1.3-1) ...",
            "Purging configuration files for shared-mime-info (1.3-1) ...",
            "Removing libharfbuzz0b:amd64 (0.9.35-2) ...",
            "Purging configuration files for libharfbuzz0b:amd64 (0.9.35-2) ...",
            "dpkg: libglib2.0-0:amd64: dependency problems, but removing anyway as you requested:",
            " pinentry-gtk2 depends on libglib2.0-0 (>= 2.16.0).",
            "",
            "Removing libglib2.0-0:amd64 (2.42.1-1+b1) ...",
            "Purging configuration files for libglib2.0-0:amd64 (2.42.1-1+b1) ...",
            "Removing libgraphite2-3:amd64 (1.3.10-1~deb8u1) ...",
            "Purging configuration files for libgraphite2-3:amd64 (1.3.10-1~deb8u1) ...",
            "Removing libgtk2.0-common (2.24.25-3+deb8u2) ...",
            "Purging configuration files for libgtk2.0-common (2.24.25-3+deb8u2) ...",
            "Removing libjasper1:amd64 (1.900.1-debian1-2.4+deb8u5) ...",
            "Purging configuration files for libjasper1:amd64 (1.900.1-debian1-2.4+deb8u5) ...",
            "Removing libtiff5:amd64 (4.0.3-12.3+deb8u7) ...",
            "Purging configuration files for libtiff5:amd64 (4.0.3-12.3+deb8u7) ...",
            "Removing libjbig0:amd64 (2.1-3.1) ...",
            "Purging configuration files for libjbig0:amd64 (2.1-3.1) ...",
            "Removing libjpeg62-turbo:amd64 (1:1.3.1-12) ...",
            "Purging configuration files for libjpeg62-turbo:amd64 (1:1.3.1-12) ...",
            "Removing libpixman-1-0:amd64 (0.32.6-3+deb8u1) ...",
            "Purging configuration files for libpixman-1-0:amd64 (0.32.6-3+deb8u1) ...",
            "Removing libthai-data (0.1.21-1) ...",
            "Removing libxcursor1:amd64 (1:1.1.14-1+deb8u2) ...",
            "Purging configuration files for libxcursor1:amd64 (1:1.1.14-1+deb8u2) ...",
            "dpkg: libx11-6:amd64: dependency problems, but removing anyway as you requested:",
            " libxrandr2:amd64 depends on libx11-6 (>= 2:1.6.0).",
            " libxrender1:amd64 depends on libx11-6 (>= 2:1.6.0).",
            " libxcomposite1:amd64 depends on libx11-6 (>= 2:1.4.99.1).",
            " libxfixes3:amd64 depends on libx11-6 (>= 2:1.6.0).",
            " libxext6:amd64 depends on libx11-6 (>= 2:1.6.0).",
            " libxdamage1:amd64 depends on libx11-6 (>= 2:1.4.99.1).",
            " libxinerama1:amd64 depends on libx11-6 (>= 2:1.6.0).",
            " libxi6:amd64 depends on libx11-6 (>= 2:1.6.0).",
            "",
            "Removing libx11-6:amd64 (2:1.6.2-3+deb8u2) ...",
            "Purging configuration files for libx11-6:amd64 (2:1.6.2-3+deb8u2) ...",
            "Removing libx11-data (2:1.6.2-3+deb8u2) ...",
            "Removing libxcb-shm0:amd64 (1.10-3+b1) ...",
            "Purging configuration files for libxcb-shm0:amd64 (1.10-3+b1) ...",
            "dpkg: libxcb1:amd64: dependency problems, but removing anyway as you requested:",
            " libxcb-render0:amd64 depends on libxcb1 (>= 1.8).",
            "",
            "Removing libxcb1:amd64 (1.10-3+b1) ...",
            "Purging configuration files for libxcb1:amd64 (1.10-3+b1) ...",
            "Removing libxau6:amd64 (1:1.0.8-1) ...",
            "Purging configuration files for libxau6:amd64 (1:1.0.8-1) ...",
            "Removing libxcb-render0:amd64 (1.10-3+b1) ...",
            "Purging configuration files for libxcb-render0:amd64 (1.10-3+b1) ...",
            "Removing libxcomposite1:amd64 (1:0.4.4-1) ...",
            "Purging configuration files for libxcomposite1:amd64 (1:0.4.4-1) ...",
            "Removing libxdamage1:amd64 (1:1.1.4-2+b1) ...",
            "Purging configuration files for libxdamage1:amd64 (1:1.1.4-2+b1) ...",
            "Removing libxdmcp6:amd64 (1:1.1.1-1+b1) ...",
            "Purging configuration files for libxdmcp6:amd64 (1:1.1.1-1+b1) ...",
            "Removing libxrandr2:amd64 (2:1.4.2-1+deb8u1) ...",
            "Purging configuration files for libxrandr2:amd64 (2:1.4.2-1+deb8u1) ...",
            "Removing libxinerama1:amd64 (2:1.1.3-1+b1) ...",
            "Purging configuration files for libxinerama1:amd64 (2:1.1.3-1+b1) ...",
            "dpkg: libxext6:amd64: dependency problems, but removing anyway as you requested:",
            " libxi6:amd64 depends on libxext6; however:",
            "  Package libxext6:amd64 is to be removed.",
            "",
            "Removing libxext6:amd64 (2:1.3.3-1) ...",
            "Purging configuration files for libxext6:amd64 (2:1.3.3-1) ...",
            "Removing libxfixes3:amd64 (1:5.0.1-2+deb8u1) ...",
            "Purging configuration files for libxfixes3:amd64 (1:5.0.1-2+deb8u1) ...",
            "Removing libxi6:amd64 (2:1.7.4-1+deb8u1) ...",
            "Purging configuration files for libxi6:amd64 (2:1.7.4-1+deb8u1) ...",
            "Removing libxml2:amd64 (2.9.1+dfsg1-5+deb8u7) ...",
            "Purging configuration files for libxml2:amd64 (2.9.1+dfsg1-5+deb8u7) ...",
            "Removing libxrender1:amd64 (1:0.9.8-1+b1) ...",
            "Purging configuration files for libxrender1:amd64 (1:0.9.8-1+b1) ...",
            "dpkg: pinentry-gtk2: dependency problems, but removing anyway as you requested:",
            " gnupg-agent depends on pinentry-gtk2 | pinentry-curses | pinentry; however:",
            "  Package pinentry-gtk2 is to be removed.",
            "  Package pinentry-curses is not configured yet.",
            "  Package pinentry is not installed.",
            "  Package pinentry-curses which provides pinentry is not configured yet.",
            "  Package pinentry-gtk2 which provides pinentry is to be removed.",
            " gnupg-agent depends on pinentry-gtk2 | pinentry-curses | pinentry; however:",
            "  Package pinentry-gtk2 is to be removed.",
            "  Package pinentry-curses is not configured yet.",
            "  Package pinentry is not installed.",
            "  Package pinentry-curses which provides pinentry is not configured yet.",
            "  Package pinentry-gtk2 which provides pinentry is to be removed.",
            "",
            "Removing pinentry-gtk2 (0.8.3-2) ...",
            "Processing triggers for mime-support (3.58) ...",
            "Processing triggers for libc-bin (2.19-18+deb8u10) ...",
            "Processing triggers for python-support (1.0.15) ...",
            "Setting up pinentry-curses (0.8.3-2) ..."
        ]
    }
}

TASK [Add repos] ****************************************************************
changed: [lab] => (item=deb http://packages.dotdeb.org     jessie all  # nginx)
changed: [lab] => (item=deb https://packages.sury.org/php/ jessie main # php5.6)
changed: [lab] => (item=deb [arch=amd64] http://lon1.mirrors.digitalocean.com/mariadb/repo/10.1/debian jessie main)

TASK [Add repo keys] ************************************************************
changed: [lab] => (item=7E3F070089DF5277)
changed: [lab] => (item=AC0E47584A7A714D)
changed: [lab] => (item=CBCB082A1BB943DB)

TASK [Add EMP-packages] *********************************************************
changed: [lab]

TASK [Check if empty DBroot password works] *************************************
ok: [lab]

TASK [Pick random password for DBroot] ******************************************
ok: [lab]

TASK [Set DBroot password (if empty)] *******************************************
changed: [lab]

TASK [Save DBroot password to ~root/.my.cnf (if it was empty)] ******************
changed: [lab]

RUNNING HANDLER [restart sshd] **************************************************
ok: [lab]

PLAY RECAP **********************************************************************
lab                        : ok=43   changed=24   unreachable=0    failed=0
provisioner                : ok=4    changed=1    unreachable=0    failed=0


real	8m24,380s
user	0m54,982s
sys	0m16,579s
```
