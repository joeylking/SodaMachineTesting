import unittest
import user_interface

class TestValidateMainMenu(unittest.TestCase):
    """Tests for the validate_main_menu function in user_interface module"""

    def test_valid_input_1_returns_proper_tuple(self):
        output = user_interface.validate_main_menu(1)
        self.assertEqual(output, (True, 1))

    def test_valid_input_2_returns_proper_tuple(self):
        output = user_interface.validate_main_menu(2)
        self.assertEqual(output, (True, 2))

    def test_valid_input_3_returns_proper_tuple(self):
        output = user_interface.validate_main_menu(3)
        self.assertEqual(output, (True, 3))

    def test_valid_input_4_returns_proper_tuple(self):
        output = user_interface.validate_main_menu(4)
        self.assertEqual(output, (True, 4))

if __name__ == '__main__':
    unittest.main()