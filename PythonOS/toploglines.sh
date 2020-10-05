#!/bin/bash

#for logfile in /var/log/*log    all log files
for logfile in /var/log/syslog ; do
	echo "Presenting: $logfile"
	cut -d' ' -f5- $logfile | sort | uniq -c| sort -nr | head -10

done
