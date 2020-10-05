#!/bin/bash

line='====================================='

echo
echo "Starting at: $(date)"; echo '+++++++++++++++++++++++++++++++++++++++'

echo 'Uptime:' ; uptime ; echo $line

echo 'Free:' ; free ; echo $line

echo 'Who:'; who ; echo $line

echo "Finishing at: $(date)"; echo

