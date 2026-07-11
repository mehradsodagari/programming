class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class SinglyLinkedList:
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
        return "[" + " → ".join(parts) + " → (head)]"
    def searching(self,target):
        if self.head is None:
            return None 
        if self.head is self.tail and self.head.data==target:
            return self.head.data
        probe=self.head 
        while probe is not self.head.next and probe.data is not target: 
            probe=probe.next  
        if self.tail.data==target:
            return self.tail.data
        if probe is self.head.next:
            return None 
        return probe.data 
    def replacement(self,target,new_data):
        if self.head is None:
            return None 
        if self.head is self.tail and self.head.data==target:
            self.head.data=new_data
            return self.head.data
        probe=self.head 
        while probe is not self.head.next and probe.data is not target: 
            probe=probe.next  
        if self.tail.data==target:
            self.tail.data=new_data
            return self.tail.data
        if probe is self.head.next:
            return None 
        probe.data=new_data
        return probe.data 
    def insert_beginning(self,data):
        new_item=Node(data) 
        if self.head is None:
            new_item.next=new_item
            self.head=new_item 
            self.tail=new_item
        else:
            new_item.next=self.head 
            self.tail.next=new_item
            self.head=new_item 
        self.__size+=1
        return new_item.data 
    def insert_end(self,data):
        if self.head is None:
            return self.insert_beginning(data) 
        new_item=Node(data) 
        self.tail.next=new_item 
        new_item.next=self.head
        self.tail=new_item 
        self.__size+=1
        return new_item.data 
    def insert_any_position(self,data,index):
        if self.head is None or index==0:
            return self.insert_beginning(data)
        if index<0:
            return None 
        if index==self.__size:
            return self.insert_end(data)
        if index>self.__size:
            return None 
        probe=self.head 
        while probe.next!=self.head and index>1:
            probe=probe.next 
        new_item=Node(data) 
        new_item.next=probe.next 
        probe.next=new_item
        self.__size+=1 
        return new_item.data 
    def remove_beginning(self):
        if self.head is None:
            return None 
        removed_item=self.head.data
        if self.head is self.tail:
            self.head=self.head=None 
        else:
            self.head=self.head.next
            self.tail.next=self.head
        self.__size-=1 
        return removed_item 
    def remove_end(self):
        if self.head is None:
            return None 
        if self.head is self.tail:
            return self.remove_beginning() 
        removed_item=self.tail.data
        if self.head.next is self.tail:
            self.tail = self.head
            self.head.next = self.head
        else:
            probe=self.head 
            while probe.next.next is not self.head:
                probe=probe.next 
            probe.next=self.head 
            self.tail=probe
        self.__size-=1 
        return removed_item 
    def remove_any_position(self,index):
        if self.head is None:
            return None 
        if self.head is self.tail or index==0:
            return self.remove_beginning() 
        if index>=self.__size:
            return None 
        if index==self.__size-1:
            return self.remove_end()
        probe=self.head 
        while probe.next is not self.head and index>1:
            probe=probe.next 
            index-=1 
        removed_item=probe.next.data 
        probe.next=probe.next.next 
        self.__size-=1
        return removed_item
