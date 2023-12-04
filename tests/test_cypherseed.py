# cypherseed/cypherseed/test_generator.py

import unittest
from cypherseed import generator

class TestCypherseed(unittest.TestCase):

    def test_generate_passphrase_length(self):
        passphrase = generator.generate_passphrase('default', 4)
        self.assertEqual(len(passphrase.split('-')), 4)

    def test_generate_passphrase_inclusion(self):
        passphrase = generator.generate_passphrase('default', 2, include_numbers=True, include_symbols=True)
        self.assertIn('-', passphrase)
        self.assertRegex(passphrase, r'\d')  # Check if contains digits
        self.assertRegex(passphrase, r'[\W_]')  # Check if contains symbols

if __name__ == '__main__':
    unittest.main()
