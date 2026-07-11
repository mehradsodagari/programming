class Node:
    def __init__(self,data,next=None):
        self.data=data 
        self.next=next 
class CircularLinkedList:
    def __init__(self,head=None,tail=None):
        self.head=head 
        self.tail=tail 
        self.__size=0
    def traversal(self):
        if self.head is None:
            return 'list is empty'
        probe=self.head
        while probe!=self.tail:
            print(probe.data,'\n')
            probe=probe.next
        print(self.tail.data)
    def searching(self,target):
        if self.head is None:
            return 'list is empty' 
        probe=self.head 
        while probe!=self.tail and probe.data!=target:
            probe=probe.next
        if self.tail.data==target:
            return self.tail.data
        if probe is self.tail:
            return 'target not found' 
        return probe.data
    def replacement(self,target,new_data):
        if self.head is None:
            return 'list is empty'
        probe=self.head 
        while probe!=self.tail and probe.data!=target:
            probe=probe.next 
        if self.tail.data==target:
            self.tail.data=new_data 
            return self.tail.data
        if probe is self.tail:
            return 'target not found'
        probe.data=new_data 
        return probe.data
    def inserting_at_the_beginning(self,data):
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
        return new_item 
    def inserting_at_the_end(self,data):
        if self.head is None:
            return self.inserting_at_the_beginning(data)
        new_item=Node(data) 
        self.tail.next=new_item 
        new_item.next=self.head 
        self.tail=new_item 
        self.__size+=1
        return new_item 
    def inserting_at_any_position(self,data,index):
        if self.head is None or index<=0:
            return self.inserting_at_the_beginning(data)
        if index>self.__size:
            return self.inserting_at_the_end(data)
        probe=self.head 
        new_item=Node(data)
        while probe!=None and index>1:
            probe=probe.next
            index-=1
        new_item.next=probe.next 
        probe.next=new_item 
        return new_item
    def removing_at_the_beginning(self):
        if self.head is None:
            return 'list is empty'
        removed_item=self.head.data
        self.head=self.head.next 
        self.tail.next=self.head 
        self.__size-=1
        return removed_item
    def removing_at_the_end(self):
        if self.head is None:
            return 'list is empty'
        if self.head.next==self.tail:
            return self.removing_at_the_beginning()
        probe=self.head 
        while probe.next!=self.tail:
            probe=probe.next
        removed_item=self.tail.data
        probe.next=self.head 
        self.tail=probe
        self.__size-=1
        return removed_item
    def removing_at_any_position(self,index):
        if self.head is None:
            return 'list is empty' 
        if index<=0:
            return self.removing_at_the_beginning() 
        if index>self.__size:
            return self.removing_at_the_end() 
        probe=self.head 
        while probe!=None and index>1:
            probe=probe.next 
            index-=1 
        if probe.next==self.tail:
            return self.removing_at_the_end() 
        removed_item=probe.next.data
        probe.next=probe.next.next 
        self.__size-=1
        return removed_item
