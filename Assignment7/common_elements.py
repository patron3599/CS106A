"""
File: common_elements.py
------------------------
By: Christopher Patron
Project: CS 106A Assignment 7: Warm-up
Date: 05/24/2022

File to implement a function that is passed two lists and returns a new list
containing those elements that appear in both of the lists passed in.
"""


def common(list1, list2):
    """
    This function is passed two lists and returns a new list containing
    those elements that appear in both of the lists passed in.
    >>> common(['a'], ['a'])
    ['a']
    >>> common(['a', 'b', 'c'], ['x', 'a', 'z', 'c'])
    ['a', 'c']
    >>> common(['a', 'b', 'c'], ['x', 'y', 'z'])
    []
    >>> common(['a', 'a', 'b'], ['a', 'a', 'x'])
    ['a']
    """
    # Initializing new list to be returned
    common_lst = []

    # Finds the maximum length between list1 and list2
    length = max(len(list1), len(list2))

    # If list1 is the longest list
    if length == len(list1):
        for char in list1:
            if char in list1 and char in list2 and char not in common_lst:
                common_lst.append(char)

    # If list2 is the longest list
    elif length == len(list2):
        for char in list2:
            if char in list1 and char in list2 and char not in common_lst:
                common_lst.append(char)

    return common_lst

def main():
    print(common(['a'], ['a']))                             # should print ['a']
    print(common(['a', 'b', 'c'], ['x', 'a', 'z', 'c']))    # should print ['a', 'c']
    print(common(['a', 'b', 'c'], ['x', 'y', 'z']))         # should print []
    print(common(['a', 'a', 'b'], ['a', 'a', 'x']))         # should print ['a']


if __name__ == '__main__':
    main()
