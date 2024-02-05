"""
File: moon_weight.py
--------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 1.E
Date: 04/15/2022

Ever wonder how much you weigh on the moon? Well good news! this
function takes your weight on earth and tells you how much you would
weigh on the moon.
"""

def main():
    weight = float(input('Please input your weight: '))
    weight_on_moon(weight)

    pass

"""
Helper Functions
"""

"""
weight_on_moon() takes the user inputted weight and then calculates their weight if 
they were to be on the moon. It also has a flag in place to stop the program if a 
negative weight is inputted.
"""
def weight_on_moon(weight):
    if weight >= 0:
        new_weight = weight * 0.165
        print('Your weight on the moon is: ' + str(new_weight))
    else:
        print('Sorry, you can not have a negative weight.')


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
