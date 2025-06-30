#!/usr/bin/env python3

def m_table(nb):
    a = 0
    while a <= 9:
        print(f"{a} x {nb} = {nb * a}")
        a += 1

nb = int(input("Enter a number\n"))
if nb > 25:
    print("so sorry, I can't do that") 
elif nb < -25:
    print("so sorry, I can't do that")
else:
    m_table(nb)