from project5_1 import SinglyLinkedList


class Queue(SinglyLinkedList):
    def __init__(self):
        super().__init__()

    def enqueue(self, data):
        return self.inserting_at_the_end(data)

    def dequeue(self):
        if self.is_empty():
            return "queue is empty"
        return self.removing_at_the_beginning()

    def is_empty(self):
        return self._SinglyLinkedList__size == 0

    def __len__(self):
        return self._SinglyLinkedList__size

    def peek(self):
        if self.is_empty():
            return None
        return self.head.data
