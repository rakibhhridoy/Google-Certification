#!/usr/bin/env python

import os
import sys

filename = sys.argv[1]

os.system("cat {} | tr ' |,|.' '\n' | sort | uniq -c | sort -nr".format(filename))



