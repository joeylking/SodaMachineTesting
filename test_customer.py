from typing import Union
import unittest
from customer import Customer

class TestGetWalletCoin(unittest.TestCase):
    """Tests for the get_wallet_coin method in Customer"""

    def setUp(self):
        self.customer = Customer()

    def test_quarter_string_returns_quarter_object(self):
        """Test that passing in string 'Quarter' returns a quarter object"""
        coin = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(0.25, coin.value)

    def test_dime_string_returns_dime_object(self):
        """Test that passing in string 'Dime' returns a dime object"""
        coin = self.customer.get_wallet_coin('Dime')
        self.assertEqual(0.10, coin.value)

    def test_nickel_string_returns_nickel_object(self):
        """Test that passing in string 'Nickel' returns a nickel object"""
        coin = self.customer.get_wallet_coin('Nickel')
        self.assertEqual(0.05, coin.value)

    def test_penny_string_returns_penny_object(self):
        """Test that passing in string 'Penny' returns a penny object"""
        coin = self.customer.get_wallet_coin('Penny')
        self.assertEqual(0.01, coin.value)

    def test_invalid_coin_string_returns_none(self):
        """Test that passing in string that is not a valid coin name returns None"""
        coin = self.customer.get_wallet_coin('Dollar')
        self.assertIsNone(coin)

class TestAddCoinsToWallet(unittest.TestCase):
    pass

class TestAddCanToBackpack(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()