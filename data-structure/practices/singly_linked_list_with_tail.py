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
    def __str__(self):
        if self.head is None:
                return '[]'
        parts = []
        probe = self.head
        while probe is not None:
            parts.append(str(probe.data))
            probe = probe.next
        return '[' + ' -> '.join(parts) + ']' 
    def is_empty(self):
        return self.__size==0
    def searching(self,target):
        if self.head is None:
            return None 
        probe=self.head 
        while probe is not None and probe.data is not target: 
            probe=probe.next 
        if probe is None:
            return None 
        return probe.data 
    def replacement(self,target,new_data):
        if self.head is None:
            return None 
        probe=self.head 
        while probe is not None and probe.data is not target: 
            probe=probe.next 
        if probe is None:
            return None  
        probe.data=new_data
        return probe.data
    def insert_beginning(self,data):
        new_item=Node(data) 
        if self.head is None:
            self.head=new_item 
            self.tail=new_item
        else:
            new_item.next=self.head 
            self.head=new_item 
        self.__size+=1
        return new_item.data 
    def insert_end(self,data):
        if self.head is None:
            return self.insert_beginning(data) 
        new_item=Node(data) 
        self.tail.next=new_item 
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
        while probe.next!=None and index>1:
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
            self.head=self.tail=None 
        else:
            self.head=self.head.next
        self.__size-=1 
        return removed_item 
    def remove_end(self):
        if self.head is None:
            return None 
        if self.head is self.tail:
            return self.remove_beginning() 
        removed_item=self.tail.data
        if self.head.next is self.tail:
            self.tail=self.head
        else:
            probe=self.head 
            while probe.next.next is not None:
                probe=probe.next 
            probe.next=None 
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
        while probe.next is not None and index>1:
            probe=probe.next 
            index-=1 
        removed_item=probe.next.data 
        probe.next=probe.next.next 
        self.__size-=1
        return removed_item
