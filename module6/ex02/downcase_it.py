#!/usr/bin/env python3

import sys

def downcase_first():
    """
    Convert the first command line argument to lowercase.
    If the number of parameters is different from 1,
    it should display "none" followed by a newline.
	"""

    if len(sys.argv) == 2:
        print(sys.argv[1].lower())
    else:
        print("none")

if __name__ == "__main__":
    downcase_first()