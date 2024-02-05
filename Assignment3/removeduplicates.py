"""
File: removeduplicates.py
-------------------------
By: Christopher Patron
Project: CS 106A Assignment 3: Problem 1.B
Date: 04/18/2022

This program gives you practice with constructing a new list
based on values given to you by the user.  You also get
practice removing duplicates from that list
"""


def read_list():
    """
    This function should ask the user for a series of integer values
    (until the user enters 0 to stop) and store all those values in a
    list.  That list should then be returned by this function.
    """

    # Initialize num_list
    num_list = []
    elem = int(input('Enter value (0 to stop): '))
    while elem != 0:
        num_list.append(elem)
        elem = int(input('Enter value (0 to stop): '))
    return num_list

    pass


def remove_duplicates(num_list):
    """
    This function is passed a list of integers and returns a new
    list with all duplicate values from the original list remove.A
    >>> remove_duplicates([1, 2, 3, 2, 3, 4])
    [1, 2, 3, 4]
    >>> remove_duplicates([1, 1, 1])
    [1]
    >>> remove_duplicates([])
    []
    """

    # Initialize no_duplicates
    no_duplicates = []
    for elem in num_list:
        # Once we have placed elem in list, we check that an element of the same value is not there
        if elem not in no_duplicates:
            no_duplicates.append(elem)
    return no_duplicates



def main():
    num_list = read_list()
    print("Original list entered by user: ")
    print(num_list)

    no_duplicates = remove_duplicates(num_list)
    print("List with duplicates removed: ")
    print(no_duplicates)



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
