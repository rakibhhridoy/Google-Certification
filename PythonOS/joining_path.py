#!/usr/bin/env python 

import os

path = input('Enter Path: ')

files = os.listdir(path)
 
for f in files:
	fullname = os.path.join(path, f)
	print(fullname)

def with_cwd():
	path = os.getcwd()
	files = os.listdir(path)
	for f in files:
		fullname = os.path.join(path,f)
		print(fullname)

with_cwd()
