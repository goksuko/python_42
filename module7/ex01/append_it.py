#!/usr/bin/env python3

import sys

def append_it():
	"""
	displays each parameter passed as an argument, one by one, by
	appending it with "ism".
	If a parameter already ends with "ism", it should be skipped and not displayed.
	If there are no parameters, the program should display "none" followed by a newline.
	"""
	if len(sys.argv) < 2:
		print("none")
		return

	for arg in sys.argv[1:]:
		# if arg.endswith("ism"):
		if arg.find("ism", len(arg) - 3) != -1:
			continue
		print(arg + "ism")

if __name__ == "__main__":
	append_it()