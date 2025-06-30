#!/usr/bin/env python

nb = int(input("Please enter a number: "))
if nb == 0:
    print("This number is both positive and negative.")
elif nb < 0:
	print("This number is negative.")
else:
    print("This number is positive.")