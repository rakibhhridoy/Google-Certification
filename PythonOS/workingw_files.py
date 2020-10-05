#!/usr/bin/env python

import datetime
import os

#remove an existing file
os.remove('testing.txt')

#rename an existing file
os.rename('spider1.txt','spider_1.txt')

#searching as file exists or not
os.path.exists('spider_1.txt')

#get file size
os.path.getsize('spider_1.txt')

#time of modification/creation of a file
def file_time():
	timestamp = os.path.getmtime('spider_1.txt')
	print(datetime.datetime.fromtimestamp(timestamp))

file_time()
