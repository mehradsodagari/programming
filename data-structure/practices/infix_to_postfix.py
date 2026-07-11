class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0 
    def push_item(self,item):
        return self.items.append(item)
    def pop_item(self):
        if self.is_empty():
            return 'satack is rmpty'
        return self.items.pop() 
    def size(self):
        return len(self.items) 
class ConvertInfixToPostfix:
    def __init__(self,infix_expression):
        self.infix_expression=infix_expression 
    def convert(self):
        if self.infix_expression.count('(')!=self.infix_expression.count(')'):
            return 'parenthesis!'
        order_operator={'^':3,
               '*':2,
               '/':2,
               '+':1,
               '-':1}
        s=Stack()
        postfix_expression=''
        current_number=''
        for char in self.infix_expression:
            if char not in ['+','-','*','/','^','(',')']:
                current_number+=char
            elif char=='(':
                if current_number:
                    postfix_expression+=current_number
                    postfix_expression+=' '
                    current_number=''
                s.push_item(char)
            elif char==')':
                if current_number:
                    postfix_expression+=current_number
                    postfix_expression+=' '
                    current_number=''
                while not s.is_empty() and s.items[-1]!='(':
                    postfix_expression+=s.pop_item()
                    postfix_expression+=' '
                if not s.is_empty() and s.items[-1]=='(':
                    s.pop_item()
            else:
                if current_number:
                    postfix_expression+=current_number
                    postfix_expression+=' '
                    current_number=''
                while not s.is_empty() and s.items[-1]!='(' and order_operator.get(s.items[-1],0)>=order_operator[char]:
                    operator=s.pop_item() 
                    postfix_expression+=operator 
                    postfix_expression+=' '
                s.push_item(char)
        if current_number:
            postfix_expression+=current_number
            postfix_expression+=' '
            current_number=''
        while not s.is_empty():
            operator=s.pop_item() 
            postfix_expression+=operator
            postfix_expression+=' '
        return postfix_expression.strip()

