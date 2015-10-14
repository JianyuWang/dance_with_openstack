#!/bin/bash

conf="/etc/my.cnf"
subpat='^[^=]*basedir[^=]*=\(.*\)$'
dirs=`sed -e "/$subpat/!d" -e 's//\1/' $conf`      
echo $dirs
