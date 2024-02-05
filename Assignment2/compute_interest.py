"""
File: compute_interest.py
-------------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 2.B
Date: 04/15/2022

This program computes the monthly interest accrued on a balance provided by the user. It
returns the account value at each month for the desired time inputted by the user. It also
offers the user the option to analyze their current option with a different interest rate
after each execution of the program.
"""

def main():
    # Initializing the parameters to be provided by the user and passed to the functions
    acc_balance, starting_year, starting_month, ending_year, ending_month, = initialize_parameters()
    # Before the program starts, check that a proper timeline has been received 
    check_dates_correct(starting_year, ending_year, starting_month, ending_month)
    interest_rate = float(input("Please enter the interest rate as a decimal: "))

    while interest_rate != 0:
        # This conditions is activated if the timeline is less than a year
        if starting_year == ending_year:
            check_single_year(acc_balance, starting_year, starting_month, ending_month, interest_rate)
            interest_rate = float(input("Please enter the interest rate as a decimal: "))

        else:
            # Body of code to be run if the condition above is not met
            acc_balance1 = first_year(acc_balance, starting_year, starting_month, interest_rate)
            acc_balance2 = middle_years(acc_balance1, starting_year, ending_year, ending_month, interest_rate)
            last_year(acc_balance2, ending_year, ending_month, interest_rate)
            interest_rate = float(input("Please enter the interest rate as a decimal: "))

    pass

"""
Helper Functions
"""

# initialize_parameters() retrieves the necessary parameters from the user to be used in this program
def initialize_parameters():
    acc_balance = float(input("Please enter the account balance: "))
    starting_year = int(input("Please enter the starting year: "))
    starting_month = int(input("Please enter the starting month: "))
    ending_year = int(input("Please enter the ending year: "))
    ending_month = int(input("Please enter the ending month: "))

    return acc_balance, starting_year, starting_month, ending_year, ending_month

"""
check_dates_correct() is a pre-condition check to ensure that the program is executed for a real timeline. 
If it is activated, it ends the program 
"""
def check_dates_correct(starting_year, ending_year,starting_month,ending_month):
    if starting_year > ending_year:
        print("Starting date needs to be before ending date")
        quit()
    elif starting_year == ending_year:
        if starting_month >= ending_month:
            print("Starting date needs to be before ending date")
            quit()


"""
check_single_year() is a pre-condition check that is activated if the user were to provide a timeline that 
was only for a single year. 
"""
def check_single_year(acc_balance, starting_year, starting_month, ending_month, interest_rate):
    num_months = ending_month - starting_month
    for i in range(num_months + 1):
        # This is done since the first month will be the original account balance
        if i == 0:
            acc_balance = acc_balance
            print('Year ' + str(starting_year) + ',' + ' month ' + str(i + starting_month) + ' balance: ' + str(
                acc_balance))
        # Interest is now being added to the account
        else:
            acc_balance = acc_balance + acc_balance * interest_rate
            print('Year ' + str(starting_year) + ',' + ' month ' + str(i + starting_month) + ' balance: ' + str(
                acc_balance))

"""
first_year() calculates and displays the monthly accrued interest for the starting year that was provided by the 
user. It then returns the value of the account balance at the end of the year which will be passed to either 
middle_years or last_year. 
"""
def first_year(acc_balance, starting_year, starting_month, interest_rate):
    num_months = 12-starting_month
    for i in range(num_months+1):
        # This is done since the first month will be the original account balance
        if i == 0:
            acc_balance = acc_balance
            print('Year ' + str(starting_year) + ',' + ' month ' + str(i + starting_month) + ' balance: ' + str(
                acc_balance))
        # Interest is now being added to the account
        else:
            acc_balance = acc_balance + acc_balance*interest_rate
            print('Year ' + str(starting_year) + ',' + ' month ' + str(i + starting_month) + ' balance: ' + str(
                acc_balance))
    return acc_balance

"""
middle_years() calculates and displays the monthly accrued interest for the time in between the starting year
and ending year that was provided by the user, if there is any. If not it will call last_year and continue 
the program. If activated, it returns the value of the account balance at the end of the year which will 
be passed to last_year. 
"""
def middle_years(acc_balance, starting_year, ending_year, ending_month, interest_rate):
    num_years = ending_year - starting_year
    # If there are no middle years, then the program continues to the last year
    if num_years == 0:
        last_year(acc_balance, ending_year, ending_month, interest_rate)
    else:
        month = 1
        # Looping through the each month for x number of middle years
        for i in range(num_years - 1):
            for j in range(12):
                acc_balance = acc_balance + acc_balance * interest_rate
                print('Year ' + str(starting_year + i + 1) + ',' + ' month ' + str(j + month) + ' balance: ' + str(
                    acc_balance))
    return acc_balance

"""
last_years() and displays the monthly accrued interest for the ending year that was provided by the 
user. It does not return the account balance to the main function.
"""
def last_year(acc_balance, ending_year, ending_month, interest_rate):
    for i in range(ending_month):
        acc_balance = acc_balance + acc_balance*interest_rate
        print('Year ' + str(ending_year) + ',' + ' month ' + str(i + 1) + ' balance: ' + str(acc_balance))
    print('')
    return acc_balance


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
