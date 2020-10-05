#!/usr/bin/env python

import os

def workingdir1():
	#get working dir
	print(os.getcwd())

	def creating_dir():
		#make a directory
		os.mkdir('done')
	
	creating_dir()
	#change to a directory
	os.chdir('done')

	os.mkdir('done1')

	#removing a empty directory
	os.rmdir('done1')

workingdir1()

#list of files and directories

def workingdir2():
	os.chdir('..')
	
	for name in os.listdir(os.getcwd()):
		fullname = os.path.join(os.getcwd(), name)
		if os.path.isdir(fullname):
			print('{} ========> is a dir'.format(fullname))
		else:
			print('{}  ========>  is a file'.format(fullname))

workingdir2()

