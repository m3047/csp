 # Content Security Policy Proof of Concept
 
 (c) 2019 Fred Morris Tacoma WA USA. Apache Licence

This is a very simple Proof of Concept demonstrating how to use a Content Security Policy
(https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) to silently audit all assets loaded by a web
page. I'm not saying you _should_ do this, just that you _can_. Given that we're talking
about the internet, somebody probably _is_ doing it. Think of it as an illustration of
unintended consequences.

## Installation

### Assumptions

* You're using the _Apache_ web server.
* The _Apache_ icons directory is served from `icons/` on the server.
* Apache directive `*.conf` files can be installed in `/etc/apache2/vhosts.d/`.
* You are installing under `/srv/www/`.
* * CGI will be installed in `/srv/www/csp/`.
* * Data (log) directory will be created as `/srv/www/data/`.
* Uses the fully qualified domain name `does-not-exist.m3047` as a domain name which should not exist!
* You have `root` access.
* `python3` is located at `/usr/bin/python3`.
* `bash` is `/bin/bash` (needed to run the installation script).
* This is a throwaway _Apache_ context. (Use a throwaway VM.)

### Prerequisites

The following _Python3_ modules are installed:

* `wsgiref`
* `json`
* `flask`

### Performing the installation

Edit the file `install.sh` and note the symbols defined at the beginning. Change any that
need changing, in particular note:

* `WWW_USER`
* `CGI_DIRECTORY`
* `DATA_DIRECTORY`

This POC was originally developed on SuSE Leap 15.0. For Debian:

* You may need to create the `/srv/www` directory.
* You may need to run `a2enmod cgi` to enable CGI.

NOTE: if you change `DATA_DIRECTORY` you will need to edit `csp.py` and if you change `CGI_DIRECTORY`
you will need to edit `csp.conf`.

Run `./install.sh` as `root`. Now restart _Apache_, e.g. `systemctl restart apache2`.

You should now be able to hit `/csp/` (note the trailing slash) on the server
and the IMG load should be logged to `$DATA_DIRECTORY/log.json`.
