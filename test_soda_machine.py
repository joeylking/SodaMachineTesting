import unittest
from soda_machine import SodaMachine

class TestFill_Register(unittest.TestCase):
    """Tests for the fill register method in SodaMachine"""
    
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_register_list_is_filled_with_correct_objects(self):
        """Tests to make sure our register list is filled with 88 objects."""
        register_list = len(self.soda_machine.register)
        self.assertEqual(88, register_list)

    def test_inventory_list_is_filled_with_Correct_objects(self):
        """Tests to make sure our inventory list is filled with 30 objects."""
        inventory_list = len(self.soda_machine.inventory)
        self.assertEqual(30,inventory_list)

    def test_get_coin_from_register_can_be_returned_from_register(self):
        """Tests to make sure each type of coin can be returned from the register."""
        """Quarter"""
        self.soda_machine.get_coin_from_register("Quarter")
        register_list_minus_one = len(self.soda_machine.register)
        self.assertEqual(87, register_list_minus_one)
        """Dime"""
        self.soda_machine.get_coin_from_register("Dime")
        self.assertEqual(87, register_list_minus_one)
        """Nickel"""
        self.soda_machine.get_coin_from_register("Nickel")
        self.assertEqual(87, register_list_minus_one)
        """Penny"""
        self.soda_machine.get_coin_from_register("Penny")
        self.assertEqual(87, register_list_minus_one)
        """Invalid string"""
        none_is_returned = self.soda_machine.get_coin_from_register("Invalid")
        self.assertEqual(None, none_is_returned)

if __name__ == '__main__':
    unittest.main()


