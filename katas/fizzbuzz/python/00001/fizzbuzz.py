class Fizzbuzz:
    def getResponse(self, value):
        fizz = lambda n : "Fizz" if n % 3 == 0 else ""
        buzz = lambda n : "Buzz" if n % 5 == 0 else ""
        return fizz(value) + buzz(value) or value

    def main(self):
        for i in range(1, 101):
            print(self.getResponse(i))

if __name__ == '__main__':
    fizzbuzz = Fizzbuzz()
    fizzbuzz.main()
