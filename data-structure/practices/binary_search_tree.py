class BinarySearchTree:
    def __init__(self,key):
        self.key=key 
        self.left=None 
        self.right=None 
    def insert_BST(self,root,key):
        if root is None:
            return BinarySearchTree(key) 
        if key<root.key:
            root.left=self.insert_BST(root.left,key)
        elif key>root.key:
            root.right=self.insert_BST(root.right,key) 
        return root 
    def delete_BST(self,root,key):
        if root is None:
            return root 
        if key<root.key:
            root.left=self.delete_BST(root.left,key) 
        elif key>root.key:
            root.right=self.delete_BST(root.right,key) 
        else:
            if root.left is None:
                return root.right 
            if root.right is None:
                return root.left 
            temp=self.find_min(root.right) 
            root.key=temp.key 
            root.right=self.delete_BST(root.right,temp.key)
        return root 
    def find_min(self,node):
        current=node 
        while current.left:
            current=current.left 
        return current 
    def find_max(self,node):
        current=node 
        while current.right:
            current=current.right 
        return current
    def search(self,root,key):
        if root is None or root.key==key:
            return root
        if key<root.key:
            return self.search(root.left,key) 
        return self.search(root.right,key)
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.key)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.key) 
            self.inorder(node.right) 
    def preorder(self,node):
        if node: 
            print(node.key) 
            self.preorder(node.left) 
            self.preorder(node.right) 
    def postorder_iterative(self,root):
        stack=[]
        current=root 
        last_visited=None 
        while stack or current:
            if current:
                stack.append(current)
                current=current.left 
            else:
                if stack[-1].right and last_visited!=stack[-1].right:
                    current=stack[-1].right 
                else:
                    print(stack[-1].key) 
                    last_visited=stack.pop()
    def inorder_iterative(self,root):
        stack=[] 
        current=root 
        while current is not None or stack:
            while current:
                stack.append(current) 
                current=current.left 
            current=stack.pop() 
            print(current.key)
            current=current.right
    def preorder_iterative(self,root):
        if not root:
            return None
        stack=[root] 
        while stack:
            node=stack.pop()
            print(node.key)
            if node.right:
                stack.append(node.right) 
            if node.left:
                stack.append(node.left) 
