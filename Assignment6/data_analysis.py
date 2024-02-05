"""
File: data_analysis.py
----------------------
By: Christopher Patron
Project: CS 106A Assignment 6: Problem 1
Date: 05/17/2022

This program read in data on cumulative infections of a disease
in different locations, and computes the number of infections
per day at each location.
"""

def load_data(filename):
    """
    The function takes in the name of a datafile (string), which
    contains data on locations and their seven day cumulative number
    of infections.  The function returns a dictionary in which the
    keys are the locations in the data file, and the value associated
    with each key is a list of the (integer) values presenting the
    cumulative number of infections at that location.
    >>> load_data('data/disease1.txt')
    {'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]}
    """

    # Initialize the dictionary
    disease_data = {}

    with open(filename) as file:
        for line in file:
            line = line.strip()
            temp_parts = line.split(',')
            parts = []
            data = []

            # Loop to create the keys
            for index in temp_parts:
                parts.append(index.strip())

            # Loop to create the values
            for i in range(1, len(parts)):
                data.append(int(parts[i]))

            # Creating each key-value pair
            location = parts[0]
            disease_data[location] = data

    return disease_data


def daily_cases(cumulative):
    """
    The function takes in a dictionary of the type produced by the load_data
    function (i.e., keys are locations and values are lists of seven values
    representing cumulative infection numbers).  The function returns a
    dictionary in which the keys are the same locations in the dictionary
    passed in, but the value associated with each key is a list of the
    seven values (integers) presenting the number of new infections each
    day at that location.
    >>> daily_cases({'Test': [1, 2, 3, 4, 4, 4, 4]})
    {'Test': [1, 1, 1, 1, 0, 0, 0]}
    >>> daily_cases({'Evermore': [1, 1, 1, 1, 1, 1, 1], 'Vanguard City': [1, 2, 3, 4, 5, 6, 7], 'Excelsior': [1, 1, 2, 3, 5, 8, 13]})
    {'Evermore': [1, 0, 0, 0, 0, 0, 0], 'Vanguard City': [1, 1, 1, 1, 1, 1, 1], 'Excelsior': [1, 0, 1, 1, 2, 3, 5]}
    """

    # Initialize the dictionary
    infection_data = {}

    for key in cumulative:
        lst = cumulative[key]
        temp_data = []

        # Looping through each value of the original dict and checking conditions
        for i in range(len(lst)):
            if i == 0:
                temp_data.append(lst[i])
            elif lst[i-1] == lst[i]:
                temp_data.append(0)
            elif lst[i-1] < lst[i]:
                temp_data.append(lst[i] - lst[i-1])

        # Creating each key-value pair
        infection_data[key] = temp_data

    return infection_data


def main():
    filename = 'data/disease1.txt'

    data = load_data(filename)
    print(f"Loaded datafile {filename}:")
    print(data)

    print("Daily infections: ")
    print(daily_cases(data))


if __name__ == '__main__':
    main()
