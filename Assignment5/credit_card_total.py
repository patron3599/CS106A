"""
File: credit_card_total.py
--------------------------
By: Christopher Patron
Project: CS 106A Assignment 5: Problem 1
Date: 05/13/2022

This program totals up a credit card bill based on
how much was spent at each store on the bill.
"""

# Loading the required bill
INPUT_FILE = 'bill1.txt'


def main():
    bill_dict = load_bill()
    calculate_bill(bill_dict)

"""
HELPER FUNCTIONS 
"""

def load_bill():
    """"
    load_bill() is called from the main function and opens the bill file so that it can be
    processed. It creates a dictionary from the file in which the stores are the keys and
    their expense are the values. It also calls the helper function clean_up().
    """
    bill_dict = {}
    with open(INPUT_FILE) as file:
        for line in file:
            line = line.strip()

            # clean_up() is called and is passed the line from each file
            store, cost = clean_up(line)
            key = store
            value = cost

            if key not in bill_dict:
                bill_dict[key] = [value]
            else:
                bill_dict[key].append(value)

    return bill_dict


def clean_up(line):
    """"
    clean_up() is passed the stipped line from load_bill() and combs through the list
    to find the store and the cost incurred at it. It then returns the store (string) and
    cost (int) back to load_bill().
    """

    # Finding the cost value in the file line
    start_cost = line.find('$') + 1
    cost = int(line[start_cost::])

    # Finding the store name in the file line
    temp_end = 0
    start_store = line.find('[', temp_end) + 1
    end = line.find(']', start_store)
    store = line[start_store:end]

    return store, cost


def calculate_bill(bill_dict):
    """"
    calculate_bill() is passed the bill dictionary that was created in load_bill(). It simply goes
    through each key in the dictionary and prints both the dictionary's key and value to the console.
    """

    for key in bill_dict.keys():
        print(key + ':' + ' $' + str(sum(bill_dict[key])))



# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
