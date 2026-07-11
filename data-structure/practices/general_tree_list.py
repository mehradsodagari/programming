class GeneralTreeList:
    def __init__(self,data):
        self.data=data 
        self.children=[]
    def add_child(self,child):
        if not isinstance(child,GeneralTreeList):
            raise TypeError('child must be GeneralTreeList')
        self.children.append(child) 
        return child 
    def remove_child(self,data):
        if len(self.children)==0 or data is None:
            return False 
        for index,child in enumerate(self.children):
            if child.data==data:
                self.children.pop(index)
                return True 
        return False 
    def remove_child_by_index(self,index):
        if not 0<=index<len(self.children):
            return False 
        self.children.pop(index)
        return True 
    def get_children(self):
        return self.children.copy()
    def count_children(self):
        return len(self.children)
    def has_child(self,data):
        if data is None or len(self.children)==0:
            return False 
        for child in self.children:
            if child.data==data:
                return True 
        return False 
    def get_child(self,data):
        if data is None or len(self.children)==0:
            return None 
        for child in self.children:
            if child.data==data:
                return child 
        return None 
    def get_child_by_index(self,index):
        if not 0<=index<len(self.children):
            return None 
        return self.children[index] 
    def insert_child_at(self,index,child):
        if not 0<=index<=len(self.children) or  not isinstance(child,GeneralTreeList):
            return False 
        self.children.insert(index,child)
        return True 
    def clear_children(self):
        self.children.clear() 
