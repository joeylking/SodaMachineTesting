import unittest
import user_interface
import cans

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

    def test_invalid_input_returns_proper_tuple(self):
        output = user_interface.validate_main_menu(5)
        self.assertEqual(output, (False, None))

class TestTryParseInt(unittest.TestCase):
    """Tests for the try_parse_int function in user_interface module"""

    def test_number_string_returns_int(self):
        output = user_interface.try_parse_int("10")
        self.assertEqual(output, 10)

    def test_invalid_string_returns_0(self):
        output = user_interface.try_parse_int("hello")
        self.assertEqual(output, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    """Tests for the get_unique_can_names function in user_interface module"""
    
    def test_input_with_duplicate_cans_returns_list_of_unique_names(self):
        can1 = cans.Cola()
        can2 = cans.Cola()
        can3 = cans.OrangeSoda()
        can4 = cans.OrangeSoda()
        can5 = cans.RootBeer()
        can6 = cans.RootBeer()
        can_list = [can1, can2, can3, can4, can5, can6]
        output = user_interface.get_unique_can_names(can_list)
        self.assertEqual(3, len(output))

    def test_input_empty_list_returns_empty_list(self):
        can_list = []
        output = user_interface.get_unique_can_names(can_list)
        self.assertEqual(0, len(output))


if __name__ == '__main__':
    unittest.main()