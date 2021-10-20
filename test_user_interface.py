import unittest
import user_interface
import cans
import coins

class TestValidateMainMenu(unittest.TestCase):
    """Tests for the validate_main_menu function in user_interface module"""

    def test_valid_input_1_returns_proper_tuple(self):
        """Test that passing in the value of 1 returns a tuple of (True, 1)"""
        output = user_interface.validate_main_menu(1)
        self.assertEqual(output, (True, 1))

    def test_valid_input_2_returns_proper_tuple(self):
        """Test that passing in the value of 2 returns a tuple of (True, 2)"""
        output = user_interface.validate_main_menu(2)
        self.assertEqual(output, (True, 2))

    def test_valid_input_3_returns_proper_tuple(self):
        """Test that passing in the value of 3 returns a tuple of (True, 3)"""
        output = user_interface.validate_main_menu(3)
        self.assertEqual(output, (True, 3))

    def test_valid_input_4_returns_proper_tuple(self):
        """Test that passing in the value of 4 returns a tuple of (True, 4)"""
        output = user_interface.validate_main_menu(4)
        self.assertEqual(output, (True, 4))

    def test_invalid_input_returns_proper_tuple(self):
        """Test that passing in the value of 5 returns a tuple of (False, None)"""
        output = user_interface.validate_main_menu(5)
        self.assertEqual(output, (False, None))

class TestTryParseInt(unittest.TestCase):
    """Tests for the try_parse_int function in user_interface module"""

    def test_number_string_returns_int(self):
        """Test that passing in the string '10' returns the integer 10"""
        output = user_interface.try_parse_int("10")
        self.assertEqual(output, 10)

    def test_invalid_string_returns_0(self):
        """Test that passing in the string 'hello' returns the integer 0"""
        output = user_interface.try_parse_int("hello")
        self.assertEqual(output, 0)

class TestGetUniqueCanNames(unittest.TestCase):
    """Tests for the get_unique_can_names function in user_interface module"""
    
    def test_input_with_duplicate_cans_returns_list_of_unique_names(self):
        """Test that passing in a list containing 2 of each can returns a list of only 3 names"""
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
        """Test that pssing in an empty list will return an empty list"""
        can_list = []
        output = user_interface.get_unique_can_names(can_list)
        self.assertEqual(0, len(output))

class TestDisplayPaymentValue(unittest.TestCase):
    """Tests for the display_payment_value function in user_interface module"""

    def test_input_list_of_each_coin_returns_proper_value(self):
        """Test that passing in a list of each coin type will return the sum of their values"""
        quarter = coins.Quarter()
        dime = coins.Dime()
        nickel = coins.Nickel()
        penny = coins.Penny()
        payment = [quarter, dime, nickel, penny]
        output = user_interface.display_payment_value(payment)
        self.assertEqual(0.41, output)

    def test_input_empty_list_returns_0(self):
        """Test that passing in an emptry list returns a value of 0"""
        payment = []
        output = user_interface.display_payment_value(payment)
        self.assertEqual(0, output)

if __name__ == '__main__':
    unittest.main()