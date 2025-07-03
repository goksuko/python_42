#!/usr/bin/env python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
print(f"Original array: {arr}")

new_set = set(arr)
print(f"Original set: {new_set}")

# res = []
# for i in new_set:
# 	if i > 5:
# 		res.append(i + 2)
res = [i + 2 for i in new_set if i > 5]
print(f"New array: {res}")
