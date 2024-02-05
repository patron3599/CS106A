"""
File: word_guess.py
-------------------
By: Christopher Patron
Project: CS 106A Assignment 5: Problem 2
Date: 05/13/2022

This is an interactive program where the user essentially plays the game
hangman. The user starts out with 8 guesses and if they get one wrong, then
they lose a guess. Otherwise, their progress in determining the word is displayed
after each guess.
"""

import random


LEXICON_FILE = "Lexicon.txt"    # File to read word list from
INITIAL_GUESSES = 8             # Initial number of guesses player starts with


def play_game(secret_word):
    """
    play_game() is passed secret_word from the get_word() function. The meat and
    potatoes of this program is ran in this function. This function also uses the help of
    update_word() which helps keep track of the user's progress.
    """

    # Initializing parameters
    previous_word = ''
    blank_word = ''
    num_guesses = INITIAL_GUESSES
    for char in secret_word:
        blank_word += '-'

    # The game begins at this point
    print('')
    print('The word now looks like this: ' + blank_word)
    print('You have ' + str(num_guesses) + ' guesses left')
    print('')

    while num_guesses >= 0:

        guess = str.upper(input('Type a single letter here, then press enter: '))
        print('')

        # Ensuring that one letter is entered at a time
        if len(guess) > 1:
            print('Guess should only be one character')

        elif guess in secret_word:
            print('That guess is correct.')

            # Calling update_word() to update the user's guessed word
            next_word = update_word(secret_word, previous_word, guess)
            previous_word = next_word
            print('The word now looks like this: ' + next_word)

            # Condition to check if the user has guessed all the letters
            if next_word == secret_word:
                print('Congratulations, the word is: ' + secret_word)
                break

        # Condition if the user guesses incorrectly
        else:
            print('There are no ' + guess + "'s" + ' in the word')
            num_guesses -= 1
            if num_guesses == 0:
                print('Sorry, you lost. The secret word was: ' + secret_word)
                break
            else:
                print('You have ' + str(num_guesses) + ' guesses left')
                print('')


def update_word(secret_word, previous_word, guess):
    """
    update_word() is passed the secret word, the current partial guess, and the guessed
    letter that the user inputted. temp_word is initialized and is used to keep updating
    previous_word until it matches the secret word.
    """
    temp_word = ''

    for char in secret_word:
        if char in previous_word:
            temp_word += char
        elif char == guess:
            temp_word += char
        else:
            temp_word += '-'

    return temp_word


def get_word():
    """
    This function returns a secret word that the player is trying
    to guess in the game.  This function initially has a very small
    list of words that it can select from to make it easier for you
    to write and debug the main game playing program.  In Part II of
    writing this program, you will re-implement this function to
    select a word from a much larger list by reading a list of words
    from the file specified by the constant LEXICON_FILE.
    """

    words = []
    with open(LEXICON_FILE) as file:
        for line in file:
            line = line.strip()
            words.append(line)

    word_index = random.randint(0, len(words))
    secret_word = words[word_index]

    return secret_word


def main():
    """
    To play the game, we first select the secret word for the
    player to guess and then play the game using that secret word.
    """
    secret_word = get_word()
    play_game(secret_word)


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == "__main__":
    main()