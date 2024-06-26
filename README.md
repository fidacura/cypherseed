# cypherseed

Cypherseed is a simple high-entropy passphrase creation tool that uses mulitple wordlists to generate secure and memorable passphrases.

## Features

- Generate high-entropy passphrases
- Customizable word count, word length, and inclusion of numbers/symbols
- Supports multiple wordlists
- Calculates passphrase strength in bits
- Easily update and filter wordlists

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cypherseed.git
   cd cypherseed
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Generate a Passphrase

To generate a passphrase, run:

```bash
./cypherseed.py <word_count> [--wordlist <wordlist_name>] [--min-length <min_length>] [--max-length <max_length>] [--include-numbers] [--include-symbols]
```

    <word_count>: Number of words in the passphrase (required)
    --wordlist: Name of the wordlist to use (default: default)
    --min-length: Minimum length of each word
    --max-length: Maximum length of each word
    --include-numbers: Include numbers in the passphrase
    --include-symbols: Include symbols in the passphrase

Example:

```bash
./cypherseed.py 7 --wordlist eff_short_wordlist.txt --min-length 5 --max-length 8 --include-numbers --include-symbols
```

### Calculate Passphrase

To calculate the strength of a passphrase, use:

```bash
./scripts/calculate_strength.py <word_count> <wordlist_size>
```

- <word_count>: Number of words in the passphrase (required)
- <wordlist_size>: Number of words in the wordlist (required)

Example:

```bash
./scripts/calculate_strength.py 4 5000
```

### Update and Manage Wordlists

To download and filter wordlists, use:

```bash
./scripts/update_wordlists.py [--download <URL>] [--source <source_path>] [--destination <destination_path>]
```

- --download: URL to download a new wordlist
- --source: Source wordlist file path for filtering
- --destination: Destination file path for the updated wordlist

Example:

```bash
./scripts/update_wordlists.py --download https://example.com/wordlist.txt --destination cypherseed/wordlists/new_wordlist.txt
./scripts/update_wordlists.py --source cypherseed/wordlists/english.txt --destination cypherseed/wordlists/filtered_wordlist.txt
```
