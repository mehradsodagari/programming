class Stack:
    def __init__(self):
        self.items=[] 
    def is_empty(self):
        return len(self.items)==0 
    def push_item(self,item):
        return self.items.append(item) 
    def pop_item(self):
        if self.is_empty():
            return None 
        return self.items.pop() 
    def size(self): 
        return len(self.items)
    def peek(self):
        if self.is_empty():
            return None 
        return self.items[-1] 
def convert(postfix):
    s=Stack() 
    tokens=postfix.split() 
    for token in tokens:
        if token.isdigit() or (token[0]=='-' and token[1:].isnumeric()):
            s.push_item(token) 
        else:
            if s.size()<2:
                return 'invalid' 
            operand1=s.pop_item()
            operand2=s.pop_item() 
            if token in '+-*/':
                result=f'({operand2} {token} {operand1})' 
                s.push_item(result) 
            else:
                result=f'({operand2}{token}{operand1})' 
                s.push_item(result)
    if s.size()!=1:
        return 'Invalid' 
    return s.items[0][1:-1] 
