"""
File: extension3_triangular_checker.py
Name: Michelle
--------------------------
This program asks our user for input and checks if the input is an
triangular number or not.

The triangular number (Tn) is a number that can be represented in the form of a triangular
grid of points where the first row contains a single element and each subsequent row contains 
one more element than the previous one.

We can just use the fact that the nth triangular number can be found by using a formula: Tn = n(n + 1) / 2.

The program ends when the user enter the EXIT number.
"""

EXIT = -100


def main():
    """
    The program checks if the input is an triangular number or not.
    """
    print('Welcome to the triangular number checker!')
    while True:
        number = int(input('n: '))
        if number == EXIT:
            break
        else:
            check = 1
            triangle_n = 1
            # process the number inputted
            while number > check:
                triangle_n = check * (check + 1) / 2
                if number == triangle_n:
                    print(str(number) + ' is a triangular number')
                    break
                check += 1
            if triangle_n != number:
                print(str(number) + ' is not a triangular number')
    print('Have a good one!')

    # Below is another way of doing it

    # print("Welcome to the triangular number checker!")
    # while True:
    #     number = int(input("n: "))
    #     if number == EXIT:
    #         print("Have a good one!")
    #         break
    #     else:
    #         i = 1
    #         while True:
    #             if ((i + 1) * i) // 2 == number:
    #                 print(str(number) + " is a triangular number")
    #                 break
    #             elif ((i + 1) * i) // 2 > number:
    #                 print(str(number) + " is not a triangular number")
    #                 break
    #             i += 1


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
