#!/usr/bin/env python3

arr = [1, 2, 3, 4, 5, 42, -100, 0, 99]
new = []

for n in arr:
	if n > 5:
		new.append(n + 2)

print(f"Original array: {arr}")
print(f"New array: {new}")