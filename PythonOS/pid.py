#!/usr/bin/env python

import re

def extract_pid(log):
	regex = r'\[(\d+)\]'
	result = re.search(regex, log)
	if result is None:  
		return ''
	return result[1]
