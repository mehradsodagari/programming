def operation_with_two_number(func):
    def number2_is_zero(number1,number2):
        if number2==0:
            raise ZeroDivisionError("the second number can't be zero")
        else:
            return (func(number1,number2))
    return number2_is_zero 
def operation_with_one_number(func):
    def number_is_zero(number):
        if number==0:
            raise ZeroDivisionError("the number can't be zero")
    return number_is_zero 
def logarithm_law(func):
    def laws(number1,number2):
        if number1<=0 or number2<0:
            raise Exception('Neither of the two numbers must be positive')
        if number2==1:
            raise Exception("second number can't be one")
        return func(number1,number2)
    return laws 
