import unittest
from soda_machine import SodaMachine
from coins import Coin
from cans import Can

class TestSodaMachine(unittest.TestCase):
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

    def test_register_has_coin_returns_true_for_all_coins(self):
        """Tests to make sure each valid coin will return True or return False for a non-valid coin name."""
        """Quarter"""
        returns_true = self.soda_machine.register_has_coin("Quarter")
        self.assertEqual(True,returns_true)
        """Dime"""
        returns_true = self.soda_machine.register_has_coin("Dime")
        self.assertEqual(True,returns_true)
        """Nickel"""
        returns_true = self.soda_machine.register_has_coin("Nickel")
        self.assertEqual(True,returns_true)
        """Penny"""
        returns_true = self.soda_machine.register_has_coin("Penny")
        self.assertEqual(True,returns_true)
        """Invalid coin name"""
        non_valid_coin_name = self.soda_machine.register_has_coin("Invalid")
        self.assertEqual(False,non_valid_coin_name)

    def test_determine_change_value_returns_correct_difference(self):
        """Tests to make sure determine_change_value returns the correct amount of change."""
        """Test with total payment higher"""
        value_of_difference = self.soda_machine.determine_change_value(5,2)
        self.assertEqual(3,value_of_difference)
        """Test with select soda price higher."""
        value_of_difference = self.soda_machine.determine_change_value(2,5)
        self.assertEqual(-3,value_of_difference)
        """Test with equal values"""
        value_of_difference = self.soda_machine.determine_change_value(5,5)
        self.assertEqual(0,value_of_difference)

    def test_calculate_coin_value_to_ensure_every_coin_has_correct_value(self):
        """Testsing the coin names and values are correct and work by adding them all together."""
        quarter = Coin("Quarter", .25)
        dime = Coin("Dime", .10)
        nickel = Coin("Nickel", .05)
        penny = Coin("Penny", .01)
        one_of_each_coin_value = self.soda_machine.calculate_coin_value([quarter, dime, nickel, penny])
        self.assertEqual(.41, one_of_each_coin_value)
        """Adding no coins together."""
        empty_list_of_coins = self.soda_machine.calculate_coin_value([])
        self.assertEqual(0,empty_list_of_coins)

    def test_get_inventory_soda_to_get_back_same_soda_name(self):
        """Testing the soda names to make sure the names are all correct and work."""
        """Cola"""
        passed_can = self.soda_machine.get_inventory_soda("Cola")
        self.assertEqual("Cola", passed_can.name)
        """Orange Soda"""
        passed_can = self.soda_machine.get_inventory_soda("Orange Soda")
        self.assertEqual("Orange Soda", passed_can.name)
        """Root Beer"""
        passed_can = self.soda_machine.get_inventory_soda("Root Beer")
        self.assertEqual("Root Beer", passed_can.name)
        """Invalid Input"""
        passed_can = self.soda_machine.get_inventory_soda("Mountian Dew")
        self.assertEqual(None, passed_can)

    def test_return_inventory_length_of_inventory_increases(self):
        """Test to make sure the length of the inventory increases when a can is returned to it."""
        self.soda_machine.return_inventory("Cola")
        self.assertEqual(31,len(self.soda_machine.inventory))

    def test_deposit_coins_into_register_ensure_register_has_correct_length(self):
        """This test is to ensure after the coins are properly populate the register."""
        quarter = Coin("Quarter", .25)
        dime = Coin("Dime", .10)
        nickel = Coin("Nickel", .05)
        penny = Coin("Penny", .01)
        list_of_cans = [quarter, dime, nickel, penny]
        self.soda_machine.deposit_coins_into_register(list_of_cans)
        register = len(self.soda_machine.register)
        self.assertEqual(92, register)

if __name__ == '__main__':
    unittest.main()


