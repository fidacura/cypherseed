#!/usr/bin/env python3
import argparse
from cypherseed.generator import generate_passphrase
from cypherseed.password_strength import calculate_strength
from cypherseed.wordlists import load_wordlist

def main():
    parser = argparse.ArgumentParser(description="Generate a high-entropy passphrase.")
    parser.add_argument('word_count', type=int, help='Number of words in the passphrase.')
    parser.add_argument('--wordlist', type=str, default='default', help='Name of the wordlist to use.')
    parser.add_argument('--min-length', type=int, help='Minimum length of each word.')
    parser.add_argument('--max-length', type=int, help='Maximum length of each word.')
    parser.add_argument('--include-numbers', action='store_true', help='Include numbers in the passphrase.')
    parser.add_argument('--include-symbols', action='store_true', help='Include symbols in the passphrase.')

    args = parser.parse_args()

    # Load the wordlist to get its size
    wordlist = load_wordlist(args.wordlist)
    wordlist_size = len(wordlist)

    passphrase = generate_passphrase(
        wordlist_name=args.wordlist,
        word_count=args.word_count,
        min_word_length=args.min_length,
        max_word_length=args.max_length,
        include_numbers=args.include_numbers,
        include_symbols=args.include_symbols
    )

    # Calculate the strength of the passphrase
    strength = calculate_strength(args.word_count, wordlist_size)

    print(f"Generated Passphrase: {passphrase}")
    print(f"Passphrase Strength: {strength:.2f} bits")

if __name__ == '__main__':
    main()
