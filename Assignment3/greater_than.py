"""
File: greater_than.py
---------------------
By: Christopher Patron
Project: CS 106A Assignment 3: Problem 1.A
Date: 04/18/2022

This program gives you practice working with lists in Python. We are
provided with 4 lists and a threshold. This program returns a copy of
the new list but the elements in that list are greater than the
threshold value.
"""


def greater_than(threshold, num_list):

    """
    This function is passed an integer (threshold) and list of integers (num_list)
    and should return a list containing only those numbers from num_list that
    have a value strictly greater than threshold.
    >>> greater_than(6, [20, 6, 12, -3, 14])
    [20, 12, 14]
    >>> greater_than(15, [16])
    [16]
    >>> greater_than(10, [1, 2, 3, 4])
    []
    >>> greater_than(0, [])
    []
    """

    # We must initialize this list since it was not created in the main function
    result_list = []
    for i in range(len(num_list)):
        elem = num_list[i]
        if elem > threshold:
            result_list.append(elem)
    return result_list



def main():
    # Lists to be passed and analyzed by greater_than
    list1 = [20, 6, 12, -3, 14]
    result_list = greater_than(6, list1)
    print(result_list)      # should print [20, 12, 14]

    list2 = [16]
    result_list = greater_than(15, list2)
    print(result_list)      # should print [16]

    list3 = [1, 2, 3, 4]
    result_list = greater_than(10, list3)
    print(result_list)      # should print []

    list4 = []
    result_list = greater_than(0, list4)
    print(result_list)      # should print []


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
