"""
File: pythagorean.py
--------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 1.F
Date: 04/15/2022

Doing some trigonometry? Forgot your calculator? No worries!
This function calculates the Pythagorean Theorem for you.
"""

import math

def main():
    print('Enter values to compute the Phytagorean Theorem (a^2 + b^2 = c^2): ')
    a = float(input('Input a value for a: '))
    b = float(input('Input a value for b: '))
    c = pythag_thm(a, b)
    print('The length of the third leg, c is: ' + str(c))

    pass

"""
Helper Functions
"""

""" 
pythag_thm() receives the parameters of a and b and calculates the value of c to be 
returned as an argument to the main function.  
"""
def pythag_thm(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
