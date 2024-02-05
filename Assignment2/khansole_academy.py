"""
File: khansole_academy.py
-------------------------
By: Christopher Patron
Project: CS106A Assignment 2: Problem 2.A

This function tests your arithmetic skills! Answer 3 questions correctly in a row to
successfully execute this program.

Note: An extension was implemented into this program to also subtract, multiply, and
divide the two values. It still meets the minimum requirements as prescribed by the
assignemnt.
"""

import random

def main():
    num_correct = 0

    # This flag determines what type of arithmetic will be computed
    flag = what_operation()
    while num_correct < 3:
        num_correct = ask_question(num_correct, flag)
    congrats(flag)

    pass

"""
Helper Functions
"""

# what_operation() asks the user what type of operation they want to practice
def what_operation():
    print('What operation would you like to perform?')
    print('')
    print('1 = addition')
    print('2 = subtraction')
    print('3 = multiplication')
    print('4 = division')
    flag = int(input('Enter number: '))
    return flag

"""
ask_question() provides the user with a mathematical expression made up of 2 random values. Upon receiving 
these values, they will passed to check_num_correct for verification.
"""
def ask_question(num_correct, flag):
    if flag == 1:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        print('What is ' + str(x) + '+' + str(y)+'?')
        user_ans = int(input('Your answer: '))
        ans = x + y
        num_correct = check_num_correct(ans, user_ans, num_correct)
        return num_correct

    elif flag == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
        print('What is ' + str(x) + '-' + str(y)+'?')
        user_ans = int(input('Your answer: '))
        ans = x - y
        num_correct = check_num_correct(ans, user_ans, num_correct)
        return num_correct

    elif flag == 3:
        x = random.randint(10, 99)
        y = random.randint(1, 9)
        print('What is ' + str(x) + 'x' + str(y)+'?')
        user_ans = int(input('Your answer: '))
        ans = x * y
        num_correct = check_num_correct(ans, user_ans, num_correct)
        return num_correct

    elif flag == 4:
        x = random.randint(10, 99)
        y = random.randint(1, 9)
        print('What is ' + str(x) + '/' + str(y)+'?')
        user_ans = int(input('Your answer: '))
        ans = x / y
        num_correct = check_num_correct(ans, user_ans, num_correct)
        return num_correct


""""
check_num_correct() receives the parameters from ask_questions and verifies the users values. If the user is 
correct, they will receive a correct answer. If they are incorrect, a correct answer will be deducted.
"""
def check_num_correct(ans, user_ans,num_correct):
    if ans == user_ans:
        # Creates an index to keep track of the user's correct answers
        num_correct += 1
        print('Correct! You have gotten ' + str(num_correct) + ' correct in a row')
        return num_correct
    else:
        num_correct -= 1
        # This condition is added to ensure the user does not get "negative" correct answers
        if num_correct < 0:
            num_correct = 0
            print('Incorrect. The expected answer is: ' + str(ans) + '. You now have ' + str(
                num_correct) + ' correct in a row')
            return num_correct
        else:
            print('Incorrect. The expected answer is: ' + str(ans) + '. You now have ' + str(
                num_correct) + ' correct in a row')
            return num_correct

# congrats() lets the user know that they have successfully answered 3 questions in a row
def congrats(flag):
    print('')
    if flag == 1:
        print('Congratulations! You mastered addition')
    if flag == 2:
        print('Congratulations! You mastered subtraction')
    if flag == 3:
        print('Congratulations! You mastered multiplication')
    if flag == 4:
        print('Congratulations! You mastered division')

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
