def compare(nb):
	if nb == 0:
		return "This number is both positive and negative."
	elif nb < 0:
		return "This number is negative."
	else:
		return "This number is positive."

first = int(input("Please enter the first number: \n"))
second = int(input("Please enter the second number: \n"))
result = first * second
print(f"{first} x {second} = {result}")
print(compare(result))
print()