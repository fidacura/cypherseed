#!/usr/bin/env python3
# cypherseed/scripts/calculate_strength.py

from cypherseed.password_strength import calculate_strength
import argparse

def main():
    parser = argparse.ArgumentParser(description='Calculate passphrase strength.')
    parser.add_argument('word_count', type=int, help='Number of words in the passphrase.')
    parser.add_argument('wordlist_size', type=int, help='Number of words in the wordlist.')
    args = parser.parse_args()

    strength = calculate_strength(args.word_count, args.wordlist_size)
    print(f'Passphrase Strength: {strength:.2f} bits')

if __name__ == '__main__':
    main()