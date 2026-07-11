class Node:
    def __init__(self,data):
        self.data=data 
        self.next=None 
class SinglyLinkedList:
    def __init__(self):
        self.head=None 
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
        else:
            new_item.next=self.head 
            self.head=new_item
        self.__size+=1 
        return new_item.data 
    def insert_end(self,data):
        if self.head is None:
            return self.insert_beginning(data) 
        probe=self.head 
        while probe.next!=None:
            probe=probe.next 
        new_item=Node(data)
        probe.next=new_item 
        self.__size+=1
        return new_item.data 
    def insert_any_position(self,data,index):
        if self.head is None or index==0:
            return self.insert_beginning(data)
        if index<0:
            return None
        if index>self.__size:
            return None
        if index==self.__size:
            return self.insert_end(data)
        probe=self.head 
        while probe!=None and index>1:
            probe=probe.next
            index-=1 
        if probe is None:
            return self.insert_end(data) 
        new_item=Node(data) 
        new_item.next=probe.next 
        probe.next=new_item 
        self.__size+=1
        return new_item.data
    def remove_beginning(self):
        if self.head is None:
            return 
        removed_item=self.head.data
        if self.head.next is None:
            self.head=None 
        else:
            self.head=self.head.next 
        self.__size-=1
        return removed_item
    def remove_end(self):
        if self.head is None:
            return
        if self.head.next is None:
            return self.remove_beginning() 
        probe=self.head 
        while probe.next.next!=None:
            probe=probe.next
        removed_item=probe.next.data 
        probe.next=None 
        self.__size-=1
        return removed_item
    def remove_any_position(self,index):
        if self.head is None:
            return
        if self.head.next is None or index==0:
            return self.remove_beginning()
        if index<0:
            return None
        if index>self.__size:
            return None
        probe=self.head 
        while probe.next!=None and index>1:
            probe=probe.next 
            index-=1 
        if probe.next is None:
            return self.remove_end() 
        removed_item=probe.next.data
        probe.next=probe.next.next
        self.__size-=1 
        return removed_item 
