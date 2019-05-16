import unittest
from fizzbuzz import Fizzbuzz

class TestFizzBuzz (unittest.TestCase):

    def setUp(self):
        self.fizzbuzz = Fizzbuzz()

    def test_shouldReturnNumber(self):
        self.assertEqual(self.fizzbuzz.getResponse(1), 1)

    def test_shouldReturnFizzIfGiven3(self):
        self.assertEqual(self.fizzbuzz.getResponse(3), "Fizz")

    def test_shouldReturnFizzIfGivenMultipleOf3(self):
        self.assertEqual(self.fizzbuzz.getResponse(6), "Fizz")
        self.assertEqual(self.fizzbuzz.getResponse(3*7), "Fizz")

    def test_shouldReturnBuzzIfGivenMultiplesOf5(self):
        self.assertEqual(self.fizzbuzz.getResponse(5), "Buzz")
        self.assertEqual(self.fizzbuzz.getResponse(5*2), "Buzz")
        self.assertEqual(self.fizzbuzz.getResponse(5*5), "Buzz")

    def test_shouldReturnFizzBuzzIfGivenMultiplesOf3And5(self):
        self.assertEqual(self.fizzbuzz.getResponse(3*5), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.getResponse(3*5*2), "FizzBuzz")
        self.assertEqual(self.fizzbuzz.getResponse(3*5*4), "FizzBuzz")

if __name__ == '__main__':
    unittest.main()
