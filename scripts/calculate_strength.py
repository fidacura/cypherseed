# cypherseed/scripts/calculate_strength.py

from cypherseed.password_strength import calculate_strength
import argparse

def main():
    # args
    parser = argparse.ArgumentParser(description='Calculate passphrase strength.')
    parser.add_argument('word_count', type=int, help='Number of words in the passphrase.')
    parser.add_argument('wordlist_size', type=int, help='Number of words in the wordlist.')
    args = parser.parse_args()

    # calculate strength
    strength = calculate_strength(args.word_count, args.wordlist_size)
    # visual output
    print(f'Passphrase Strength: {strength:.2f} bits')

if __name__ == '__main__':
    main()