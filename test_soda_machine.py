import unittest
from soda_machine import SodaMachine

class Fill_Register(unittest.TestCase):
    """Tests for the fill register method in SodaMachine"""
    
    def setUp(self):
        self.soda_machine = SodaMachine()

    def test_quarters_are_filled_into_register_list(self):
        """Tests to make sure our list in register is filled with quarters."""
        






if __name__ == '__main__':
    unittest.main()


