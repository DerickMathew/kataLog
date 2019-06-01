import unittest
from opTreeParser import OpTreeParser

class TestOpTreeParserTest (unittest.TestCase):
    def setUp(self):
        self.opTreeParser = OpTreeParser();

    def test_shouldPrintLhsOpAndRhs(self):
        input = {
            'lhs': '10',
            'op': '+',
            'rhs': '10'
        };
        expectedOutput = '10+10'
        actualOutput = self.opTreeParser.printEquation(input)
        self.assertEqual(expectedOutput, actualOutput)

    def test_shouldPrintTreeWith2UnequalLevels(self):
        input = {
            'lhs': '7',
            'op': '=',
            'rhs': {
                'lhs': '5',
                'op': '+',
                'rhs': '2'
            }
        };
        expectedOutput = '7=5+2'
        actualOutput = self.opTreeParser.printEquation(input)
        self.assertEqual(expectedOutput, actualOutput)

    def test_shouldPrintTreeWith2EqualLevels(self):
        input = {
            'lhs': {
                'lhs': '10',
                'op': '-',
                'rhs': '3'
            },
            'op': '=',
            'rhs': {
                'lhs': '5',
                'op': '+',
                'rhs': '2'
            }
        };
        expectedOutput = '10-3=5+2'
        actualOutput = self.opTreeParser.printEquation(input)
        self.assertEqual(expectedOutput, actualOutput)

    def test_shouldSwapNodes(self):
        input = {
            'lhs': '10',
            'op': '+',
            'rhs': '5'
        };
        expectedOutput = {
            'lhs': '5',
            'op': '+',
            'rhs': '10'
        };
        actualOutput = self.opTreeParser.swapLhsAndRhs(input)
        self.assertEqual(expectedOutput, actualOutput)

if __name__ == '__main__':
    unittest.main()
