"""
File: rocket.py
Name: Michelle
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 3 Handout.

"""

# This constant determines rocket size.
SIZE = 5


def main():
    """
    This rocket consist of 6 parts: 2 heads, 2 belts, 1 upper body and 1 lower body
    """
    head()
    belt()
    upper_body()
    lower_body()
    belt()
    head()


def head():
    """
    To make a triangle part used at the top and the end of the rocket and print it in the console
    :return: None
    """
    for i in range(SIZE):               # The variable "i" means which "row" to print

        # Print each row
        for j in range(SIZE - i):
            print(' ', end="")          # print empty string
        for j in range(i + 1):
            print('/', end="")          # print /
        for j in range(i + 1):
            print("\\", end="")         # print \

        print("")                       # Move to next row


def belt():
    """
    To make a belt of the rocket and print it in the console
    :return: None
    """
    print('+', end="")
    for i in range(SIZE * 2):
        print('=', end="")
    print('+')


def upper_body():
    """
    To make the upper part of the rocket and print it in the console
    :return: None
    """
    for i in range(SIZE):
        print('|', end="")
        for j in range(SIZE - i - 1):
            print('.', end="")             # print .
        for j in range(i + 1):
            print('/\\', end="")           # print /\
        for j in range(SIZE - i - 1):
            print('.', end="")             # print .
        print('|')


def lower_body():
    """
    To make the lower part of the rocket and print it in the console
    :return: None
    """
    for i in range(SIZE):
        print('|', end="")
        for j in range(i):
            print('.', end="")              # print .
        for j in range(SIZE - i):
            print('\\', end="")             # print \/
            print('/', end="")
        for j in range(i):
            print('.', end="")              # print .
        print('|')


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == "__main__":
    main()
