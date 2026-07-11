import math
from project3_2 import (
    operation_with_two_number,
    operation_with_one_number,
    logarithm_law,
)


class Calculator:
    def __init__(self):
        pass

    def addition(self, number1, number2):
        return number1 + number2

    def minus(self, number1, number2):
        return number1 - number2

    def multiplication(self, number1, number2):
        return number1 * number2

    @operation_with_two_number
    def division(self, number1, number2):
        return number1 / number2

    def power(self, number1, number2):
        return pow(number1, number2)

    def nth_root(self, number1, number2):
        return pow(number1, 1 / number2)

    @operation_with_two_number
    def remainder(self, number1, number2):
        return number1 % number2

    @logarithm_law
    def logarithm(self, number1, number2):
        return math.log(number1, number2)

    def percent(self, number):
        return number / 100

    def square(self, number):
        return pow(number, 2)

    def square_root(self, number):
        return math.sqrt(number)

    @operation_with_one_number
    def reverse(self, number):
        return pow(number, -1)

    def natural_logarithm(self, number):
        return math.log(number, math.e)

    def exponential(self, number):
        return math.exp(number)

    def factorial(self, number):
        return math.factorial(number)

    def absolute_mathematical_value(self, number):
        return abs(number)

    def sinus(self, number):
        number = math.radians(number)
        return math.sin(number)

    def cosinus(self, number):
        number = math.radians(number)
        return math.cos(number)

    def tangente(self, number):
        number = math.radians(number)
        return math.tan(number)

    def cotangente(self, number):
        number = math.radians(number)
        return 1 / math.tan(number)

    def secante(self, number):
        number = math.radians(number)
        cos = self.cosinus(number)
        return 1 / cos

    def cosecante(self, number):
        number = math.radians(number)
        sin = self.sinus(number)
        return 1 / sin

    def sinus_inverse(self, number):
        number = math.radians(number)
        return math.asin(number)

    def cosinus_inverse(self, number):
        number = math.radians(number)
        return math.acos(number)

    def tangente_inverse(self, number):
        number = math.radians(number)
        return math.atan(number)

    def cotangente_inverse(self, number):
        number = math.radians(number)
        return math.atan(1 / number)

    def secante_inverse(self, number):
        number = math.radians(number)
        return math.acos(1 / number)

    def cosecante_inverse(self, number):
        number = math.radians(number)
        return math.asin(1 / number)

    def sinus_hyperbolique(self, number):
        number = math.radians(number)
        return math.sinh(number)

    def cosinus_hyperbolique(self, number):
        number = math.radians(number)
        return math.cosh(number)

    def tangente_hyperbolique(self, number):
        number = math.radians(number)
        return math.tanh(number)

    def cotangente_hyperbolique(self, number):
        number = math.radians(number)
        return math.cosh(number) / math.sinh(number)

    def secante_hyperbolique(self, number):
        number = math.radians(number)
        return 1 / math.cosh(number)

    def cosecante_hyperbolique(self, number):
        number = math.radians(number)
        return 1 / math.sinh(number)

    def main(self, operator, number1, number2):
        if operator == "+":
            return self.addition(number1, number2)
        elif operator == "-":
            return self.minus(number1, number2)
        elif operator == "*":
            return self.multiplication(number1, number2)
        elif operator == "/":
            return self.division(number1, number2)
        elif operator == "^":
            return self.power(number1, number2)
        elif operator == "%":
            return self.remainder(number1, number2)
        elif operator == "ⁿ√":
            return self.nth_root(number1, number2)
        elif operator == "log":
            return self.logarithm(number1, number2)

    def main_function(self, function_name, number):
        if function_name == "square":
            return self.square(number)
        elif function_name == "square_root":
            return self.square_root(number)
        elif function_name == "reverse":
            return self.reverse(number)
        elif function_name == "e":
            return self.exponential(number)
        elif function_name == "fact":
            return self.factorial(number)
        elif function_name == "| |":
            return self.absolute_mathematical_value(number)
        elif function_name == "ln":
            return self.natural_logarithm(number)
        elif function_name == "sin":
            return self.sinus(number)
        elif function_name == "cos":
            return self.cosinus(number)
        elif function_name == "tan":
            return self.tangente(number)
        elif function_name == "cot":
            return self.cotangente(number)
        elif function_name == "sec":
            return self.secante(number)
        elif function_name == "csc":
            return self.cosecante(number)
        elif function_name == "arcsin":
            return self.sinus_inverse(number)
        elif function_name == "arccos":
            return self.cosinus_inverse(number)
        elif function_name == "arctan":
            return self.tangente_inverse(number)
        elif function_name == "arccot":
            return self.cotangente_inverse(number)
        elif function_name == "arcsec":
            return self.secante_inverse(number)
        elif function_name == "arccsc":
            return self.cosecante_inverse(number)
        elif function_name == "sinh":
            return self.sinus_hyperbolique(number)
        elif function_name == "cosh":
            return self.cosinus_hyperbolique(number)
        elif function_name == "tanh":
            return self.tangente_hyperbolique(number)
        elif function_name == "coth":
            return self.cotangente_hyperbolique(number)
        elif function_name == "sech":
            return self.secante_hyperbolique(number)
        elif function_name == "csch":
            return self.cosecante_hyperbolique(number)
