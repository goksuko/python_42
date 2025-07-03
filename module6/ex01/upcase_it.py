#!/usr/bin/env python3

import sys

def upcase_first():
    """
    Displays the string in uppercase, followed by a newline.
    If the number of parameters is different from 1, display "none" followed by a newline.
    """

    if len(sys.argv) == 2:
        print(sys.argv[1].upper())
    else:
        print("none")

if __name__ == "__main__":
    upcase_first()