class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push_item(self, item):
        return self.items.append(item)

    def pop_item(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def size(self):
        return len(self.items)
