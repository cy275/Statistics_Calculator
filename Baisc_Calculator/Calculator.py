from Baisc_Calculator.Addition import addition
from Baisc_Calculator.Subtraction import subtraction
from Baisc_Calculator.Multiplication import multiplication
from Baisc_Calculator.Division import division
from Baisc_Calculator.Square import square
from Baisc_Calculator.Square_Root import square_root


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def sqrt(self, a):
        self.result = square_root(a)
        return self.result
