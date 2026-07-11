class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        self.previous=None 
class CircularDoublyLinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None 
        self.__size=0
    def __len__(self):
        return self.__size 
    def is_empty(self):
        return self.__size==0
    def __str__(self):
        if not self.head:
            return "[]"
        parts = []
        probe = self.head
        while True:
            parts.append(str(probe.data))
            probe = probe.next
            if probe == self.head:
                break
        return " ↔ ".join(parts) + " ↔ (head)"
    def __iter__(self):
        if not self.head:
            return
        probe = self.head
        while True:
            yield probe
            probe = probe.next
            if probe == self.head:
                break
    def searching(self,target):
        if self.head is None:
            return None 
        probe=self.head 
        while True:
            if probe.data==target:
                return probe.data 
            probe=probe.next 
            if probe is self.head:
                break 
        return 
    def replacement(self,target,new_data):
        if self.head is None:
            return None 
        probe=self.head 
        while True:
            if probe.data==target:
                probe.data=new_data 
                return probe.data 
            probe=probe.next 
            if probe is self.head:
                break 
        return None
    def insert_beginning(self,data):
        new_item=Node(data)
        if self.head is None:
            new_item.next=new_item 
            new_item.previous=new_item 
            self.head=self.tail=new_item 
        else:
            self.tail.next=new_item 
            new_item.previous=self.tail 
            new_item.next=self.head 
            self.head.previous=new_item 
            self.head=new_item 
        self.__size+=1
        return new_item 
    def insert_end(self,data):
        if self.head is None:
            return self.insert_beginning(data) 
        new_item=Node(data)
        self.tail.next=new_item 
        new_item.previous=self.tail 
        new_item.next=self.head 
        self.head.previous=new_item 
        self.tail=new_item
        self.__size+=1 
        return new_item 
    def insert_any_position(self,data,index):
        if self.head is None or index==0:
            return self.insert_beginning(data) 
        if index<0:
            return None 
        if index>=self.__size:
            return self.insert_end(data) 
        probe=self.head 
        while probe.next!=self.head and index>1:
            probe=probe.next 
            index-=1 
        new_item=Node(data) 
        new_item.next=probe.next 
        probe.next.previous=new_item 
        probe.next=new_item 
        new_item.previous=probe 
        self.__size+=1
        return new_item
    def remove_beginning(self):
        if self.head is None:
            return None 
        removed_item=self.head.data 
        if self.head is self.tail:
            self.head=self.tail=None 
        else:
            self.tail.next=self.head.next 
            self.head.next.previous=self.tail 
            self.head=self.head.next
        self.__size-=1 
        return removed_item 
    def remove_end(self):
        if self.head is None or self.head is self.tail:
            return self.remove_beginning() 
        removed_item=self.tail.data 
        self.tail.previous.next=self.head 
        self.head.previous=self.tail.previous 
        self.tail=self.tail.previous 
        self.__size-=1
        return removed_item 
    def remove_any_position(self,index):
        if self.head is None or self.head is self.tail or index==0:
            return self.remove_beginning() 
        if index<0:
            return None
        if index==self.__size-1:
            return self.remove_end() 
        if index>self.__size:
            return None 
        probe=self.head 
        while probe.next!=self.head and index>1:
            probe=probe.next 
            index-=1 
        removed_item=probe.next.data  
        probe.next=probe.next.next
        probe.next.next.previous=probe 
        self.__size-=1
        return removed_item
import unittest

class TestCircularDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.cdll = CircularDoublyLinkedList()

    def test_empty_list(self):
        self.assertTrue(self.cdll.is_empty())
        self.assertEqual(len(self.cdll), 0)
        self.assertEqual(str(self.cdll), "[]")

    def test_insert_beginning_single(self):
        self.cdll.insert_beginning(42)
        self.assertEqual(len(self.cdll), 1)
        self.assertEqual(str(self.cdll), "42 ↔ (head)")

    def test_insert_end_multiple(self):
        self.cdll.insert_end(10)
        self.cdll.insert_end(20)
        self.cdll.insert_end(30)
        self.assertEqual(len(self.cdll), 3)
        self.assertEqual(str(self.cdll), "10 ↔ 20 ↔ 30 ↔ (head)")

    def test_insert_beginning_multiple(self):
        self.cdll.insert_beginning(10)
        self.cdll.insert_beginning(20)
        self.cdll.insert_beginning(30)
        self.assertEqual(len(self.cdll), 3)
        self.assertEqual(str(self.cdll), "30 ↔ 20 ↔ 10 ↔ (head)")

    def test_insert_any_position(self):
        self.cdll.insert_end(10)
        self.cdll.insert_end(30)
        self.cdll.insert_any_position(20, 1)  # بین 10 و 30
        self.assertEqual(str(self.cdll), "10 ↔ 20 ↔ 30 ↔ (head)")

        self.cdll.insert_any_position(5, 0)   # اول لیست
        self.assertEqual(str(self.cdll), "5 ↔ 10 ↔ 20 ↔ 30 ↔ (head)")

        self.cdll.insert_any_position(999, 4) # آخر لیست
        self.assertEqual(str(self.cdll), "5 ↔ 10 ↔ 20 ↔ 30 ↔ 999 ↔ (head)")

    def test_remove_beginning(self):
        self.cdll.insert_end(10)
        self.cdll.insert_end(20)
        self.cdll.insert_end(30)
        self.cdll.remove_beginning()
        self.assertEqual(str(self.cdll), "20 ↔ 30 ↔ (head)")

    def test_remove_end(self):
        self.cdll.insert_end(10)
        self.cdll.insert_end(20)
        self.cdll.insert_end(30)
        self.cdll.remove_end()
        self.assertEqual(str(self.cdll), "10 ↔ 20 ↔ (head)")

    def test_remove_any_position(self):
        self.cdll.insert_end(10)
        self.cdll.insert_end(20)
        self.cdll.insert_end(30)
        self.cdll.insert_end(40)
        self.cdll.remove_any_position(1)  # حذف 20
        self.assertEqual(str(self.cdll), "10 ↔ 30 ↔ 40 ↔ (head)")

        self.cdll.remove_any_position(2)  # حذف 40
        self.assertEqual(str(self.cdll), "10 ↔ 30 ↔ (head)")

    def test_search_and_replace(self):
        self.cdll.insert_end(100)
        self.cdll.insert_end(200)
        self.cdll.insert_end(300)

        self.assertEqual(self.cdll.searching(200), 200)
        self.assertIsNone(self.cdll.searching(999))

        self.cdll.replacement(200, 888)
        self.assertEqual(self.cdll.searching(888), 888)
        self.assertEqual(str(self.cdll), "100 ↔ 888 ↔ 300 ↔ (head)")

    def test_remove_until_empty(self):
        self.cdll.insert_end(1)
        self.cdll.insert_end(2)
        self.cdll.insert_end(3)

        self.cdll.remove_beginning()
        self.cdll.remove_end()
        self.cdll.remove_any_position(0)

        self.assertTrue(self.cdll.is_empty())
        self.assertEqual(len(self.cdll), 0)
        self.assertEqual(str(self.cdll), "[]")

    def test_iter(self):
        values = [10, 20, 30]
        for v in values:
            self.cdll.insert_end(v)
        
        result = [node.data for node in self.cdll]
        self.assertEqual(result, [10, 20, 30])


if __name__ == '__main__':
    unittest.main(verbosity=2)
