import math
from decorators_for_calculator import operation_with_two_number,operation_with_one_number,logarithm_law
class Calculator:
    class Operations_With_Two_Number:
        def __init__(self,number1,number2):
            self.number1=number1
            self.number2=number2  
        def addition(self):
            return self.number1+self.number2 
        def minus(self):
            return self.number1-self.number2 
        def multiplication(self):
            return self.number1*self.number2 
        @operation_with_two_number
        def division(self):
            return self.number1/self.number2 
        def power(self):
            return pow(self.number1,self.number2)
        def nth_root(self):
            return math.sqrt(self.number1,self.number2)
        @operation_with_two_number
        def remainder(self):
            return self.number1%self.number2 
        @logarithm_law
        def logarithm(self):
            return math.log(self.number1,self.number2)
    class Operations_With_one_Number:
        def __init__(self,number):
            self.number=number 
        def percent(self):
            return self.number/100 
        def square(self):
            return pow(self.number,2) 
        def square_root(self):
            return math.sqrt(self.number)
        @operation_with_one_number
        def reverse(self):
            return pow(self.number,-1) 
        def natural_logarithm(self):
            return math.log(self.number,math.e)
        def exponential(self):
            return math.exp(self.number) 
        def factorial(self):
            return math.factorial(self.number) 
        def absolute_mathematical_value(self):
            return math.abs(self.number)
        def sinus(self):
            self.number=math.radians(self.number)
            return math.sin(self.number)
        def cosinus(self):
            self.number=math.radians(self.number)
            return math.cos(self.number) 
        def tangente(self):
            self.number=math.radians(self.number)
            return math.tan(self.number)
        def cotangente(self):
            self.number=math.radians(self.number)
            return math.cot(self.number)
        def secante(self):
            self.number=math.radians(self.number)
            cos=self.cosinus(self.number)
            return 1/cos 
        def cosecante(self):
            self.number=math.radians(self.number)
            sin=self.sinus(self.number) 
            return 1/sin 
        def sinus_inverse(self):
            self.number=math.radians(self.number)
            return math.asin(self.number) 
        def cosinus_inverse(self):
            self.number=math.radians(self.number)
            return math.acos(self.number) 
        def tangente_inverse(self):
            self.number=math.radians(self.number)
            return math.atan(self.number) 
        def cotangente_inverse(self):
            self.number=math.radians(self.number)
            return math.atan(1/self.number)
        def secante_inverse(self):
            self.number=math.radians(self.number)
            return math.acos(1/self.number) 
        def cosecante_inverse(self):
            self.number=math.radians(self.number)
            return math.asin(1/self.number)
        def sinus_hyperbolique(self):
            self.number=math.radians(self.number)
            return math.sinh(self.number) 
        def cosinus_hyperbolique(self):
            self.number=math.radians(self.number)
            return math.cosh(self.number) 
        def tangente_hyperbolique(self):
            self.number=math.radians(self.number)
            return math.tanh(self.number)
        def cotangente_hyperbolique(self):
            self.number=math.radians(self.number)
            return math.cosh(self.number)/math.sinh(self.number)
        def secante_hyperbolique(self):
            self.number=math.radians(self.number)
            return 1/math.cosh(self.number) 
        def cosecante_hyperbolique(self):
            self.number=math.radians(self.number)
            return 1/math.sinh(self.number)
    class Operator_on_function:
        def __init__(self,function,number):
            self.function=function 
            self.number=number 
        def integral(self):
            pass 
        def derivative(self):
            pass 
def main():
    try:
        result=Calculator
        what_operation=input('what operation do you want to perform? ')
        if what_operation in ['addition','minus','multiplication','division','power','nth_root','log']:
            first_number=int(input('enter the first number : '))
            second_number=int(input('enter the second number : '))
            operation=Calculator.Operations_With_Two_Number(first_number,second_number) 
            return getattr(operation,what_operation)()
        elif what_operation in ['percent','square','square root','reverse','natural logarithm','exponential','factorial',
                                'absolute mathematical value','sinus','cosinus','tangente','cotengante','secante','cosecante',
                                'sinus inverse','cosinus inverse','tangente inverse','cotangente inverse','secante inverse',
                                'cosecante inverse','sinus hyperbolique','cosinus hyperbolique','tangente hyperbolique',
                                'cotangente hyperbolique','secante hyperbolique','cosecante hyperbolique']:
            number=int(input('enter the number : '))
            operation=Calculator.Operations_With_one_Number(number) 
            return getattr(operation,what_operation)()
        else:
            answer=input('are you sure you entered the operator name correctly?(y/n) ')
            while answer.lower() not in ['y','n']:
                print('please answer caerfully.')
                answer=input('are you sure you entered the operator name correctly?(y/n) ') 
            if answer=='y':
                return "excuse me.this calculator can't do that."
            else:
                return main()
    except Exception as e:  
        return f'error : {e}'
if __name__=='__main__':
    print(main())