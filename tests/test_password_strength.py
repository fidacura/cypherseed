"""
Tests for the cypherseed password strength module.
"""

import unittest
import math
from cypherseed.password_strength import (
    calculate_strength,
    calculate_advanced_strength,
    classify_strength,
    time_to_crack_estimate,
    analyse_passphrase_strength
)


class TestPasswordStrength(unittest.TestCase):
    
    def test_calculate_strength_basic(self):
        """Test basic strength calculation."""
        # 4 words from 2048-word list should be 4 * log2(2048) = 44 bits
        expected = 4 * math.log2(2048)
        actual = calculate_strength(4, 2048)
        self.assertAlmostEqual(actual, expected, places=2)
    
    def test_calculate_strength_different_sizes(self):
        """Test strength calculation with different parameters."""
        # test with known values
        strength = calculate_strength(6, 7776)  # eff large wordlist
        expected = 6 * math.log2(7776)
        self.assertAlmostEqual(strength, expected, places=2)
    
    def test_calculate_advanced_strength(self):
        """Test advanced strength calculation with additional elements."""
        base_strength = calculate_strength(4, 2000)
        advanced_strength = calculate_advanced_strength(
            4, 2000, include_numbers=True, include_symbols=True
        )
        # advanced should be higher than base
        self.assertGreater(advanced_strength, base_strength)
    
    def test_classify_strength(self):
        """Test strength classification."""
        self.assertEqual(classify_strength(25), "Very Weak")
        self.assertEqual(classify_strength(40), "Weak")
        self.assertEqual(classify_strength(60), "Fair")
        self.assertEqual(classify_strength(80), "Good")
        self.assertEqual(classify_strength(100), "Strong")
        self.assertEqual(classify_strength(130), "Very Strong")
    
    def test_time_to_crack_estimate(self):
        """Test time to crack estimates."""
        estimate = time_to_crack_estimate(40)  # 40 bits
        self.assertIn("human_readable", estimate)
        self.assertIn("seconds", estimate)
        self.assertGreater(estimate["seconds"], 0)
        
        # very low entropy should be instant
        estimate_low = time_to_crack_estimate(1)
        self.assertIn("second", estimate_low["human_readable"].lower())
    
    def test_analyse_passphrase_strength_comprehensive(self):
        """Test comprehensive passphrase analysis."""
        analysis = analyse_passphrase_strength(5, 7776, include_numbers=True)
        
        # check all expected keys are present
        expected_keys = [
            "entropy_bits", "base_entropy_bits", "additional_entropy_bits",
            "strength_classification", "time_to_crack", "total_combinations",
            "wordlist_size", "word_count", "includes_numbers", "includes_symbols"
        ]
        for key in expected_keys:
            self.assertIn(key, analysis)
        
        # check values make sense
        self.assertEqual(analysis["word_count"], 5)
        self.assertEqual(analysis["wordlist_size"], 7776)
        self.assertTrue(analysis["includes_numbers"])
        self.assertFalse(analysis["includes_symbols"])
        self.assertGreater(analysis["entropy_bits"], analysis["base_entropy_bits"])
    
    def test_invalid_input_word_count(self):
        """Test invalid word count raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_strength(-1, 2048)
        with self.assertRaises(ValueError):
            calculate_strength(0, 2048)
    
    def test_invalid_input_wordlist_size(self):
        """Test invalid wordlist size raises ValueError."""
        with self.assertRaises(ValueError):
            calculate_strength(4, 0)
        with self.assertRaises(ValueError):
            calculate_strength(4, -100)
    
    def test_advanced_strength_invalid_counts(self):
        """Test advanced strength with invalid count parameters."""
        with self.assertRaises(ValueError):
            calculate_advanced_strength(4, 2000, include_numbers=True, number_count=0)
        with self.assertRaises(ValueError):
            calculate_advanced_strength(4, 2000, include_symbols=True, symbol_count=-1)


if __name__ == '__main__':
    unittest.main()