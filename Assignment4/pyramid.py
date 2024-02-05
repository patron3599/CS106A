"""
File: pyramid.py
----------------
By: Christopher Patron
Project: CS 106A Assignment 4: Problem 2.A
Date: 04/28/2022

This program creates a stack of rectangles in a pyramid formation.
The dimensions of the pyramid can be adjusted to produce a new one
of based off the number of bricks in the pyramid's base.

"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_pyramid(canvas):
    """
    draw_pyramid is passed the canvas created in make_canvas. This function
    then creates the pyramid with a nested for-loop that is creating the
    individual rectangles and arranging them into the shape of the pyramid.
    """

    # Initializing the variables for the current row
    for j in range(BRICKS_IN_BASE):
        new_base = BRICKS_IN_BASE - j
        bb_up_x = (CANVAS_WIDTH - (new_base * BRICK_WIDTH)) * 0.5
        bb_up_y = CANVAS_HEIGHT - BRICK_HEIGHT*(j+1)
        bb_low_x = bb_up_x + BRICK_WIDTH
        bb_low_y = bb_up_y + BRICK_HEIGHT

        # Creates current row based on the variables in the loop above
        for i in range(new_base):
            canvas.create_rectangle(bb_up_x + i*BRICK_WIDTH, bb_up_y, bb_low_x + i*BRICK_WIDTH, bb_low_y)



######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 2, height=height + 2)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
