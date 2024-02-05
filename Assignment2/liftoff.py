"""
File: liftoff.py
----------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 1.C
Date: 04/15/2022

This program writes out the calls for a spaceship that is about to launch.
It counts down the numbers from 10 to 1 and then writes “Liftoff!”
"""

def main():
    print('Launch Initiated!')
    print('')
    countdown()
    print('')
    print('We Have Liftoff!')

    pass

"""
Helper Functions
"""

# countdown() performs the countdown sequence for the spaceship's launch
def countdown():
    for i in range(10):
        index = 10-i
        print(str(index))


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()
