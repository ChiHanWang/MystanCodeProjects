"""
File: quadratic_solver.py
Name: Michelle
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	We can find the answer of quadratic polynomial function.
	"""
	print("stanCode Quadratic Solver!")
	a = int(input('Enter a: '))
	b = int(input('Enter b: '))
	c = int(input('Enter c: '))

	# 判別式
	discriminant = b ** 2 - 4 * a * c

	if discriminant < 0:
		print("No real roots")
	else:
		if discriminant > 0:
			root1 = (-b + math.sqrt(discriminant)) / (2 * a)
			root2 = (-b - math.sqrt(discriminant)) / (2 * a)
			print("Two roots: " + str(root1) + " , " + str(root2))
		elif discriminant == 0:
			root = (0 - b) / (2 * a)
			print("One root: " + str(root))


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
	main()
