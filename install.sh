#!/bin/bash

WWW_USER=wwwrun
CGI_DIRECTORY=/srv/www
DATA_DIRECTORY=/srv/www/data
VHOSTS_DIRECTORY=/etc/apache2/vhosts.d
APACHE_CONF=csp.conf

cp csp.conf $VHOSTS_DIRECTORY/$APACHE_CONF
chown root $VHOSTS_DIRECTORY/$APACHE_CONF

cp -a csp $CGI_DIRECTORY
chown -R $WWW_USER $CGI_DIRECTORY/csp

mkdir $DATA_DIRECTORY
chown $WWW_USER $DATA_DIRECTORY


