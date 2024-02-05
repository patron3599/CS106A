"""
File: encoded_string.py
-----------------------
By: Christopher Patron
Project: CS 106A Assignment 4: Problem 1.B
Date: 04/28/2022

This program expands strings encoded with run-length encoding.
"""


def expand_encoded_string(encoded):
    """
    This function is passed a run-length encoded string and
    returns the expanded version of that string.
    >>> expand_encoded_string('B4')
    'BBBB'
    >>> expand_encoded_string('m1e2t1')
    'meet'
    >>> expand_encoded_string('B1o2k2e2p1e1r1!3')
    'Bookkeeper!!!'
    """
    # Initializing the result string
    result = ""

    # Outer loop is set to skip every other element which is the desired length of the initial string
    for i in range(0, len(encoded)-1, 2):
        char = encoded[i]
        num_char = 1 * int(encoded[i+1])

        # This loop concatenates the desired number of letters to the original one
        for j in range(num_char-1):
            char += encoded[i]

        result = result + char

    return result



def main():
    result = expand_encoded_string('B4')
    print(result)      # should print: BBBB

    result = expand_encoded_string('m1e2t1')
    print(result)      # should print: meet

    result = expand_encoded_string('B1o2k2e2p1e1r1!3')
    print(result)      # should print: Bookkeeper!!!


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
