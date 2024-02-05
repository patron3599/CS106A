from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
------------------------------
By: Christopher Patron 
Project: CS106A Assignment 1: Problem 1

This file instructs Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper), and then return
to its initial position in the upper left corner of the house.
"""

def main():
    get_in_position()
    collect_paper()
    get_in_position()
pass

"""
HELPER FUNCTIONS
"""

"""
collect_paper tells Karel to move an arbitrary distance until a beeper is 
present, pick up the beeper, and return to its starting condition. 
"""
def collect_paper():
    while front_is_clear():
        move()
        if beepers_present():
            pick_beeper()
            flip_karel()

# turn_right rotates Karel 3 times
def turn_right():
    for i in range(3):
        turn_left()

# flip_karel rotates Karel 180 degrees
def flip_karel():
    for i in range(2):
        turn_left()

# get_in_position prepares for Karel to execute collect_paper and return back to its original position
def get_in_position():
    turn_right()
    move()
    if facing_south():
        turn_left()
    if front_is_blocked():
        turn_right()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()