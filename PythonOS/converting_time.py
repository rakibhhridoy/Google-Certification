#!/usr/bin/env python


def to_seconds(hours,minuets,seconds):
	return hours*3600+minuets*60+seconds*60

print('Welcome To Time Converter!\n==========================\n')
cont = "y"
while (cont.lower() == "y"):
	hours = int(input('Hours: '))
	minuets = int(input('Minuets: '))
	seconds = int(input('Seconds: '))

	print("Thats {} seconds!".format(to_seconds(hours, minuets, seconds)))
	print()
	cont = input("Do you want to do another conversion? [y to continue]: ")

print('bye buddy!')
