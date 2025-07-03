#!/usr/bin/env python3

import sys

def print_parameters():
    print(f"Number of parameters: {len(sys.argv) - 1}.")

if __name__ == "__main__":
    print_parameters()