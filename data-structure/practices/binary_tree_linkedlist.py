class Node:
    def __init__(self,value):
        self.value=value 
        self.left=None 
        self.right=None 
class BinaryTreeLinkedList:
    def __init__(self):
        self.root=None 
        self.__size=0
    def insert_root(self,value):
        if self.root is None:
            self.root=Node(value) 
            self.__size+=1
            return self.root
        return None 
    def insert_left(self,parent,value):
        if parent is None:
            return None
        if parent.left is None:
            parent.left=Node(value) 
            self.__size+=1
            return parent.left
        return None 
    def insert_right(self,parent,value):
        if parent is None:
            return None
        if parent.right is None:
            parent.right=Node(value) 
            self.__size+=1
            return parent.right
        return None 
    def insert_parent(self,node,value):
        if node is None or self.root is None:
            return None 
        if self.root is node:
            new_node=Node(value) 
            new_node.left=self.root 
            self.root=new_node 
            return new_node 
        parent=self.find_parent(node)
        if parent is None:
            return None 
        new_node=Node(value) 
        new_node.left=node 
        if parent.left is node:
            parent.left=new_node 
        else:
            parent.right=new_node 
        self.__size+=1 
        return new_node
    def get_left_child(self,parent):
        if parent is None:
            return None
        if parent.left is not None:
            return parent.left 
        return None 
    def get_right_child(self,parent):
        if parent is None:
            return None
        if parent.right is not None:
            return parent.right 
        return None 
    def find_parent(self,node):
        if node is None or self.root is None or self.root==node:
            return None 
        def _find_parent_recursive(current,target,parent):
            if current is None:
                return None 
            if current is target:
                return parent 
            left_has=_find_parent_recursive(current.left,target,current) 
            if left_has:
                return left_has 
            return _find_parent_recursive(current.right,target,current) 
        return _find_parent_recursive(self.root,node,None)
    def get_size(self):
        return self.__size 
    def is_empty(self):
        return self.root is None
    def find_leaves(self):
        if self.is_empty():
            return 'tree is empty'
        leaves=[] 
        def _find_leaves_recursive(node):
            if node:
                if node.left is None and node.right is None:
                    leaves.append(str(node.value)) 
                else:
                    _find_leaves_recursive(node.left)
                    _find_leaves_recursive(node.right) 
        _find_leaves_recursive(self.root)
        return '.'.join(leaves) if leaves else "tree has no leaves"
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right) 
    def preorder(self,node):
        if node:
            print(node.value)
            self.preorder(node.left)
            self.preorder(node.right) 
    def postorder_iterative(self,root):
        if root is None:
            return None
        stack=[]
        current=root 
        last_visited=None 
        while current or stack:
            if current:
                stack.append(current)
                current=current.left
            else:
                if stack[-1].right and stack[-1].right!=last_visited:
                    current=stack[-1].right 
                else:
                    print(stack[-1].value) 
                    last_visited=stack.pop() 
    def inorder_iterative(self,root):
        if root is None:
            return None
        stack=[]
        current=root 
        while current is not None or stack:
            while current:
                stack.append(current)
                current=current.left 
            current=stack.pop() 
            print(current.value) 
            current=current.right 
    def preorder_iterative(self,root):
        if root is None:
            return None 
        stack=[root] 
        while stack:
            node=stack.pop() 
            print(node.value) 
            if node.right:
                stack.append(node.right) 
            if node.left:
                stack.append(node.left) 
        
