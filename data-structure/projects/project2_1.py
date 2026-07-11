class Node:
    def __init__(self, data, previous=None, next=None):
        self.data = data
        self.previous = previous
        self.next = next


class Doubly_linkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def traversal(self):
        if self.head is None:
            return None
        probe = self.head
        while probe is not None:
            print(probe.data, end=" -> ")
            probe = probe.next

    def searching(self, target):
        if self.head is None:
            return None
        elif self.head is self.tail:
            if self.head.data == target:
                return self.head.data
            else:
                return None
        else:
            probe = self.head
            while probe is not None:
                if probe.data == target:
                    return probe.data
                probe = probe.next
        return None

    def replacement(self, data, target):
        if self.head is None:
            return None
        elif self.head is self.tail:
            if self.head.data == target:
                self.head.data = data
                return self.head.data
            else:
                return None
        else:
            probe = self.head
            while probe is not None:
                if probe.data == target:
                    probe.data = data
                    return probe.data
                probe = probe.next
        return None

    def inserting_at_the_beginning(self, data):
        new_item = Node(data)
        if self.head is None:
            self.head = new_item
            self.tail = new_item
        else:
            new_item.next = self.head
            self.head.previous = new_item
            self.head = new_item
        return new_item

    def inserting_at_the_end(self, data):
        new_item = Node(data)
        if self.head is None:
            return self.inserting_at_the_beginning(data)
        else:
            self.tail.next = new_item
            new_item.previous = self.tail
            self.tail = new_item
        return new_item

    def inserting_at_any_position(self, data, index):
        if self.head is None or index <= 0:
            return self.inserting_at_the_beginning(data)
        else:
            new_item = Node(data)
            probe = self.head
            while probe is not None and index - 1 > 0:
                probe = probe.next
                index -= 1
            if probe.next is None:
                return self.inserting_at_the_end(data)
            else:
                new_item.next = probe.next
                new_item.previous = probe
                probe.next.previous = new_item
                probe.next = new_item
        return new_item

    def removing_at_the_beginning(self):
        if self.head is None:
            return None
        elif self.head is self.tail:
            removed_item = self.head.data
            self.head, self.tail = None
        else:
            removed_item = self.head.data
            self.head = self.head.next
            self.head.previous = None
        return removed_item

    def removing_at_the_end(self):
        if self.head is None or self.head is self.tail:
            return self.removing_at_the_beginning()
        else:
            removed_item = self.tail.data
            self.tail = self.tail.previous
            self.tail.next = None
            return removed_item

    def removing_at_any_position(self, index):
        if self.head is None or index <= 0:
            return self.removing_at_the_beginning()
        elif self.head is self.tail:
            return self.removing_at_the_beginning()
        else:
            probe = self.head
            while probe.next is not None and index - 1 > 0:
                probe = probe.next
                index -= 1
            if probe.next is None:
                return self.removing_at_the_end()
            else:
                removed_item = probe.next.data
                probe.next = probe.next.next
                if probe.next is not None:
                    probe.next.previous = probe
            return removed_item
