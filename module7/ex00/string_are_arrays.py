#!/usr/bin/env python3

import sys

def print_z():
	"""
	displays "z" for each occurrence of the character
	"z" in the string passed as a parameter, followed by a newline.
	If the number of parameters is different from 1, or if there are no "z" characters in
	the string, it should display "none" followed by a newline."
	"""
	if len(sys.argv) != 2:
		print("none")
		return

	# count = sys.argv[1].count('z')
	count = 0
	for char in sys.argv[1]:
		if char == 'z':
			count += 1
	if count == 0:
		print("none")
	else:
		print('z' * count)

if __name__ == "__main__":
	print_z()
