class GeneralTreeNodeLinkedList:
    def __init__(self,data):
        self.data=data 
        self.first_child=None 
        self.next_sibling=None
    def add_child(self,child):
        if not isinstance(child,GeneralTreeNodeLinkedList):
            raise TypeError('child must be GeneralTreeNodeLinkedList')
        if not self.first_child:
            self.first_child=child 
            return child 
        current=self.first_child 
        while current.next_sibling:
            current=current.next_sibling 
        current.next_sibling=child 
        return child 
    def remove_child(self,data):
        if self.first_child is None:
            return False 
        if self.first_child.data==data:
            self.first_child=self.first_child.next_sibling
            return True
        current=self.first_child 
        while current.next_sibling:
            if current.next_sibling.data==data:
                current.next_sibling=current.next_sibling.next_sibling 
                return True 
            current=current.next_sibling 
        return False 
    def get_children(self):
        children=[] 
        current=self.first_child 
        while current:
            children.append(current)
            current=current.next_sibling 
        return children 
    def count_children(self):
        count=0 
        current=self.first_child 
        while current:
            count+=1 
            current=current.next_sibling 
        return count 
    def has_child(self,data):
        if self.first_child is None or data is None:
            return False
        current=self.first_child 
        while current:
            if current.data==data:
                return True 
            current=current.next_sibling 
        return False 
