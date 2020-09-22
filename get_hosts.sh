#!/bin/bash
# Usage: % sudo ./get_hosts.sh $HOME 3.7.7 192.168.101.0/24
# where: 3.7.7 is your pyenv version and 192.168.101.0/24 is the network to scan
# Json Usage: % sudo ./get_hosts.sh $HOME 3.7.7 --json 192.168.101.0/24
if ! ([ ${EUID:-$(id -u)} -eq 0 ]) ; then
    echo 'Sorry, you can only run as root'
    exit 0
fi
export HOME=$1
export PATH=$HOME/.pyenv/versions/$2/bin/:$PATH

python get_hosts.py $3 $4