#!/usr/bin/env python


import os
import subprocess as sp

my_env = os.environ.copy()
my_env['PATH'] = os.pathsep.join(['/opt/myapp/', my_env['PATH']])

result = sp.run(['myapp'], env=my_env)
