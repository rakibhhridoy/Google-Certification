#!/usr/bin/env python

import os

path = os.getcwd()
elements = os.listdir(path)
 
for elem in elements:
	fullname = os.path.join(path, elem)
	if os.path.isdir(fullname):
		print('{} =========  is a Directory'.format(fullname))
	else:
		print('{} ========= is a file'.format(fullname))

