"""
File: random_numbers.py
-----------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 1.D
Date: 04/15/2022

This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

def main():
    print('Here are 10 random numbers: ')
    print('')
    generate_rand_nums()

    pass

"""
Helper Functions
"""

# generate_rand_nums() generates 10 random numbers to returned to the user
def generate_rand_nums():
    NUM_RANDOM = 10
    MIN_RANDOM = 0
    MAX_RANDOM = 100
    for i in range(NUM_RANDOM):
        num = random.randint(MIN_RANDOM, MAX_RANDOM)
        print('Number ' + str(i+1) + ': ' + str(num))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
