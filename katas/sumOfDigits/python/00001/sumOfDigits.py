import functools

class SumOfDigits:
    def sumDigits(self, number):
        if (number < 10):
            return number
        digitStringArray = list(str(number))
        digitArray = map(lambda n : int(n), digitStringArray)
        return self.sumDigits(functools.reduce(lambda x, y: x + y,  digitArray))

    def main():
        return sumDigits(7);

if __name__ == '__main__':
    sumOfDigits = SumOfDigits()
    sumOfDigits.main()
