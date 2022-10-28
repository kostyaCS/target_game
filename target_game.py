from typing import List
import random
import string
import sys


def generate_grid():
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    alphabet = list(string.ascii_uppercase)
    grid = []
    for _ in range(3):
        current = []
        while len(current) != 3:
            choice = random.choice(alphabet)
            current.append(choice)
            alphabet.remove(choice)
        grid.append(current)
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """




def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    users_list_of_words = []
    while True:
        word = input('Введіть слово: ')
        if word == '':
            break
        if word not in users_list_of_words:
            users_list_of_words.append(word)
        else:
            continue
    return users_list_of_words


def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass
