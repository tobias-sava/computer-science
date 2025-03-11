# Problem Set 2, hangman.py
# Name: Tobias Sava
# Collaborators: None
# Date: 11/03/2025
# Time spent:

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open('words', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(" ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    if secret_word in letters_guessed:
        return True
    
    return False

def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    missing = ''
    
    for letter in secret_word:
        if letter in letters_guessed:
            missing = letter + missing
        if letter not in letters_guessed:
            missing = '*' + missing
        
        return missing

def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
    alphabet = string.ascii_lowercase
    
    available_letters = [letter for letter in alphabet if letter not in letters_guessed]
    
    return ''.join(available_letters)

def hangman(secret_word, with_help):
    secret_word = secret_word.lower()
    letters_guessed = []
    remaining_guesses = 10
    
    print(f"Welcome to the game Hangman! The secret word contains {len(secret_word)} letters.")
    
    while remaining_guesses > 0:
        print(f"\nYou have {remaining_guesses} guesses left.")
        print("Available letters:", get_available_letters(letters_guessed))
        
        guess = input("Please guess a letter: ").lower()
        
        if guess == "!":
            if with_help and remaining_guesses >= 3:
                remaining_guesses -= 3
                for letter in secret_word:
                    if letter not in letters_guessed:
                        letters_guessed.append(letter)
                        print(f"One of the letters in the word is: {letter}")
                        break
            else:
                print("Sorry, you don't have enough guesses left to get help.")
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue
        
        if guess in letters_guessed:
            print(f"You've already guessed the letter {guess}.")
            continue
        
        letters_guessed.append(guess)
        
        if guess in secret_word:
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
        else:
            print(f"Oops! That letter is not in the word.")
            if guess in "aeiou":
                remaining_guesses -= 2
            else:
                remaining_guesses -= 1
        
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            break
    else:
        print(f"Sorry, you've run out of guesses. The word was {secret_word}.")




# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    secret_word = choose_word(wordlist)
    with_help = False
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass

 