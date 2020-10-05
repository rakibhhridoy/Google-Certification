#!/usr/bin/env python

import os
import sys
import re
import subprocess as sp

filename = sys.argv[1]

if not os.path.exists(filename):
	with open(filename, 'w') as f:

		if not re.search('.py$', filename) is None:
			f.write('#!/usr/bin/env python')

		elif not re.search('.sh$',filename) is None:
			f.write('#!/bin/bash')

		else:
			f.write('{} is created,start writing more'.format(filename))
		print('file created')

else:
	print('Error {} file is already exists!'.format(filename))


sys.exit(1)

