#!/usr/bin/env python3

import sys

def rev_params():
	"""
	Displays all the strings passed as parameters,
	followed by a newline, in reverse order.
	If there are fewer than two parameters,
	it should display "none" followed by a newline.
	"""
	if len(sys.argv) > 2:
		for param in reversed(sys.argv[1:]):
			print(param)
	else:
		print("none")

if __name__ == "__main__":
	rev_params()