class ArrayBinaryTree:
    def __init__(self):
        self.tree=[] 
    def insert(self,value):
        self.tree.append(value) 
    def left_child(self,index):
        if not 0<=index<len(self.tree):
            return None
        left=2*index+1 
        if left<len(self.tree):
            return self.tree[left] 
        return None 
    def right_child(self,index):
        if not 0<=index<len(self.tree):
            return None
        right=2*index+2 
        if right<len(self.tree):
            return self.tree[right]
        return None 
    def parent(self,index):
        if not 0<index<len(self.tree):
            return None
        parent=(index-1)//2 
        return self.tree[parent] 
    def find_leaves(self):
        leaves=[] 
        for index in range(len(self.tree)):
            left=2*index+1 
            right=2*index+2 
            if left>=len(self.tree) and right>=len(self.tree):
                leaves.append(self.tree[index])
        return leaves if leaves else None 
    