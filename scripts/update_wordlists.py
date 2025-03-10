# cypherseed/scripts/update_wordlists.py

import argparse
import os
import requests

# download wordlist
def download_wordlist(url, destination):
    """
    Download a wordlist from a given URL and save it to the specified destination.

    :param url: URL of the wordlist to download.
    :param destination: Path to save the downloaded wordlist.
    """
    response = requests.get(url)
    with open(destination, 'w') as file:
        file.write(response.text)

# filter wordlist
def filter_wordlist(source, destination, criteria):
    """
    Filter a wordlist based on specified criteria and save the filtered list.

    :param source: Path of the source wordlist.
    :param destination: Path to save the filtered wordlist.
    :param criteria: Function to determine if a word meets the criteria.
    """
    with open(source, 'r') as src, open(destination, 'w') as dest:
        for word in src:
            if criteria(word.strip()):
                dest.write(word)

# filter wordlist
def criteria_example(word):
    """
    Example criteria function for filtering words.

    :param word: A word from the wordlist.
    :return: True if the word meets the criteria, False otherwise.
    """
    # define criteria here. e.g.:
    return len(word) >= 5 and len(word) <= 8

def main():
    # args
    parser = argparse.ArgumentParser(description='Update and manage wordlists for cypherseed.')
    parser.add_argument('--download', metavar='URL', type=str, help='URL to download a new wordlist.')
    parser.add_argument('--source', metavar='SOURCE', type=str, help='Source wordlist file path for filtering.')
    parser.add_argument('--destination', metavar='DEST', type=str, help='Destination file path for the updated wordlist.')
    args = parser.parse_args()

    # download wordlist
    if args.download:
        # visual output
        print(f"Downloading wordlist from {args.download}")
        # download wordlist
        destination = args.destination or 'downloaded_wordlist.txt'
        download_wordlist(args.download, destination)
        # visual output
        print(f"Wordlist downloaded to {destination}")

    # filter wordlist
    if args.source and args.destination:
        # visual output
        print(f"Filtering wordlist from {args.source} to {args.destination}")
        # filter wordlist
        filter_wordlist(args.source, args.destination, criteria_example)
        # visual output
        print(f"Filtered wordlist saved to {args.destination}")

if __name__ == '__main__':
    main()
