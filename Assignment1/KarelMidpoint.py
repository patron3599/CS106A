from karel.stanfordkarel import * 

"""
File: MidpointKarel.py
----------------------
By: Christopher Patron 
Project: CS106A Assignment 1: Problem 4

This file instructs Karel to find the midpoint of the world 
it is currently in. When it finds the middle Karel should leave
a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners). The world may be of any size, but it is 
assumed that it is at least as tall as it is wide.
"""

def main():
    if front_is_blocked():
        put_beeper()
    else:
        put_beeper()
        first_pass()
        converge_beepers()
        check_midpoint()
    pass

"""
HELPER FUNCTIONS
"""

# first_pass initializes the world so that converge_beepers can be executed
def first_pass():
    while front_is_clear():
        move()
        if front_is_blocked():
            put_beeper()
    flip_karel()

# converge_beepers tells Karel to move beepers one avenue over until it converges towards the middle of the world
def converge_beepers():
    move()
    while no_beepers_present():
        move()
        if beepers_present():
            pick_beeper()
            flip_karel()
            move()
            put_beeper()
            move()

# check_midpoint has Karel check that it is in the middle of the world
def check_midpoint():
    if beepers_present():
        pick_beeper()
        flip_karel()
        move()

# flip_karel rotates Karel 180 degrees
def flip_karel():
    for i in range(2):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
