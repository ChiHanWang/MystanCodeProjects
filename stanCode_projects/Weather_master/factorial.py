"""
File: factioral.py
Name: Michelle
-------------------
This program will continually ask our user to give a number
and will calculate the factorial result of the number and print it on the console.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
	"""
	The program computes the answer of factorial.
	"""
	print("Welcome to stanCode factorial master!")
	while True:
		n = int(input("Give me a number, and I will list the answer of factorial: "))
		if n == EXIT:
			print("------See ya!------")
			break
		else:
			a = 1   # give initial value
			for i in range(1, n+1):   # (n+1): The upper limit must include n.
				a = a * i       # according to the number I give, it computes the answer of factorial.
			print("Answer: " + str(a))

	# Below is another way of doing it

	# print('Welcome to stanCode factorial master!')
	# while True:
	# 	n = int(input('Give me a number, and I will list the answer of factorial: '))
	# 	if n == EXIT:
	# 		break
	# 	else:
	# 		count = 1
	# 		ans = 1
	# 		while n != count:
	# 			count += 1
	# 			ans *= count
	# 		print('Answer: ' + str(ans))
	# print('------See ya!------')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
	main()
