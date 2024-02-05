from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
------------------------
By: Christopher Patron 
Project: CS106A Assignment 1: Problem 3

This file instructs Karel to create a checkerboard pattern with 
beepers for a world of arbitrary width and height.
"""

def main():
    put_beeper()
    if front_is_blocked():
        scale_up()
    else:
        while front_is_clear():
            scale_forward()
    pass

"""
HELPER FUNCTIONS
"""

# scale_up is called if Karel is in a "column" world
def scale_up():
    turn_left()
    while front_is_clear():
        move()
        if no_beepers_present():
            if front_is_clear():
                move()
                put_beeper()

# scale_forward instructs Karel to do a forward pass through a row
def scale_forward():
    while front_is_clear():
        move()
        if no_beepers_present():
            if front_is_clear():
                move()
                put_beeper()

    # An end-condition check to determine if there is an even or odd number of columns in the world
    if no_beepers_present():
        turn_left()
        scale_backwards_even()
    else:
        turn_left()
        scale_backwards_odd()

# scale_backwards_even is called if their is an even number of columns in the world
def scale_backwards_even():
    if front_is_clear():
        move()
        put_beeper()
        turn_left()
        while front_is_clear():
            move()
            if no_beepers_present():
                if front_is_clear():
                    move()
                    put_beeper()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            put_beeper()

# scale_backwards_odd is called if their is an odd number of columns in the world
def scale_backwards_odd():
    if front_is_clear():
        move()
        turn_left()
        while front_is_clear():
            move()
            if no_beepers_present():
                if front_is_clear():
                    put_beeper()
                    move()
        turn_right()
        if front_is_clear():
            move()
            turn_right()
            put_beeper()

# turn_right rotates Karel 3 times
def turn_right():
    for i in range(3):
        turn_left()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
