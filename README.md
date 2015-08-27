# SERVIT #

ARCH VERSION - Under Active Development!
```
 ____  _____ ______     _____ _____
/ ___|| ____|  _ \ \   / /_ _|_   _|
\___ \|  _| | |_) \ \ / / | |  | |  
 ___) | |___|  _ < \ V /  | |  | |  
|____/|_____|_| \_\ \_/  |___| |_|  

```
[![Build Status](https://travis-ci.org/aerth/arch-servit.svg)](https://travis-ci.org/aerth/arch-servit)

MIT LICENSE

Contributors:

aerth

### CLI interface for Arch server management, including support for: ###

* Apache2 Virtual Hosts
* Postfix / Dovecot Email Address Management
* EASY SSH / SCP
* ASCII ART
* Add User
* Easy to add your favorite scripts
* Super CLI Menu


### How do I get set up? ###




* httpd.conf before using httpd-createsite

Find this:
```
# Virtual hosts
#Include conf/extra/httpd-vhosts.conf
```

And make it this:
```
# Virtual hosts
#Include conf/extra/httpd-vhosts.conf
Include conf/extra/servit-arch.conf
```

Restart your httpd (using systemctl or servit)

* Clone it!
```
git clone https://github.com/aerth/servit.git

```


* Install it!


```
sudo cp ./dependencies/httpd-createsite /usr/local/bin/
sudo cp ./arch-servit /usr/local/bin/
sudo chmod +x /usr/local/bin/arch-servit
sudo chmod +x /usr/local/bin/httpd-createsite

```

* Run it!

```
arch-servit
```

* Dependencies
httpd-createsite. Arch. Superuser. Python + Ncurses.


### Contributing? ###

* Review code
* Make sure your changes didn't break the app
* Describe changes in git commits

### Who do I talk to? ###

* Repo admin

aerth@isupon.us (email)

### Future Releases ###

Next release will have support for Red Hat, CentOS, and Arch servers.
If you know how that works, go ahead and do it. Pull requests are welcome.
