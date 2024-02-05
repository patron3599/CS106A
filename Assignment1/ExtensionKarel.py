from karel.stanfordkarel import *

"""
File: ExtensionKarel.py
-----------------------
This file is for optional extension programs. 
"""

def main():
    put_beeper()
    first_pass()
    converge_beepers()
    check_midpoint()
    make_stump()
    set_up_tree()
    #move_forward()
    #start_tree()
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
        pick_beeper()

def make_stump():
    move()
    turn_right()
    for i in range(3):
        for j in range(3):
            put_beeper()
            move()
        flip_karel()
        while front_is_clear():
            move()
        turn_left()
        move()
        turn_left()

def set_up_tree():
    for i in range(2):
        move()
    turn_left()
    put_beeper()
    if left_is_blocked():
        continue_tree()
    else:
        finish_base()

def finish_base():
    flip_karel()
    while front_is_clear():
        move()
        put_beeper()
    flip_karel()
    set_flag_right()
    while beepers_present():
        move()
        if no_beepers_present():
            put_beeper()
        if front_is_blocked():
            set_flag_left()




def continue_tree():
    set_flag_right()
    move()
    while front_is_clear():
        put_beeper()
        move()
        if beepers_present():
            pick_beeper()
            turn_left()


def start_tree():
    for i in range(2):
        move()
    turn_left()
    put_beeper()
    move_backward()
    move_forward()


def move_forward():
    set_flag_left()
    turn_right()
    move()
    while front_is_clear():
        put_beeper()
        move()
        if beepers_present():
            pick_beeper()
            turn_left()


def move_backward():
    set_flag_right()
    if right_is_blocked():
        while front_is_clear():
            if beepers_present():
                move()
            else:
                put_beeper()
    else:
        flip_karel()
        while front_is_clear():
            put_beeper()
            move()
    turn_right()
    put_beeper()


def set_flag_left():
    turn_right()
    move()
    turn_left()
    if front_is_clear():
        move()
        put_beeper()

def set_flag_right():
    move()
    turn_right()
    if front_is_clear():
        move()
        put_beeper()
        flip_karel()
        move()
        turn_right()


# flip_karel rotates Karel 180 degrees
def flip_karel():
    for i in range(2):
        turn_left()

# turn_right rotates Karel 3 times
def turn_right():
    for i in range(3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
