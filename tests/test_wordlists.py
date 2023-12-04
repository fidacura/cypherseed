# cypherseed/cypherseed/test_wordlists.py

import unittest
import os
from cypherseed import wordlists

class TestWordlists(unittest.TestCase):

    def test_load_wordlist(self):
        words = wordlists.load_wordlist('default')
        self.assertIsInstance(words, list)
        self.assertTrue(len(words) > 0)

    def test_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            wordlists.load_wordlist('nonexistent')

if __name__ == '__main__':
    unittest.main()
