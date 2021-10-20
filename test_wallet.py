import unittest
from wallet import Wallet

class TestFillWallet(unittest.TestCase):
    """Tests for the fill_wallet method in Wallet"""

    def setUp(self):
        self.wallet = Wallet()

    def test_money_list_length(self):
        """Test that when a Wallet object is instantiated, its money list has a length of 88"""
        length = len(self.wallet.money)
        self.assertEqual(88, length)

if __name__ == '__main__':
    unittest.main()