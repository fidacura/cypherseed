# cypherseed/cypherseed/generator.py

from cypherseed.wordlists import load_wordlist
from secrets import choice
import string
import random

def generate_passphrase(wordlist_name, word_count, separator='-', min_word_length=None, max_word_length=None, include_numbers=False, include_symbols=False):
    """
    Generate a high-entropy passphrase.

    :param wordlist_name: Name of the wordlist to use.
    :param word_count: Number of words in the passphrase.
    :param separator: Separator between words in the passphrase.
    :param min_word_length: Minimum length of each word.
    :param max_word_length: Maximum length of each word.
    :param include_numbers: Include numbers in the passphrase.
    :param include_symbols: Include symbols in the passphrase.
    :return: Generated passphrase.
    """
    words = load_wordlist(wordlist_name)

    # Filter words based on length criteria
    if min_word_length or max_word_length:
        words = [word for word in words if (min_word_length is None or len(word) >= min_word_length) and (max_word_length is None or len(word) <= max_word_length)]
    
    if not words:
        raise ValueError("No words in the wordlist meet the specified length criteria.")
    
    # Generate passphrase
    passphrase = separator.join(choice(words) for _ in range(word_count))

    # Optionally include numbers and symbols
    if include_numbers:
        numbers = string.digits
        passphrase += separator + choice(numbers)
    if include_symbols:
        symbols = string.punctuation
        passphrase += separator + choice(symbols)

    return passphrase



