"""
Tests for the cypherseed generator module.
"""

import unittest
import re
from cypherseed.generator import generate_passphrase, generate_multiple_passphrases


class TestGenerator(unittest.TestCase):
    
    def test_generate_passphrase_basic(self):
        """Test basic passphrase generation."""
        passphrase = generate_passphrase('default', 4)
        words = passphrase.split('-')
        self.assertEqual(len(words), 4)
        # each part should be a non-empty string
        for word in words:
            self.assertTrue(len(word) > 0)
    
    def test_generate_passphrase_word_count(self):
        """Test different word counts."""
        for count in [2, 5, 8]:
            passphrase = generate_passphrase('default', count)
            self.assertEqual(len(passphrase.split('-')), count)
    
    def test_generate_passphrase_custom_separator(self):
        """Test custom separator."""
        passphrase = generate_passphrase('default', 3, separator='_')
        self.assertIn('_', passphrase)
        self.assertNotIn('-', passphrase)
        self.assertEqual(len(passphrase.split('_')), 3)
    
    def test_generate_passphrase_include_numbers(self):
        """Test inclusion of numbers."""
        passphrase = generate_passphrase('default', 3, include_numbers=True)
        # should contain at least one digit
        self.assertTrue(re.search(r'\d', passphrase))
    
    def test_generate_passphrase_include_symbols(self):
        """Test inclusion of symbols."""
        passphrase = generate_passphrase('default', 3, include_symbols=True)
        # should contain at least one symbol from our safe set
        self.assertTrue(re.search(r'[!@#$%^&*+=?]', passphrase))
    
    def test_generate_passphrase_random_separators(self):
        """Test random separators functionality."""
        passphrase = generate_passphrase('default', 4, random_separators=True)
        # should not contain regular separator
        self.assertNotIn('-', passphrase)
        # should have exactly 3 separators (between 4 words)
        # each separator should be a digit or symbol
        separators_found = re.findall(r'[0-9!@#$%^&*+=?]', passphrase)
        self.assertGreaterEqual(len(separators_found), 3)
    
    def test_generate_passphrase_word_length_filtering(self):
        """Test word length filtering."""
        passphrase = generate_passphrase('default', 3, min_word_length=5, max_word_length=7)
        words = [word for word in passphrase.split('-') if word.isalpha()]
        for word in words:
            self.assertGreaterEqual(len(word), 5)
            self.assertLessEqual(len(word), 7)
    
    def test_generate_multiple_passphrases(self):
        """Test generating multiple passphrases."""
        passphrases = generate_multiple_passphrases('default', 3, count=5)
        self.assertEqual(len(passphrases), 5)
        # each should be different
        self.assertEqual(len(set(passphrases)), 5)
    
    def test_invalid_word_count(self):
        """Test invalid word count raises ValueError."""
        with self.assertRaises(ValueError):
            generate_passphrase('default', 0)
        with self.assertRaises(ValueError):
            generate_passphrase('default', -1)
    
    def test_invalid_word_lengths(self):
        """Test invalid word length parameters."""
        with self.assertRaises(ValueError):
            generate_passphrase('default', 4, min_word_length=10, max_word_length=5)
    
    def test_nonexistent_wordlist(self):
        """Test that nonexistent wordlist raises FileNotFoundError."""
        with self.assertRaises(FileNotFoundError):
            generate_passphrase('nonexistent_wordlist', 4)


if __name__ == '__main__':
    unittest.main()