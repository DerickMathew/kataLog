import unittest
from romanNumeralsToInt import RomanNumeralsToInt

class TestRomanNumeralsToInt(unittest.TestCase):

    def setUp(self):
        self.romanNumeralsToInt = RomanNumeralsToInt()

    def test_IReturns1(self):
        self.assertEqual(1, self.romanNumeralsToInt.getNum('I'));

    def test_VReturns5(self):
        self.assertEqual(5, self.romanNumeralsToInt.getNum('V'));

    def test_XReturns10(self):
        self.assertEqual(10, self.romanNumeralsToInt.getNum('X'));

    def test_LReturns50(self):
        self.assertEqual(50, self.romanNumeralsToInt.getNum('L'));

    def test_CReturns100(self):
        self.assertEqual(100, self.romanNumeralsToInt.getNum('C'));

    def test_DReturns500(self):
        self.assertEqual(500, self.romanNumeralsToInt.getNum('D'));

    def test_MReturns1000(self):
        self.assertEqual(1000, self.romanNumeralsToInt.getNum('M'));

    def test_IIReturns2(self):
        self.assertEqual(2, self.romanNumeralsToInt.getNum('II'));

    def test_IVReturns4(self):
        self.assertEqual(4, self.romanNumeralsToInt.getNum('IV'));

    def test_IXReturns9(self):
        self.assertEqual(9, self.romanNumeralsToInt.getNum('IX'));

    def test_XIXReturns19(self):
        self.assertEqual(19, self.romanNumeralsToInt.getNum('XIX'));

    def test_XLReturns40(self):
        self.assertEqual(40, self.romanNumeralsToInt.getNum('XL'));

    def test_IXLReturns39(self):
        self.assertEqual(39, self.romanNumeralsToInt.getNum('IXL'));

    def test_IVXLReturns34(self):
        self.assertEqual(34, self.romanNumeralsToInt.getNum('IVXL'));

    def test_IVXLCDMReturns344(self):
        self.assertEqual(334, self.romanNumeralsToInt.getNum('IVXLCDM'));

    def test_MIVXLCDMReturns1344(self):
        self.assertEqual(1334, self.romanNumeralsToInt.getNum('MIVXLCDM'));

    def test_IMMMMReturns3999(self):
        self.assertEqual(3999, self.romanNumeralsToInt.getNum('IMMMM'));

if __name__ == '__main__':
    unittest.main()
