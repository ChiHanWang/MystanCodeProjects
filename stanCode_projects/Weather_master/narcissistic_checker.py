"""
File: extension4_narcissistic_checker.py
Name: Michelle
------------------------
This program asks our user for input and checks if the input is a
narcissistic number or not.

A positive integer is called a narcissistic number if it
is equal to the sum of its own digits each raised to the
power of the number of digits.

Example: 153 is narcissistic because 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.
Note that by this definition all single digit numbers are narcissistic.

Students are recommended to use // and % to complete this program.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    This program checks if the input is a narcissistic number or not.
    """
    print('Welcome to the narcissistic number checker!')
    while True:
        number = int(input('n: '))
        if number == EXIT:
            break
        else:
            # check number's length
            length = 0
            current = number
            while current > 0:
                current //= 10
                length += 1

            # process the number
            total = 0
            current = number
            while current > 0:
                unit = current % 10
                total += unit ** length
                current = (current - unit) // 10

            if total == number:
                print(str(number) + ' is a narcissistic number')
            else:
                print(str(number) + ' is not a narcissistic number')

    print('Have a good one!')

    # Below is another way of doing it

    # print("Welcome to the narcissistic number checker!")
    # while True:
    #     number = int(input("n: "))
    #     total = 0  # use 'total' to record
    #     if number == EXIT:
    #         print("Have a good one!")
    #         break
    #     else:
    #         n1 = number
    #         n2 = number
    #         length = 0
    #
    #         # check number's length
    #         while n1 != 0:
    #             n1 //= 10
    #             length += 1  # calculate the length of the number
    #
    #         # process the number
    #         while n2 != 0:
    #             data = n2 % 10  # collect all single digit numbers of n
    #             n2 //= 10
    #             total += (data ** length)
    #
    #         if total == number:
    #             print(str(number) + " is a narcissistic number")
    #         else:
    #             print(str(number) + " is not a narcissistic number")


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
