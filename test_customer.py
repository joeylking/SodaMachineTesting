import unittest
import coins
from cans import Cola
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
    """Tests for the add_coins_to_wallet method in Customer"""

    def setUp(self):
        self.customer = Customer()

    def test_adding_coins_increases_length_of_money_list(self):
        """Test that passing in a list of 3 coins increases length of customer's wallet's money list by 3"""
        original_money_length = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([coins.Dime, coins.Penny, coins.Nickel])
        new_money_length = len(self.customer.wallet.money)
        self.assertEqual((original_money_length + 3), new_money_length)

    def test_adding_no_coins_doesnt_increase_length_of_money_list(self):
        """Test that passing in an empty list does not increase length of customer's wallet's money list"""
        original_money_length = len(self.customer.wallet.money)
        self.customer.add_coins_to_wallet([])
        new_money_length = len(self.customer.wallet.money)
        self.assertEqual(original_money_length, new_money_length)

class TestAddCanToBackpack(unittest.TestCase):
    """Tests for the add_can_to_backpack method in Customer"""

    def setUp(self):
        self.customer = Customer()

    def test_adding_cola_object_increases_purchased_cans_length(self):
        """Test that passing in a Cola object increases the length of customer's backpack's purchased_cans by 1"""
        original_purchased_length = len(self.customer.backpack.purchased_cans)
        self.customer.add_can_to_backpack(Cola)
        new_purchased_length = len(self.customer.backpack.purchased_cans)
        self.assertEqual((original_purchased_length + 1), new_purchased_length)

if __name__ == '__main__':
    unittest.main()