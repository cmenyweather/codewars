import unittest
from loosechange import loose_change

class Test_Loose_Change_input(unittest.TestCase):
    def test_change(self):
        # Test least amount of coins used to make up the amount
        self.assertEqual(loose_change(29), {'Nickels': 0, 'Pennies': 4, 'Dimes': 0, 'Quarters':1})
        self.assertEqual(loose_change(91), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters':3})
        self.assertEqual(loose_change(0), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters':0})
        self.assertEqual(loose_change(-2), {'Nickels': 0, 'Pennies': 0, 'Dimes': 0, 'Quarters':0})
        self.assertEqual(loose_change(3.9), {'Nickels': 0, 'Pennies': 3, 'Dimes': 0, 'Quarters':0})
        self.assertEqual(loose_change(66.4), {'Nickels': 1, 'Pennies': 1, 'Dimes': 1, 'Quarters':2})

    def test_values(self):
        # Test that bad values are caught
        self.assertRaises(ValueError, loose_change, 'string')
        self.assertRaises(ValueError, loose_change, [1, 2, 3])
        self.assertRaises(ValueError, loose_change, {'test':1})
        self.assertRaises(ValueError, loose_change, (1, 2, 3))

if __name__ == '__main__':
    unittest.main()
