import unittest
from findTheOddInt import FindTheOddInt

class TestFindTheOddInt (unittest.TestCase):
    def setUp(self):
        self.findTheOddInt = FindTheOddInt()

    def test_returnNumberIfOnlyOneElement(self):
        arr = [1]
        actual = self.findTheOddInt.getOddInt(arr)
        self.assertEqual(1, actual)

    def test_shouldNotShowRepeatedElements(self):
        arr = [2, 1, 2]
        actual = self.findTheOddInt.getOddInt(arr)
        self.assertEqual(1, actual)
