# cypherseed/cypherseed/password_strength.py

import math
import argparse

# calculate strength
def calculate_strength(word_count, wordlist_size):
    """
    Calculate the strength of a passphrase based on its entropy.

    Entropy is calculated using the formula: entropy = word_count * log2(wordlist_size)

    :param word_count: Number of words in the passphrase.
    :param wordlist_size: Number of words in the wordlist.
    :return: Entropy of the passphrase in bits.
    """
    # error mngmt
    if wordlist_size <= 0:
        raise ValueError("Wordlist size must be greater than 0.")
    
    # error mngmt
    if word_count <= 0:
        raise ValueError("Word count must be greater than 0.")

    # password strength
    return word_count * math.log2(wordlist_size)


def main():
    # args
    parser = argparse.ArgumentParser(description='Calculate the strength of a passphrase.')
    parser.add_argument('word_count', type=int, help='Number of words in the passphrase.')
    parser.add_argument('wordlist_size', type=int, help='Number of words in the wordlist.')
    args = parser.parse_args()

    # calculate strength
    strength = calculate_strength(args.word_count, args.wordlist_size)
    print(f'Passphrase Strength: {strength:.2f} bits')

if __name__ == '__main__':
    main()