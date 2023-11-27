# cypherseed/cypherseed/password_strength.py

import math

def calculate_strength(word_count, wordlist_size):
    """
    Calculate the strength of a passphrase.

    :param word_count: Number of words in the passphrase.
    :param wordlist_size: Number of words in the wordlist.
    :return: Entropy of the passphrase.
    """
    return word_count * math.log2(wordlist_size)
