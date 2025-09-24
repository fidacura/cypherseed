"""
Tests for the cypherseed wordlists module.
"""

import unittest
from cypherseed.wordlists import (
    load_wordlist,
    get_available_wordlists,
    get_wordlist_info
)


class TestWordlists(unittest.TestCase):
    
    def test_load_wordlist_default(self):
        """Test loading the default wordlist."""
        words = load_wordlist('default')
        self.assertIsInstance(words, list)
        self.assertGreater(len(words), 1000)  # should be substantial
        # all words should be non-empty strings
        for word in words[:10]:  # check first 10
            self.assertIsInstance(word, str)
            self.assertGreater(len(word), 0)
    
    def test_load_wordlist_with_extension(self):
        """Test loading wordlist with .txt extension."""
        words_without_ext = load_wordlist('default')
        words_with_ext = load_wordlist('default.txt')
        self.assertEqual(words_without_ext, words_with_ext)
    
    def test_load_different_wordlists(self):
        """Test loading different available wordlists."""
        available = get_available_wordlists()
        self.assertGreater(len(available), 0)
        
        # test loading each available wordlist
        for wordlist_name in available[:2]:  # test first 2 to avoid long test times
            words = load_wordlist(wordlist_name)
            self.assertIsInstance(words, list)
            self.assertGreater(len(words), 0)
    
    def test_get_available_wordlists(self):
        """Test getting list of available wordlists."""
        wordlists = get_available_wordlists()
        self.assertIsInstance(wordlists, list)
        self.assertGreater(len(wordlists), 0)
        
        # should include our known wordlists
        known_wordlists = ['default', 'eff_large_wordlist', 'eff_short_wordlist']
        for known in known_wordlists:
            self.assertIn(known, wordlists)
    
    def test_get_wordlist_info(self):
        """Test getting wordlist information."""
        info = get_wordlist_info('default')
        
        # check expected keys
        expected_keys = ['name', 'size', 'min_word_length', 'max_word_length', 'avg_word_length']
        for key in expected_keys:
            self.assertIn(key, info)
        
        # check values make sense
        self.assertEqual(info['name'], 'default')
        self.assertGreater(info['size'], 0)
        self.assertGreater(info['min_word_length'], 0)
        self.assertGreaterEqual(info['max_word_length'], info['min_word_length'])
        self.assertGreater(info['avg_word_length'], 0)
    
    def test_load_nonexistent_wordlist(self):
        """Test that loading nonexistent wordlist raises FileNotFoundError."""
        with self.assertRaises(FileNotFoundError) as context:
            load_wordlist('definitely_nonexistent_wordlist_12345')
        
        # error message should mention available wordlists
        self.assertIn('Available wordlists:', str(context.exception))
    
    def test_wordlist_content_quality(self):
        """Test that wordlist content is reasonable quality."""
        words = load_wordlist('default')
        
        # should have reasonable number of words
        self.assertGreater(len(words), 1000)
        
        # words should not be too short or too long
        word_lengths = [len(word) for word in words]
        avg_length = sum(word_lengths) / len(word_lengths)
        self.assertGreater(avg_length, 2)  # average should be reasonable
        self.assertLess(avg_length, 15)    # but not too long
        
        # should not have obvious empty entries
        empty_words = [word for word in words if not word.strip()]
        self.assertEqual(len(empty_words), 0)


if __name__ == '__main__':
    unittest.main()