#!/usr/bin/env python

def write_till_25(nb):
    while nb <= 25:
        print(f"Inside the loop, my variable is {nb}")
        nb += 1

nb = int(input("Enter a number less than 25\n"))
if nb > 25:
    print("Error") 
elif nb < -25:
    print("so sorry, I can't do that")
else:
	write_till_25(nb)