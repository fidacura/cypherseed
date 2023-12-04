# cypherseed/tests/test_password_strength.py

import unittest
from cypherseed import password_strength

class TestPasswordStrength(unittest.TestCase):

    def test_calculate_strength(self):
        strength = password_strength.calculate_strength(4, 2048)
        self.assertTrue(strength > 0)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            password_strength.calculate_strength(-1, 2048)

if __name__ == '__main__':
    unittest.main()
