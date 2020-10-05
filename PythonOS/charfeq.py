#!/usr/bin/env python


import os 
import sys

filename = sys.argv[1]

def character_frequency_words():
	try:
		f = open(filename)
	except OSError:
		return None

	characters = {}
	for line in f:
		for char in line:
			characters[char] = characters.get(char, 0) +1
	f.close()

	print(characters)

character_frequency_words()


