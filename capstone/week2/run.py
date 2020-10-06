#!/usr/bin/env python3

import os, requests, sys

ip_add =  sys.argv[1] 				#hosted website ip address
dir_feed = '/data/feedback'
files = os.listdir(dir_feed)


for f in files:
	path = os.path.join(dir_feed, f)
	file = open(path)
	data = file.read().split('\n')
	dict = {'title': data[0], 'name': data[1], 'date': data[2], 'feedback': data[3]}
	response = requests.post('http://{}/feedback/'.format(ip_add), json= dict)
	print(response.status_code)
	file.close()

