class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
        self.previous=None 
class DoublyLinkedList:
    def __init__(self):
        self.head=None 
        self.tail=None
        self.__size=0 
    def __len__(self):
        return self.__size 
    def is_empty(self):
        return self.__size==0
    def __iter__(self):
        probe = self.head
        while probe:
            yield probe       
            probe = probe.next
    def __str__(self):
        if not self.head:
            return "[]"
        return " ↔ ".join(str(node.data) for node in self) 
    def searching(self,target):
        if self.head is None:
            return None 
        probe=self.head 
        while probe!=None and probe.data!=target:
            probe=probe.next 
        if probe is None:
            return None 
        return probe.data 
    def replacement(self,target,new_data):
        if self.head is None:
            return None 
        probe=self.head 
        while probe!=None and probe.data!=target:
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
        self.tail=new_item 
        self.__size+=1
        return new_item
    def insert_any_position(self,data,index):
        if self.head is None or index==0:
            return self.insert_beginning(data) 
        if index<0:
            return None 
        probe=self.head 
        if index>=self.__size:
            return self.insert_end(data)
        while probe!=None and index>1:
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
            self.head=self.head.next 
            self.head.previous=None
        self.__size-=1
        return removed_item 
    def remove_end(self):
        if self.head is None or self.head is self.tail:
            return self.remove_beginning() 
        removed_item=self.tail.data 
        self.tail=self.tail.previous 
        self.tail.next=None 
        self.__size-=1
        return removed_item 
    def remove_any_position(self,index):
        if self.head is None or index==0 or self.head is self.tail:
            return self.remove_beginning() 
        if index>=self.__size or index<0:
            return None 
        if index==self.__size-1:
            return self.remove_end()
        probe=self.head 
        while probe!=None and index>1:
            probe=probe.next 
            index-=1 
        removed_item=probe.next.data 
        probe.next=probe.next.next 
        probe.next.next.previous=probe
        self.__size-=1
        return removed_item
