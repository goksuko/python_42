#!usr/bin/env python3
import math

nb = float(input("Give me a number: "))

print(math.ceil(nb))

print("\nBONUS OPERATIONS:")
print("rounding up:")
print(math.ceil(nb))
print("rounding down:")
print(math.floor(nb))
print("rounding to the nearest integer:")
print(round(nb))