#!/usr/bin/env python3

import sys

def display_first():
    if len(sys.argv) > 1:
        print(sys.argv[1])
    else:
        print("none")

if __name__ == "__main__":
    display_first()