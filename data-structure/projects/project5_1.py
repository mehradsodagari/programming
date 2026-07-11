class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.__size = 0

    def traversal(self):
        if self.head is None:
            return "list is empty"
        probe = self.head
        while probe != None:
            print(probe.data, end=" -> ")
            probe = probe.next

    def searching(self, target):
        if self.head is None:
            return "list is empty"
        probe = self.head
        while probe != None and probe.data != target:
            probe = probe.next
        if probe is None:
            return "target not found"
        return probe.data

    def replacement(self, target, new_data):
        if self.head is None:
            return "list is empty"
        probe = self.head
        while probe != None and probe.data != target:
            probe = probe.next
        if probe is None:
            return "target not found"
        probe.data = new_data
        return probe.data

    def inserting_at_the_beginning(self, data):
        new_item = Node(data)
        new_item.next = self.head
        self.head = new_item
        if self.tail is None:
            self.tail = new_item
        self.__size += 1
        return new_item

    def inserting_at_the_end(self, data):
        if self.head is None:
            return self.inserting_at_the_beginning(data)
        new_item = Node(data)
        self.tail.next = new_item
        self.tail = new_item
        self.__size += 1
        return new_item

    def inserting_at_any_position(self, data, index):
        if self.head is None or index <= 0:
            return self.inserting_at_the_beginning(data)
        probe = self.head
        new_item = Node(data)
        while probe != None and index > 1:
            probe = probe.next
            index -= 1
        if probe is None:
            return self.inserting_at_the_end(data)
        new_item.next = probe.next
        probe.next = new_item
        self.__size += 1
        return new_item

    def removing_at_the_beginning(self):
        if self.head is None:
            return "list is empty"
        if self.__size == 1:
            removed_item = self.head
            self.head = self.tail = None
            self.__size -= 1
            return removed_item
        removed_item = self.head
        self.head = self.head.next
        self.__size -= 1
        return removed_item

    def removing_at_the_end(self):
        if self.head is None:
            return "list is empty"
        if self.head.next == self.tail:
            return self.removing_at_the_beginning()
        probe = self.head
        while probe.next.next != None:
            probe = probe.next
        if self.__size == 1:
            return self.removing_at_the_beginning()
        removed_item = probe.next
        probe.next = probe.next.next
        self.tail = probe
        self.__size -= 1
        return removed_item

    def removing_at_any_position(self, index):
        if self.head is None:
            return "list is empty"
        if index > self.__size:
            return f"the list does not have an element with index {index}"
        probe = self.head
        while probe.next != None and index > 1:
            probe = probe.next
            index -= 1
        if probe.next is self.tail:
            return self.removing_at_the_end()
        if self.__size == 1:
            return self.removing_at_the_beginning()
        removed_item = probe.next
        probe.next = probe.next.next
        self.__size -= 1
        return removed_item
