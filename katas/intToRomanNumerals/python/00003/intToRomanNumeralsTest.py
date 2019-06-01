import unittest
from intToRomanNumerals import IntToRomanNumerals

class TestIntToRomanNumeralsTest(unittest.TestCase):
    def setUp(self):
        self.intToRomanNumerals = IntToRomanNumerals()

    def test_1ReturnsI(self):
        self.assertEqual('I', self.intToRomanNumerals.getRomanNumeral(1))

    def test_2ReturnsII(self):
        self.assertEqual('II', self.intToRomanNumerals.getRomanNumeral(2))

    def test_5ReturnsV(self):
        self.assertEqual('V', self.intToRomanNumerals.getRomanNumeral(5))

    def test_10ReturnsX(self):
        self.assertEqual('X', self.intToRomanNumerals.getRomanNumeral(10))

    def test_50ReturnsL(self):
        self.assertEqual('L', self.intToRomanNumerals.getRomanNumeral(50))

    def test_100ReturnsC(self):
        self.assertEqual('C', self.intToRomanNumerals.getRomanNumeral(100))

    def test_500ReturnsD(self):
        self.assertEqual('D', self.intToRomanNumerals.getRomanNumeral(500))

    def test_1000ReturnsM(self):
        self.assertEqual('M', self.intToRomanNumerals.getRomanNumeral(1000))

    def test_4ReturnsIV(self):
        self.assertEqual('IV', self.intToRomanNumerals.getRomanNumeral(4))

    def test_9ReturnsIX(self):
        self.assertEqual('IX', self.intToRomanNumerals.getRomanNumeral(9))

    def test_14ReturnsXIV(self):
        self.assertEqual('XIV', self.intToRomanNumerals.getRomanNumeral(14))

    def test_1994ReturnsMCMXCIV(self):
        self.assertEqual('MCMXCIV', self.intToRomanNumerals.getRomanNumeral(1994))

    def test_1900ReturnsMCM(self):
        self.assertEqual('MCM', self.intToRomanNumerals.getRomanNumeral(1900))


if __name__ == '__main__':
    unittest.main()
