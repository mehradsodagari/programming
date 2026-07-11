class Stack:
    def __init__(self):
        self.list_items = []

    def is_empty(self):
        return len(self.list_items) == 0

    def pop(self):
        if not self.is_empty():
            return self.list_items.pop()
        else:
            raise IndexError("no have any item in list")

    def push(self, item):
        return self.list_items.append(item)

    def size(self):
        return len(self.list_items)

    def __str__(self):
        return str(self.list_items)


def match_parenthesis(parenthesis_string):
    s = Stack()
    match = {"(": ")", "[": "]", "{": "}"}
    if len(parenthesis_string) % 2 != 0:
        return False
    for char in parenthesis_string:
        if char in match:
            s.push(char)
        else:
            if s.is_empty():
                return False
            last_open = s.pop()
            if match[last_open] != char:
                return False
    return s.is_empty()


print(match_parenthesis("(()"))
