from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
------------------------
By: Christopher Patron 
Project: CS106A Assignment 1: Problem 2

This file instructs Karel to re-build broken columns (represented 
as beepers). In this file, Karel will scale each column and place 
a beeper as necessary to repair the columns of arbitrary length, 
but are a fixed distance apart from each other. 
"""

def main():
    turn_left()
    while right_is_clear():
        scale_col()
        shift_col()
    scale_col()

"""
HELPER FUNCTIONS
"""

# scale_col instructs Karel to climb up the column that is to be repaired
def scale_col():
    # Moving up the column
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()
        if no_beepers_present():
            put_beeper()

    # Moving down the column
    flip_karel()
    if no_beepers_present():
        put_beeper()
    while front_is_clear():
        move()

# shift_col instructs Karel to shift to the next column to be repaired
def shift_col():
    turn_left()
    for i in range(4):
        move()
    turn_left()

# turn_right rotates Karel 3 times
def turn_right():
    for i in range(3):
        turn_left()

# flip_karel rotates Karel 180 degrees
def flip_karel():
    for i in range(2):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
