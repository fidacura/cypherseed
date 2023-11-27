# cypherseed/cypherseed/wordlists.py

import os

def load_wordlist(name):
    """
    Load words from a specified wordlist.

    :param name: The name of the wordlist file.
    :return: List of words.
    """
    wordlist_path = os.path.join(os.path.dirname(__file__), 'wordlists', f'{name}.txt')
    with open(wordlist_path, 'r') as file:
        return [line.strip() for line in file]
