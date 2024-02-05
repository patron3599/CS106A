"""
File: biasbars.py
---------------------
By: Christopher Patron
Project: CS 106A Assignment 6: Problem 2
Date: 05/23/2022

This program is passed the word_data dictionary from biasbarsdata.py and represents the
data in that dictionary as a bar chart. This chart displays the the frequency of the word
for each gender and allows the user to input any word to see how it is applied to each
gender in a review.
"""

import tkinter
import biasbarsdata
import biasbarsgui as gui


# Provided constants to load and plot the word frequency data
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

FILENAME = "data/full-data.txt"

VERTICAL_MARGIN = 30
LEFT_MARGIN = 60
RIGHT_MARGIN = 30
LABELS = ["Low Reviews", "Medium Reviews", "High Reviews"]
LABEL_OFFSET = 10
BAR_WIDTH = 75
LINE_WIDTH = 2
TEXT_DX = 2
NUM_VERTICAL_DIVISIONS = 7
TICK_WIDTH = 15


def get_centered_x_coordinate(width, idx):
    """
    Given the width of the canvas and the index of the current review
    quality bucket to plot, returns the x coordinate of the centered
    location for the bars and label to be plotted relative to.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current label in the LABELS list
    Returns:
        x_coordinate (float): The centered x coordinate of the horizontal line 
                              associated with the specified label.
    >>> round(get_centered_x_coordinate(1000, 0), 1)
    211.7
    >>> round(get_centered_x_coordinate(1000, 1), 1)
    515.0
    >>> round(get_centered_x_coordinate(1000, 2), 1)
    818.3
    """

    # Calculating the plotting region's width
    region_width = width - LEFT_MARGIN - RIGHT_MARGIN

    # For Low Review
    if idx == 0:
        x_coordinate = ((region_width/3)/2) + LEFT_MARGIN
        return x_coordinate

    # For Medium Review
    elif idx == 1:
        x_coordinate = (region_width/2) + LEFT_MARGIN
        return x_coordinate

    # For High Review
    elif idx == 2:
        x_coordinate = ((region_width*2)/3) + ((region_width/3)/2) + LEFT_MARGIN
        return x_coordinate


def draw_fixed_content(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background border and x-axis labels on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing content from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas

    # Creating plotting region
    canvas.create_rectangle(LEFT_MARGIN, VERTICAL_MARGIN, width - RIGHT_MARGIN, height - VERTICAL_MARGIN,
                            width=LINE_WIDTH)

    # Creating review labels
    for i in range(len(LABELS)):
        canvas.create_text(get_centered_x_coordinate(width, i), height - (LABEL_OFFSET + VERTICAL_MARGIN/2),
                           text=LABELS[i], anchor=tkinter.N)


def plot_word(canvas, word_data, word):
    """
    Given a dictionary of word frequency data and a single word, plots
    the distribution of the frequency of this word across gender and 
    rating category.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        word_data (dictionary): Dictionary holding word frequency data
        word (str): The word whose frequency distribution you want to plot
    """

    draw_fixed_content(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    region_height = height - (2*VERTICAL_MARGIN)

    # We have provided code to calculate the maximum frequency for the specified
    # word from the provided dict 
    gender_data = word_data[word]
    max_frequency = max(max(gender_data[biasbarsdata.KEY_WOMEN]), max(gender_data[biasbarsdata.KEY_MEN]))
    
    # Creating Tick Marks
    x1 = LEFT_MARGIN - (TICK_WIDTH/2)
    x2 = LEFT_MARGIN + (TICK_WIDTH/2)

    tick_ht = []
    for i in range(NUM_VERTICAL_DIVISIONS+1):
        temp_ht = VERTICAL_MARGIN + ((region_height*i)/NUM_VERTICAL_DIVISIONS)
        tick_ht.append(temp_ht)
        canvas.create_line(x1, tick_ht[i], x2, tick_ht[i], width=LINE_WIDTH)

    # Creating Tick Labels
    tick_label = []
    for i in range(NUM_VERTICAL_DIVISIONS + 1):
        temp_label = int((max_frequency*i)/NUM_VERTICAL_DIVISIONS)
        tick_label.append(temp_label)

    rev_tick_label = tick_label[::-1]
    for i in range(NUM_VERTICAL_DIVISIONS + 1):
        canvas.create_text(LEFT_MARGIN-LABEL_OFFSET, tick_ht[i], text=rev_tick_label[i], anchor=tkinter.E)

    # Creating Bars

    # For Women Data Points
    y2_w = region_height + VERTICAL_MARGIN

    for i in range(len(LABELS)):
        x_w = get_centered_x_coordinate(width, i)
        y1_w = height - VERTICAL_MARGIN - region_height*(gender_data[biasbarsdata.KEY_WOMEN][i]/max_frequency)
        # Makes Bars
        canvas.create_rectangle(x_w - BAR_WIDTH, y1_w, x_w, y2_w, fill='dodgerblue')
        # Makes Label
        if gender_data[biasbarsdata.KEY_WOMEN][i] != 0:
            canvas.create_text(x_w - BAR_WIDTH + TEXT_DX, y1_w, text='W', anchor=tkinter.NW)

    # For Men Data Points
    y2_m = region_height + VERTICAL_MARGIN

    for i in range(len(LABELS)):
        x_m = get_centered_x_coordinate(width, i)
        y1_m = height - VERTICAL_MARGIN - region_height*(gender_data[biasbarsdata.KEY_MEN][i]/max_frequency)
        # Makes Bars
        canvas.create_rectangle(x_m, y1_m, x_m + BAR_WIDTH, y2_m, fill='orange')
        # Makes Label
        if gender_data[biasbarsdata.KEY_MEN][i] != 0:
            canvas.create_text(x_m + TEXT_DX, y1_m, text='M', anchor=tkinter.NW)


def convert_counts_to_frequencies(word_data):
    """
    This code is provided to you! 

    It converts a dictionary 
    of word counts into a dictionary of word frequencies by 
    dividing each count for a given gender by the total number 
    of words found in reviews about professors of that gender.
    """ 
    K = 1000000
    total_words_men = sum([sum(counts[biasbarsdata.KEY_MEN]) for word, counts in word_data.items()])
    total_words_women = sum([sum(counts[biasbarsdata.KEY_WOMEN]) for word, counts in word_data.items()])
    for word in word_data:
        gender_data = word_data[word]
        for i in range(3):
            gender_data[biasbarsdata.KEY_MEN][i] *= K / total_words_men
            gender_data[biasbarsdata.KEY_WOMEN][i] *= K / total_words_women


# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])

    # Load data
    word_data = biasbarsdata.read_file(FILENAME)
    convert_counts_to_frequencies(word_data)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Bias Bars')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, word_data, plot_word, biasbarsdata.search_words)

    # draw_fixed once at startup so we have the borders and labels
    # even before the user types anything.
    draw_fixed_content(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
