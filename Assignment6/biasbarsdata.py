"""
File: biasbarsdata.py
------------------
By: Christopher Patron
Project: CS 106A Assignment 6: Problem 2
Date: 05/19/2022

This file reads the large data file containing all the ratings and creates
a word_data dictionary for every single letter. For each word, the dictionary
also tracks how many times it was referred to a man or woman, and also the
the rating associated with that word.

"""

KEY_WOMEN = "W"
KEY_MEN = "M"


def convert_rating_to_index(rating):
    """
    Converts the specified numerical rating into a "bucket"
    index for the three groups of review buckets (low reviews, 
    medium reviews, and high reviews). The rules for this 
    conversion are specified in the assignment handout.

    Input:
        rating (float): The numerical rating associated with 
                        a review

    Output: 
        bucket_index (int): The index of the "bucket" into which 
                          the review falls

    >>> convert_rating_to_index(1.0)
    0
    >>> convert_rating_to_index(1.5)
    0
    >>> convert_rating_to_index(3.0)
    1
    >>> convert_rating_to_index(3.5)
    1
    >>> convert_rating_to_index(4.0)
    2
    >>> convert_rating_to_index(5.5)
    2
    """

    # Defining the boundaries of the reviews
    low_reviews = rating < 2.5
    medium_reviews = 2.5 <= rating <= 3.5
    high_reviews = rating > 2.5

    # Checking conditions to return the proper bucket index
    if low_reviews is True:
        bucket_index = 0
        return bucket_index

    elif medium_reviews is True:
        bucket_index = 1
        return bucket_index

    elif high_reviews is True:
        bucket_index = 2
        return bucket_index


def add_data_for_word(word_data, word, gender, rating):
    """
    Updates the word_data dictionary to log an occurence of the
    specified word in a review with the given rating about a professor
    of the specified gender.

    Input:
        word_data (dictionary): dict holding word frequency data
        word (string): the word for which frequency data is being updated
        gender (string): the gender label for the specified comment in which 
                         this word was seen
        rating (float): the numerical rating of the review in which this word
                         was seen

    >>> word_data = {}
    >>> add_data_for_word(word_data, "good", "M", 5.0)
    >>> word_data
    {'good': {'W': [0, 0, 0], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "good", "W", 4.5)
    >>> word_data
    {'good': {'W': [0, 0, 1], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "good", "W", 3.0)
    >>> word_data
    {'good': {'W': [0, 1, 1], 'M': [0, 0, 1]}}
    >>> add_data_for_word(word_data, "bad", "M", 1.5)
    >>> word_data
    {'good': {'W': [0, 1, 1], 'M': [0, 0, 1]}, 'bad': {'W': [0, 0, 0], 'M': [1, 0, 0]}}
    """

    # Initializing the default dict for each time the function is called
    default_dict = {KEY_WOMEN: [0, 0, 0], KEY_MEN: [0, 0, 0]}

    # Conditions for if word is not in dictionary
    if word not in word_data and gender == KEY_WOMEN:
        word_data[word] = default_dict
        bucket_index = convert_rating_to_index(rating)
        word_data[word][KEY_WOMEN][bucket_index] += 1

    elif word not in word_data and gender == KEY_MEN:
        word_data[word] = default_dict
        bucket_index = convert_rating_to_index(rating)
        word_data[word][KEY_MEN][bucket_index] += 1

    # Conditions for if word is in dictionary
    elif word in word_data and gender == KEY_WOMEN:
        bucket_index = convert_rating_to_index(rating)
        word_data[word][KEY_WOMEN][bucket_index] += 1

    elif word in word_data and gender == KEY_MEN:
        bucket_index = convert_rating_to_index(rating)
        word_data[word][KEY_MEN][bucket_index] += 1


def read_file(filename):
    """
    Reads the information from the specified file and builds a new 
    word_data dictionary with the data found in the file. Returns the
    newly created dictionary. 

    Input:
        filename (str): name of the file holding professor review data

    >>> read_file('data/small-one.txt')
    {'okay': {'W': [0, 0, 0], 'M': [0, 1, 0]}, 'best': {'W': [0, 0, 1], 'M': [0, 0, 0]}}
    >>> read_file('data/small-two.txt')
    {'awesome': {'W': [0, 0, 2], 'M': [0, 0, 1]}, 'teacher': {'W': [0, 0, 1], 'M': [0, 0, 1]}, 'class': {'W': [0, 0, 1], 'M': [0, 0, 0]}}
    >>> read_file('data/small-three.txt')
    {'average': {'W': [0, 0, 0], 'M': [1, 3, 0]}, 'best': {'W': [0, 0, 3], 'M': [1, 0, 0]}, 'not': {'W': [0, 0, 0], 'M': [2, 0, 0]}}
    """

    # Initializing the word_data dict
    word_data = {}

    with open(filename) as file:
        next(file)
        for line in file:
            line = line.strip()
            parts = line.split(',')
            rating = float(parts[0])
            reviews = parts[2].split() # Creating a list of words for each review to be sorted
            gender = parts[1]

            for word in reviews:
                add_data_for_word(word_data, word, gender, rating)

    return word_data


def search_words(word_data, target):
    """
    Given a word_data dictionary that stores word frequency information and a target string,
    returns a list of all words in the dictionary that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        word_data (dictionary): a dictionary containing word frequency data
        target (str): a string to look for in the names contained within word_data

    Returns:
        matching_words (List[str]): a list of all words from word_data that contain
                                    the target string
    """

    # Initializing the string list
    matching_words = []

    for key in word_data:
        if target.upper() in key:
            matching_words.append(key)

        elif target.lower() in key:
            matching_words.append(key)

    return matching_words


def print_words(word_data):
    """
    (This function is provided for you)
    Given a word_data dictionary, print out all its data, one word per line.
    The words are printed in alphabetical order,
    with the corresponding frequency data displayed in order
    of associated review quality for each gender.

    This code makes use of the sorted function, which is given as input a 
    list of elements and returns a list containing the same elements sorted in
    increasing order. For strings, "increasing" order maps to alphabetical 
    ordering.

    Input:
        word_data (dictionary): a dictionary containing word frequency data organized by gender and rating quality
    """
    for key, value in sorted(word_data.items()):
        print(key, end=" ")
        for gender, counts in sorted(value.items()):
            print(gender, counts, end=" ")
        print("")


def main():

    # (This function is provided for you)
    import sys
    args = sys.argv[1:]

    if len(args) == 0:
        return
    # Two command line forms
    # 1. data_file
    # 2. -search target data_file

    # Assume no search, so filename to read
    # is the first argument
    filename = args[0]

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filename = args[2]  # Update filename to skip first 2 args

    # Read in the data from the file name
    word_data = read_file(filename)

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_words(word_data, target)
        for word in search_results:
            print(word)
    else:
        print_words(word_data)


if __name__ == '__main__':
    main()
