#!/usr/bin/env python3

import sys
import tkinter
import json

CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600


def draw_grid(canvas, grid):
    """
    Given a grid of colors, and a canvas, we want to visualize
    this grid on the canvas. For example, given a grid:

    [['red', 'orange', 'yellow'],
     ['green', 'blue', 'purple']]

    We would want to draw 6 boxes on our canvas, where all boxes
    have the same width and height, and are colored according to
    the values in the grid. Use the width and height of your grid
    to determine how many boxes to draw, and how wide/tall each
    box should be. Use the create_rectangle() function to draw on
    your canvas. To preview the expected output for the grid
    shown above, run python3 draw_grid_soln.py.
    """

    len1 = len(grid)
    len2 = len(grid[0])
    tot_len = len1 * len2

    coords = [(0, 0)]
    for i in range(1, tot_len+1):
        x = CANVAS_WIDTH/(i)










def make_canvas(width, height, title):
    """
    (Provided code).
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "grid")
    # try modifying this grid to get different drawings!
    grid = [['red', 'orange', 'yellow'], ['green', 'blue', 'purple']]
    draw_grid(canvas, grid)
    canvas.mainloop()


if __name__ == "__main__":
    main()

