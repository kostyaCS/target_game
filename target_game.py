from math import isclose
from typing import List
import random
import string


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
            current.append(random.choice(alphabet))
        grid.append(current)
    return grid


def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    >>> get_words('/Users/kostyantin/UCUpython/target_game/en.txt', ['w', 'u', 'm', 'r', 'o', 'v', 'k', 'i', 'f'])
    ['fork', 'form', 'forum', 'four', 'fowk', 'from', 'frow', 'irok', 'komi', 'kori', 'miro', 'moki', 'ovum', 'work', 'worm', 'wouf']
    """
    central_letter = letters[4]
    list_of_all_words = []
    list_of_suited_words = []
    with open(f, 'r', encoding='utf-8') as file_with_words:
        for line in file_with_words:
            list_of_all_words.append(line.strip().lower())
    for word in list_of_all_words:
        if len(word) > 3 and central_letter in word:
            for letter in word:
                if not letter in letters or word.count(letter) > letters.count(letter):
                    break
            else:
                if word not in list_of_suited_words:
                    list_of_suited_words.append(word)
    return list_of_suited_words



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
