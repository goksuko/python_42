#!/usr/bin/env python3

import sys
import re

def scan_parameters():
    """
    displays the number of times the keyword appears in the string.
    If the number of parameters is different from 2 or if the first string does not appear
    in the second, it should display none followed by a newline.
    """

    if len(sys.argv) != 3:
        print("none")
    elif len(re.findall(sys.argv[1], sys.argv[2])) != 0:
        print(f"{len(re.findall(sys.argv[1], sys.argv[2]))}")
    else:
        print("none")

if __name__ == "__main__":
    scan_parameters()



