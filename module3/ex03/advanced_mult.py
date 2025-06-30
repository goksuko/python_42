#!/usr/bin/env python3

a = 0
while (a <= 10):
    b = 0
    s = f"Table of {a}: "
    while (b <= 10):
        s += f"{a * b} "
        b += 1
    print(s)
    a += 1
    