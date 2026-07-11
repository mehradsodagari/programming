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
            operator_order = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3}
            multy_digit_numbers = []
            multy_digit_number = ""
            for index, char in enumerate(self.infix_expression):
                if char not in ["+", "-", "*", "/", "^", "(", ")"] or char == ".":
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
                            operator = s.pop_item()
                            multy_digit_numbers.append(
                                self.main(operator, number1, number2)
                            )
                        s.push_item(char)
                elif char == "(":
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""
                    s.push_item(char)
                elif char == ")":
                    if multy_digit_number:
                        multy_digit_numbers.append(float(multy_digit_number))
                        multy_digit_number = ""
                    while not s.is_empty() and s.items[-1] != "(":
                        number2 = multy_digit_numbers.pop()
                        number1 = multy_digit_numbers.pop()
                        operator = s.pop_item()
                        multy_digit_numbers.append(
                            self.main(operator, number1, number2)
                        )
                    s.pop_item()
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
                        operator = s.pop_item()
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
                operator = s.pop_item()
                multy_digit_numbers.append(self.main(operator, number1, number2))
            return multy_digit_numbers[0]
        except Exception as e:
            return f"error : {e}"
