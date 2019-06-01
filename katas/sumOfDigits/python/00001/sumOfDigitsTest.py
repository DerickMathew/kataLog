import unittest
from sumOfDigits import SumOfDigits

class TestSumOfDigits (unittest.TestCase):

    def setUp(self):
        self.sumOfDigits = SumOfDigits()

    def test_numberIfSingleDigitNumber(self):
        self.assertEqual(self.sumOfDigits.sumDigits(1), 1);

    def test_6IfNumberIs15(self):
        self.assertEqual(self.sumOfDigits.sumDigits(15), 6);

    def test_9IfNumberIs99(self):
        self.assertEqual(self.sumOfDigits.sumDigits(99), 9);

    def test_9IfNumberIs12Nines(self):
        self.assertEqual(self.sumOfDigits.sumDigits(999999999999), 9);

if __name__ == '__main__':
    unittest.main()
