"""
File: rating_stats.py
----------------------
By: Christopher Patron
Project: CS 106A Assignment 6: Problem 2
Date: 05/17/2022

This file defines a program that allows a user to calculate
baseline summary statistics about a datafile of professor review
data. 
"""


def calculate_rating_stats(filename):
    """
    This function analyzes the professor review data in the given
    file to calculate the percentage of reviews for both men and
    women that fall in the "high rating" bucket, which is a numerical
    rating that is greater than 3.5.

    The resulting information is printed to the console.
    """

    # Initialize counters
    tot_counter_M = 0
    tot_counter_W = 0
    high_counter_M = 0
    high_counter_W = 0

    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            lst = line.split(',')
            lst[0] = float(lst[0])

            # Conditions are checked wether the review is for a M or W and if the rating > 3.5
            if lst[1] == 'M' and lst[0] > 3.5:
                high_counter_M += 1
                tot_counter_M += 1
            elif lst[1] == 'M' and lst[0] <= 3.5:
                tot_counter_M += 1
            elif lst[1] == 'W' and lst[0] > 3.5:
                high_counter_W += 1
                tot_counter_W += 1
            elif lst[1] == 'W' and lst[0] <= 3.5:
                tot_counter_W += 1

    # Calculating percentages
    women_rating = round(100*(high_counter_W / tot_counter_W))
    men_rating = round(100*(high_counter_M / tot_counter_M))

    # Printing results
    print(str(women_rating) + '% of reviews for women in the data set are high.')
    print(str(men_rating) + '% of reviews for men in the data set are high.')



def main():
    # Ask the user to input the name of a file
    filename = input("Which data file would you like to load?") # 'data/full-data.txt'

    # Calculate review distribution statistics by gender for
    # that file. This function should print out the results of
    # the analysis to the console.
    calculate_rating_stats(filename)


if __name__ == '__main__':
    main()
