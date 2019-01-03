```
$ time ansible-playbook launch-DO.yml

PLAY [provisioner] **************************************************************

TASK [Gather facts about SSH key (fingerprint look-up)] *************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner]

TASK [digital_ocean_sshkey_facts] ***********************************************
ok: [provisioner]

TASK [set_fact] *****************************************************************
ok: [provisioner] => (item={u'public_key': u'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQCyQ5wJKkduGWq7Q1Ar46F+gc61pQiuy6YXKI623/lnz1xVV8y58NSGI5AYs1e5thygB72ZWgZO1w7tXVxyJ3jGS1c1vHAG8myqcu5ZZYdX6rzZ7+HXpcsLTDuqPs8VUhTzDf8kUGwaiMEsG0sHsy98jupxF1iTojBjEmA7rixnVM+EA94Z7KrHmAS9yOYa9P6P0KrnwK4tAz3GtrxyEOGGs9kXQ9B88kQHvQvTTMVG26zbln0Yt3jSqvBIo4nD6gWiKtCsN0Y/2bSrCdy33C/HKr4uHizgHumruDsbECYtga/k7VOQrr3+uc5t7MpXLUxNdGBNN4hnBSrt/DVSSwm/ mz0@nb13', u'id': 23550519, u'name': u'ansible', u'fingerprint': u'04:39:43:86:22:6b:e6:fa:c0:22:38:2d:b2:91:13:9c'})

TASK [Find or create Droplet, then register in-memory] **************************
changed: [provisioner]

TASK [debug] ********************************************************************
ok: [provisioner] => {
    "msg": "Droplet de.x302.net 104.248.137.215 2a03:b0c0:3:e0::ee:5001"
}

TASK [Add droplet to in-memory (dynamic) inventory] *****************************
ok: [provisioner]

PLAY [dohosts] ******************************************************************

TASK [Check port 22 is open] ****************************************************
ok: [do1 -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [do1]

TASK [Confirm host connection works] ********************************************
ok: [do1]

TASK [Replace systemd (stage 1 - install sysvinit-core etc.)] *******************
changed: [do1]

TASK [Reboot to replace systemd (ETA 23 seconds) if sysvinit just installed] ****
changed: [do1]

TASK [Replace systemd (stage 2 - uninstall systemd)] ****************************
changed: [do1]

TASK [fail] *********************************************************************
skipping: [do1]

TASK [Check port 22 is open] ****************************************************
ok: [do1 -> localhost]

TASK [Use ansible_port=22 if open] **********************************************
ok: [do1]

TASK [Check SSH port 2222, skip if 22 is OK] ************************************
skipping: [do1]

TASK [Set SSH port 2222 if check OK.] *******************************************
skipping: [do1]

TASK [Fail if neither SSH port is open] *****************************************
skipping: [do1]

TASK [Confirm host connection works] ********************************************
ok: [do1]

TASK [Setup SSH Port 2222 ; no UseDNS, AcceptEnv.] ******************************
changed: [do1] => (item={u'key': u'Port', u'value': 2222})
changed: [do1] => (item={u'key': u'UseDNS', u'value': u'no'})
changed: [do1] => (item={u'key': u'AcceptEnv', u'value': u''})

TASK [Restart sshd] *************************************************************
ok: [do1]

TASK [Write swap file] **********************************************************
changed: [do1]

TASK [Set swapfile permissions] *************************************************
changed: [do1]

TASK [Create swapfile] **********************************************************
changed: [do1]

TASK [Enable swapfile] **********************************************************
changed: [do1]

TASK [Add swapfile to /etc/fstab] ***********************************************
changed: [do1]

TASK [Configure vm.swappiness] **************************************************
changed: [do1]

TASK [Configure vm.vfs_cache_pressure] ******************************************
changed: [do1]

TASK [Install updates] **********************************************************
changed: [do1]

TASK [Install essential packages] ***********************************************
changed: [do1]

TASK [Ensure service is enabled and running] ************************************
ok: [do1] => (item=openntpd)

TASK [Ensure sudoers.d is enabled] **********************************************
ok: [do1]

TASK [Set up password-less sudo for admin users] ********************************
changed: [do1]

TASK [Strict SSH access] ********************************************************
ok: [do1] => (item={u'key': u'PubkeyAuthentication', u'value': u'yes'})
ok: [do1] => (item={u'key': u'ChallengeResponseAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'PermitRootLogin', u'value': u'without-password'})
ok: [do1] => (item={u'key': u'PasswordAuthentication', u'value': u'no'})
changed: [do1] => (item={u'key': u'MaxAuthTries', u'value': u'2'})
changed: [do1] => (item={u'key': u'LoginGraceTime', u'value': u'6'})
changed: [do1] => (item={u'key': u'MaxSessions', u'value': u'5'})
changed: [do1] => (item={u'key': u'MaxStartups', u'value': u'10:30:60'})

TASK [Create admin user] ********************************************************
changed: [do1]

TASK [Copy my ssh pubkey to $USERNAME on the new host] **************************
changed: [do1]

TASK [Purge unused packages] ****************************************************
changed: [do1]

TASK [debug] ********************************************************************
ok: [do1] => {
    "uninstall.stdout_lines": [
        "Reading package lists...",
        "Building dependency tree...",
        "Reading state information...",
        "The following extra packages will be installed:",
        "  pinentry-curses",
        "Suggested packages:",
        "  pinentry-doc",
        "The following packages will be REMOVED:",
        "  acpi* apt-listchanges* aptitude* aptitude-common* aptitude-doc-en* arping*",
        "  at* bash-completion* bind9-host* cloud-init* cloud-initramfs-growroot*",
        "  cloud-utils* console-setup* console-setup-linux* dbus* debconf-i18n*",
        "  debian-faq* dh-python* dictionaries-common* discover* discover-data*",
        "  distro-info* distro-info-data* dmidecode* dnsutils* doc-debian*",
        "  docutils-common* docutils-doc* eject* emacsen-common* euca2ools* exim4*",
        "  exim4-base* exim4-config* exim4-daemon-light* firmware-linux-free*",
        "  fontconfig* fontconfig-config* fonts-dejavu-core* ftp* gcc-4.8-base* gdisk*",
        "  geoip-database* hicolor-icon-theme* host* iamerican* ibritish*",
        "  ienglish-common* info* install-info* installation-report* irqbalance*",
        "  isc-dhcp-client* isc-dhcp-common* iso-codes* ispell* keyboard-configuration*",
        "  krb5-locales* laptop-detect* libalgorithm-c3-perl* libatk1.0-0*",
        "  libatk1.0-data* libauthen-sasl-perl* libavahi-client3* libavahi-common-data*",
        "  libavahi-common3* libbind9-90* libcairo2* libcap-ng0* libcgi-fast-perl*",
        "  libcgi-pm-perl* libclass-accessor-perl* libclass-c3-perl*",
        "  libclass-c3-xs-perl* libclass-isa-perl* libcups2* libcwidget3*",
        "  libdata-optlist-perl* libdata-section-perl* libdatrie1* libdbus-1-3*",
        "  libdiscover2* libdns-export100* libdns100* libencode-locale-perl*",
        "  libevent-2.0-5* libfcgi-perl* libfile-listing-perl* libfont-afm-perl*",
        "  libfontconfig1* libgc1c2* libgdk-pixbuf2.0-0* libgdk-pixbuf2.0-common*",
        "  libgeoip1* libglib2.0-0* libglib2.0-data* libgpgme11* libgpm2*",
        "  libgraphite2-3* libgtk2.0-0* libgtk2.0-bin* libgtk2.0-common* libharfbuzz0b*",
        "  libhtml-form-perl* libhtml-format-perl* libhtml-parser-perl*",
        "  libhtml-tagset-perl* libhtml-tree-perl* libhttp-cookies-perl*",
        "  libhttp-daemon-perl* libhttp-date-perl* libhttp-message-perl*",
        "  libhttp-negotiate-perl* libintl-perl* libio-html-perl* libio-socket-ip-perl*",
        "  libio-socket-ssl-perl* libio-string-perl* libirs-export91* libisc-export95*",
        "  libisc95* libisccc90* libisccfg-export90* libisccfg90* libjasper1* libjbig0*",
        "  libjpeg62-turbo* liblcms2-2* liblwp-mediatypes-perl*",
        "  liblwp-protocol-https-perl* liblwres90* libmailtools-perl* libmpdec2*",
        "  libmro-compat-perl* libnet-http-perl* libnet-smtp-ssl-perl*",
        "  libnet-ssleay-perl* libnet1* libnfsidmap2* libnuma1* libpango-1.0-0*",
        "  libpangocairo-1.0-0* libpangoft2-1.0-0* libpaper-utils* libpaper1*",
        "  libparams-util-perl* libparse-debianchangelog-perl* libparted2* libpcap0.8*",
        "  libpci3* libpixman-1-0* libpython3-stdlib* libpython3.4-minimal*",
        "  libpython3.4-stdlib* libsigsegv2* libsoftware-license-perl*",
        "  libsub-exporter-perl* libsub-install-perl* libsub-name-perl*",
        "  libtext-template-perl* libtext-unidecode-perl* libthai-data* libthai0*",
        "  libtiff5* libtimedate-perl* libtirpc1* libtokyocabinet9* liburi-perl*",
        "  libuuid-perl* libwebp5* libwebpdemux1* libwebpmux1* libwww-perl*",
        "  libwww-robotrules-perl* libx11-6* libx11-data* libxapian22* libxau6*",
        "  libxcb-render0* libxcb-shm0* libxcb1* libxcomposite1* libxcursor1*",
        "  libxdamage1* libxdmcp6* libxext6* libxfixes3* libxi6* libxinerama1*",
        "  libxml-libxml-perl* libxml-namespacesupport-perl* libxml-parser-perl*",
        "  libxml-sax-base-perl* libxml-sax-expat-perl* libxml-sax-perl* libxmuu1*",
        "  libxrandr2* libxrender1* libxslt1.1* libyaml-0-2*",
        "  linux-image-3.16.0-4-amd64* linux-image-amd64* lsb-release* m4* man-db*",
        "  manpages* mutt* nano* nfs-common* os-prober* parted* pciutils*",
        "  pinentry-gtk2* procmail* python-boto* python-cffi* python-chardet*",
        "  python-cheetah* python-configobj* python-crypto* python-cryptography*",
        "  python-debian* python-debianbts* python-defusedxml* python-distro-info*",
        "  python-docutils* python-ecdsa* python-json-pointer* python-jsonpatch*",
        "  python-lxml* python-ndg-httpsclient* python-oauth* python-openssl*",
        "  python-paramiko* python-pil* python-pkg-resources* python-ply*",
        "  python-prettytable* python-pyasn1* python-pycparser* python-pygments*",
        "  python-reportbug* python-requestbuilder* python-requests* python-roman*",
        "  python-serial* python-setuptools* python-six* python-soappy*",
        "  python-software-properties* python-urllib3* python-wstools* python-yaml*",
        "  python3* python3-apt* python3-minimal* python3.4* python3.4-minimal* rename*",
        "  reportbug* resolvconf* rpcbind* shared-mime-info* task-english*",
        "  task-ssh-server* tasksel* tasksel-data* tcpd* texinfo* unattended-upgrades*",
        "  util-linux-locales* vim* vim-runtime* w3m* wamerican* wget* xauth*",
        "  xdg-user-dirs* xkb-data*",
        "The following NEW packages will be installed:",
        "  pinentry-curses",
        "0 upgraded, 1 newly installed, 279 to remove and 0 not upgraded.",
        "Need to get 29.3 kB of archives.",
        "After this operation, 446 MB disk space will be freed.",
        "Get:1 http://mirrors.digitalocean.com/debian/ jessie/main pinentry-curses amd64 0.8.3-2 [29.3 kB]",
        "Fetched 29.3 kB in 0s (288 kB/s)",
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
        "(Reading database ... 42406 files and directories currently installed.)",
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
        "Removing cloud-init (0.7.6~bzr976-2) ...",
        "Removing 'diversion of /etc/init/ureadahead.conf to /etc/init/ureadahead.conf.disabled by cloud-init'",
        "Purging configuration files for cloud-init (0.7.6~bzr976-2) ...",
        "dpkg: warning: while removing cloud-init, directory '/usr/lib/python2.7/dist-packages/cloudinit/sources' not empty so not removed",
        "dpkg: warning: while removing cloud-init, directory '/usr/lib/python2.7/dist-packages/cloudinit/config' not empty so not removed",
        "dpkg: warning: while removing cloud-init, directory '/etc/cloud/cloud.cfg.d' not empty so not removed",
        "Removing cloud-initramfs-growroot (0.18.debian5) ...",
        "Purging configuration files for cloud-initramfs-growroot (0.18.debian5) ...",
        "Removing cloud-utils (0.26-2) ...",
        "Removing console-setup (1.123) ...",
        "Purging configuration files for console-setup (1.123) ...",
        "Removing console-setup-linux (1.123) ...",
        "Purging configuration files for console-setup-linux (1.123) ...",
        "Removing dbus (1.8.22-0+deb8u1) ...",
        "[....] Stopping system message bus: dbus\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
        "Purging configuration files for dbus (1.8.22-0+deb8u1) ...",
        "Removing debconf-i18n (1.5.56+deb8u1) ...",
        "Removing debian-faq (5.0.3) ...",
        "Removing python-software-properties (0.92.25debian1) ...",
        "Removing unattended-upgrades (0.83.3.2+deb8u1) ...",
        "Purging configuration files for unattended-upgrades (0.83.3.2+deb8u1) ...",
        "dpkg: warning: while removing unattended-upgrades, directory '/var/log/unattended-upgrades' not empty so not removed",
        "Removing python3-apt (0.9.3.12) ...",
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
        "Removing distro-info (0.14) ...",
        "Removing python-distro-info (0.14) ...",
        "Removing distro-info-data (0.26) ...",
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
        "Removing euca2ools (3.1.0-1) ...",
        "Removing exim4 (4.84.2-2+deb8u5) ...",
        "Purging configuration files for exim4 (4.84.2-2+deb8u5) ...",
        "Removing exim4-daemon-light (4.84.2-2+deb8u5) ...",
        "[....] Stopping MTA: exim4_listener\u001b[?25l\u001b7\u001b[1G[\u001b[32m ok \u001b[39;49m\u001b8\u001b[?12l\u001b[?25h.",
        "Purging configuration files for exim4-daemon-light (4.84.2-2+deb8u5) ...",
        "Removing exim4-base (4.84.2-2+deb8u5) ...",
        "Purging configuration files for exim4-base (4.84.2-2+deb8u5) ...",
        "Removing exim4-config (4.84.2-2+deb8u5) ...",
        "Purging configuration files for exim4-config (4.84.2-2+deb8u5) ...",
        "dpkg-statoverride: warning: no override present",
        "Removing firmware-linux-free (3.3) ...",
        "Removing dh-python (1.20141111-2) ...",
        "Removing python3 (3.4.2-2) ...",
        "Purging configuration files for python3 (3.4.2-2) ...",
        "Processing triggers for man-db (2.7.0.2-5) ...",
        "Processing triggers for initramfs-tools (0.120+deb8u3) ...",
        "update-initramfs: Generating /boot/initrd.img-3.16.0-7-amd64",
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
        "(Reading database ... 38601 files and directories currently installed.)",
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
        "(Reading database ... 38610 files and directories currently installed.)",
        "Removing libgtk2.0-bin (2.24.25-3+deb8u2) ...",
        "Removing ftp (0.17-31) ...",
        "Removing gcc-4.8-base:amd64 (4.8.4-1) ...",
        "Removing gdisk (0.8.10-2) ...",
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
        "Removing liblwres90 (1:9.9.5.dfsg-9+deb8u16) ...",
        "Purging configuration files for liblwres90 (1:9.9.5.dfsg-9+deb8u16) ...",
        "Removing python3.4 (3.4.2-1+deb8u1) ...",
        "Purging configuration files for python3.4 (3.4.2-1+deb8u1) ...",
        "Removing libpython3-stdlib:amd64 (3.4.2-2) ...",
        "Removing libpython3.4-stdlib:amd64 (3.4.2-1+deb8u1) ...",
        "dpkg-query: no packages found matching pkgname",
        "Removing libmpdec2:amd64 (2.4.1-1) ...",
        "Purging configuration files for libmpdec2:amd64 (2.4.1-1) ...",
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
        "Removing python3-minimal (3.4.2-2) ...",
        "Removing python3.4-minimal (3.4.2-1+deb8u1) ...",
        "Purging configuration files for python3.4-minimal (3.4.2-1+deb8u1) ...",
        "Removing libpython3.4-minimal:amd64 (3.4.2-1+deb8u1) ...",
        "dpkg-query: no packages found matching pkgname",
        "Purging configuration files for libpython3.4-minimal:amd64 (3.4.2-1+deb8u1) ...",
        "dpkg-query: no packages found matching pkgname",
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
        "Removing python-lxml (3.4.0-1+deb8u1) ...",
        "Removing libxslt1.1:amd64 (1.1.28-2+deb8u3) ...",
        "Purging configuration files for libxslt1.1:amd64 (1.1.28-2+deb8u3) ...",
        "Removing python-yaml (3.11-2) ...",
        "Removing libyaml-0-2:amd64 (0.1.6-3) ...",
        "Purging configuration files for libyaml-0-2:amd64 (0.1.6-3) ...",
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
        "Removing lsb-release (4.1+Debian13+nmu1) ...",
        "Purging configuration files for lsb-release (4.1+Debian13+nmu1) ...",
        "Removing man-db (2.7.0.2-5) ...",
        "Purging configuration files for man-db (2.7.0.2-5) ...",
        "  Removing catpages as well as /var/cache/man hierarchy.",
        "Removing manpages (3.74-1) ...",
        "Removing os-prober (1.65+deb8u1) ...",
        "Removing procmail (3.22-24+deb8u1) ...",
        "Removing python-boto (2.34.0-2) ...",
        "Removing python-ndg-httpsclient (0.3.2-1) ...",
        "Removing python-openssl (0.14-1) ...",
        "Removing python-cryptography (0.6.1-1+deb8u1) ...",
        "Removing python-cffi (0.8.6-1) ...",
        "Removing python-requestbuilder (0.2.3-1) ...",
        "Removing python-requests (2.4.3-6) ...",
        "Removing python-debian (0.1.27) ...",
        "Removing python-chardet (2.3.0-1) ...",
        "Removing python-cheetah (2.4.4-3) ...",
        "Removing python-configobj (5.0.6-1) ...",
        "Removing python-paramiko (1.15.1-1+deb8u1) ...",
        "Removing python-crypto (2.6.1-5+deb8u1) ...",
        "Removing python-defusedxml (0.4.1-2) ...",
        "Removing python-ecdsa (0.11-1) ...",
        "Removing python-jsonpatch (1.3-5) ...",
        "Purging configuration files for python-jsonpatch (1.3-5) ...",
        "Removing python-json-pointer (1.0-2) ...",
        "Removing python-oauth (1.0.1-4) ...",
        "Removing python-setuptools (5.5.1-1) ...",
        "Removing python-pkg-resources (5.5.1-1) ...",
        "Removing python-pycparser (2.10+dfsg-3) ...",
        "Removing python-ply (3.4-5) ...",
        "Removing python-prettytable (0.7.2-3) ...",
        "Removing python-pyasn1 (0.1.7-1) ...",
        "Removing python-pygments (2.0.1+dfsg-1.1+deb8u1) ...",
        "Purging configuration files for python-pygments (2.0.1+dfsg-1.1+deb8u1) ...",
        "Removing python-roman (2.0.0-1) ...",
        "Removing python-serial (2.6-1.1) ...",
        "Removing python-urllib3 (1.9.1-3) ...",
        "Removing python-six (1.8.0-1) ...",
        "Removing rename (0.20-3) ...",
        "update-alternatives: using /usr/bin/prename to provide /usr/bin/rename (rename) in auto mode",
        "Removing resolvconf (1.76.1) ...",
        "resolvconf.postrm: Reboot recommended",
        "Purging configuration files for resolvconf (1.76.1) ...",
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

TASK [Add repos] ****************************************************************
changed: [do1] => (item=deb http://packages.dotdeb.org     jessie all  # nginx)
changed: [do1] => (item=deb https://packages.sury.org/php/ jessie main # php5.6)
changed: [do1] => (item=deb [arch=amd64] http://lon1.mirrors.digitalocean.com/mariadb/repo/10.1/debian jessie main)

TASK [Add repo keys] ************************************************************
changed: [do1] => (item=7E3F070089DF5277)
changed: [do1] => (item=AC0E47584A7A714D)
changed: [do1] => (item=CBCB082A1BB943DB)

TASK [Add EMP-packages] *********************************************************
changed: [do1]

RUNNING HANDLER [restart sshd] **************************************************
ok: [do1]

RUNNING HANDLER [Reload sysctl] *************************************************
ok: [do1]

PLAY RECAP **********************************************************************
do1                        : ok=33   changed=21   unreachable=0    failed=0
provisioner                : ok=7    changed=1    unreachable=0    failed=0


$ time ansible-playbook destroy-DO.yml
Name of server to destroy:

PLAY [provisioner] **************************************************************

TASK [Gathering Facts] **********************************************************
ok: [provisioner]

TASK [Delete droplet] ***********************************************************
changed: [provisioner]

PLAY RECAP **********************************************************************
provisioner                : ok=2    changed=1    unreachable=0    failed=0

real	0m4,308s
user	0m1,784s
sys	0m0,398s
```
