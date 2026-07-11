from project3_1 import Stack
from project3_3 import Calculator


class Infix_expression(Calculator):
    def __init__(self, infix_expression):
        self.infix_expression = infix_expression.replace(" ", "")

    def calculation(self):
        if not self.infix_expression:
            return "you have not entered an expression to calculate."
        try:
            s = Stack()
            operator_order = {
                "+": 1,
                "-": 1,
                "*": 2,
                "/": 2,
                "^": 3,
                "ⁿ√": 3,
                "sin": 4,
                "cos": 4,
                "tan": 4,
                "cot": 4,
                "sec": 4,
                "csc": 4,
                "arcsin": 4,
                "arccos": 4,
                "arctan": 4,
                "arccot": 4,
                "arcsec": 4,
                "arccsc": 4,
                "sinh": 4,
                "cosh": 4,
                "tanh": 4,
                "coth": 4,
                "sech": 4,
                "csch": 4,
                "log": 4,
                "e": 4,
                "ln": 4,
                "reverse": 4,
            }
            multy_digit_numbers = []
            multy_digit_number = ""
            current_function = ""
            for index, char in enumerate(self.infix_expression):
                if char in "0123456789.":
                    multy_digit_number += char
                elif char == "-":
                    if index == 0 or self.infix_expression[index - 1] in [
                        "+",
                        "-",
                        "*",
                        "/",
                        "^",
                        "(",
                    ]:
                        multy_digit_numbers.append(0)
                        s.push_item(char)
                    else:
                        if multy_digit_number:
                            multy_digit_numbers.append(float(multy_digit_number))
                            multy_digit_number = ""
                        while (
                            not s.is_empty()
                            and s.items[-1] != "("
                            and operator_order.get(s.items[-1], 0)
                            >= operator_order[char]
                        ):
                            number2 = multy_digit_numbers.pop()
                            number1 = multy_digit_numbers.pop()
                            operator = s.items.pop()
                            multy_digit_numbers.append(
                                self.main(operator, number1, number2)
                            )
                        s.push_item(char)
                elif char == "(":
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""
                    s.push_item(char)
                    if current_function:
                        s.push_item(current_function)
                        current_function = ""
                elif char == ")":
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""

                    while (
                        not s.is_empty()
                        and s.items[-1] != "("
                        and len(multy_digit_numbers) >= 2
                    ):
                        number2 = multy_digit_numbers.pop()
                        number1 = multy_digit_numbers.pop()
                        operator = s.items.pop()
                        multy_digit_numbers.append(
                            self.main(operator, number1, number2)
                        )

                    if not s.is_empty() and s.items[-1] in operator_order:
                        number = multy_digit_numbers.pop()
                        function = s.items.pop()
                        multy_digit_numbers.append(self.main_function(function, number))

                    if not s.is_empty() and s.items[-1] == "(":
                        s.items.pop()
                elif char.isalpha():
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""
                    current_function += char
                else:
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""
                    while (
                        not s.is_empty()
                        and s.items[-1] != "("
                        and operator_order.get(s.items[-1], 0) >= operator_order[char]
                    ):
                        number2 = multy_digit_numbers.pop()
                        number1 = multy_digit_numbers.pop()
                        operator = s.items.pop()
                        multy_digit_numbers.append(
                            self.main(operator, number1, number2)
                        )
                    s.push_item(char)
            if multy_digit_number:
                multy_digit_numbers.append(float(multy_digit_number))
                multy_digit_number = ""
            while not s.is_empty():
                number2 = multy_digit_numbers.pop()
                number1 = multy_digit_numbers.pop()
                operator = s.items.pop()
                multy_digit_numbers.append(self.main(operator, number1, number2))
            return multy_digit_numbers[0]
        except Exception as e:
            return f"error : {e}"

expression=input('Enter your expression:')
infix=Infix_expression(expression)
print(infix.calculation())