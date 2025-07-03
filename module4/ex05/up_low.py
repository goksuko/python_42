#!/usr/bin/env python3

def change(letter):
	if letter.isupper():
		return letter.lower()
	else:
		return letter.upper()

str = input()
ans = ""
for letter in str:
	ans += change(letter)
print(ans)