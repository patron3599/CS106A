"""
File: subtract_numbers.py
-------------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 1.B
Date: 04/15/2022

This program gets two real-values from the user and prints
the first number minus the second number.
"""

def main():
    print('This program subtracts two numbers')

    # Subtraction operation begins
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    ans = num1 - num2

    # Result from subtraction operation is returned to the user
    print('The total is: ' + str(ans))

    pass

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
