#!/usr/bin/env python3

import sys

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print("none")
	else:
		try:
			start = int(sys.argv[1])
			end = int(sys.argv[2])
			if start > end:
				print("none")
			else:
				new_arr = []
				for i in range(start, end + 1):
					new_arr.append(i)
				print(new_arr)
		except ValueError:
			print("none")

