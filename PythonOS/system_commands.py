#!/usr/bin/env python

import subprocess as sp

sp.run(['date'])

sp.run(['ls','-al'])

result = sp.run(['pwd'])
print(result)
print(result.returncode)


#sp.run(['shutdown'])

sp.run(['sleep','2'])
