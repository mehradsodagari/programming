class Stack:
    def __init__(self):
        self.items=[] 
    def is_empty(self):
        return len(self.items)==0 
    def push_item(self,data):
        return self.items.append(data)
    def pop_item(self):
        if self.is_empty():
            return 'stack is empty' 
        return self.items.pop() 
    def peek(self):
        return self.items[-1] 
    def __len__(self):
        return len(self.items) 
    