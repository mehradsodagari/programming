class BinaryTreeList:
    def __init__(self,size):
        self.tree=[None]*size 
    def insert_root(self,value):
        if self.tree[0] is None or self.is_empty():
            self.tree[0]=value 
            return 0 
        return -1
    def insert_left(self,index,value):
        if index<0 or index>=len(self.tree) or self.tree[index] is None:
            return None 
        left_index=2*index+1 
        if left_index<len(self.tree):
            if self.tree[left_index] is None:
                self.tree[left_index]=value 
                return True 
        return None 
    def insert_right(self,index,value):
        if index<0 or index>=len(self.tree) or self.tree[index] is None:
            return None 
        right_index=2*index+2 
        if right_index<len(self.tree):
            if self.tree[right_index] is None:
                self.tree[right_index]=value 
                return True 
        return None 
    def insert_parent(self,index,value):
        if index<0 or index>=len(self.tree):
            return None 
        parent_index=(index-1)//2 
        if 0<=parent_index<len(self.tree):
            if self.tree[parent_index] is None:
                self.tree[parent_index]=value 
                return True 
        return None 
    def get_left_child(self,index):
        if index<0 or index>=len(self.tree):
            return None 
        left_index=2*index+1 
        if left_index<len(self.tree):
            return self.tree[left_index] 
        return None 
    def get_right_child(self,index):
        if index<0 or index>=len(self.tree):
            return None 
        right_index=2*index+2 
        if right_index<len(self.tree):
            return self.tree[right_index] 
        return None 
    def find_parent(self,index):
        if index<=0 or index>=len(self.tree):
            return None 
        parent=(index-1)//2 
        if 0<=parent<len(self.tree):
            return self.tree[parent] 
        return None
    def get_size(self):
        return len(self.tree)
    def is_empty(self):
        return all(element is None for element in self.tree) or len(self.tree)==0
    def find_leaves(self):
        if self.is_empty():
            return None
        leaves=[]
        for index in range(len(self.tree)):
            left_index=2*index+1 
            right_index=2*index+2      
            if self.tree[index] is not None:
                condition1=left_index>=len(self.tree) and right_index>=len(self.tree)
                condition2=False
                if left_index<len(self.tree) and right_index<len(self.tree):
                    condition2=self.tree[left_index] is None and self.tree[right_index] is None
                elif left_index>=len(self.tree) and right_index>=len(self.tree):
                    condition2=True
                if condition1 or condition2:
                    leaves.append(str(self.tree[index]))   
        return ' '.join(leaves) if leaves else "there are no leaves"
    def postorder(self,node_index):
        if 0<=node_index<len(self.tree): 
            if self.tree[node_index] is not None:
                left_child=2*node_index+1 
                right_child=2*node_index+2
                if left_child<len(self.tree):
                    self.postorder(left_child) 
                if right_child<len(self.tree):
                    self.postorder(right_child) 
                print(self.tree[node_index])
    def inorder(self,node_index):
        if 0<=node_index<len(self.tree):
            if self.tree[node_index] is not None:
                left_child=2*node_index+1 
                right_child=2*node_index+2
                if left_child<len(self.tree):
                    self.inorder(left_child)
                print(self.tree[node_index])
                if right_child<len(self.tree):
                    self.inorder(right_child)
    def preorder(self,node_index):
        if 0<=node_index<len(self.tree):
            if self.tree[node_index] is not None:
                left_child=2*node_index+1 
                right_child=2*node_index+2
                print(self.tree[node_index])
                if left_child<len(self.tree):
                    self.preorder(left_child)
                if right_child<len(self.tree):
                    self.preorder(right_child)
    def postorder_iterative(self,root_index):
        if not 0<=root_index<len(self.tree) or self.tree[root_index] is None:
            return None
        stack=[] 
        current=root_index 
        last_visited=-1
        while stack or (0<=current<len(self.tree) and self.tree[current] is not None):
            while 0<=current<len(self.tree) and self.tree[current] is not None:
                stack.append(current) 
                left_child=2*current+1 
                current=left_child if left_child<len(self.tree) else -1 
            peek_node=stack[-1] if stack else -1 
            right_child=2*peek_node+2
            if (0<=right_child<len(self.tree) and 
                self.tree[right_child] is not None and
                last_visited!=right_child):
                current=right_child 
            else:
                print(self.tree[peek_node])
                last_visited=stack.pop() 
                current=-1
    def inorder_iterative(self,root_index):
        if not 0<=root_index<len(self.tree) or self.tree[root_index] is None:
            return None 
        stack=[]
        current=root_index 
        while stack or (0<=current<len(self.tree) and self.tree[current] is not None):
            while 0<=current<len(self.tree) and self.tree[current] is not None:
                stack.append(current)
                left_child=2*current+1 
                current=left_child if left_child<len(self.tree) else -1  
            current=stack.pop() 
            print(self.tree[current]) 
            right_child=2*current+2 
            current=right_child if (right_child<len(self.tree) and
                                    self.tree[right_child] is not None) else -1
    def preorder_iterative(self,root_index):
        if not 0<=root_index<len(self.tree) or self.tree[root_index] is None:
            return None 
        stack=[root_index]
        while stack:
            parent=stack.pop()
            print(self.tree[parent])
            if 2*parent+2<len(self.tree):
                if self.tree[2*parent+2] is not None:
                    stack.append(2*parent+2)
            if 2*parent+1<len(self.tree):
                if self.tree[2*parent+1] is not None:
                    stack.append(2*parent+1)
