class AVlNode:
    def __init__(self,key):
        self.key=key 
        self.left=None 
        self.right=None 
        self.height=1 
class AVlTree:
    def __init__(self):
        self.root=None
    def height(self,node):
        return node.height if node else 0 
    def update_height(self,node):
        if node:
            node.height=1+max(self.height(node.left),self.height(node.right))
    def balance_factor(self,node):
        return self.height(node.left)-self.height(node.right) if node else 0 
    def rotate_right(self,x):
        y=x.left 
        T2=y.right 
        y.right=x 
        x.left=T2 
        self.update_height(y)
        self.update_height(x) 
        return y 
    def rotate_left(self,x):
        y=x.right 
        T2=y.left 
        y.left=x
        x.right=T2
        self.update_height(y)
        self.update_height(x)
        return y 
    def balance(self,node):
        b=self.balance_factor(node)
        if b>1:
            if self.balance_factor(node.left)>=0:
                return self.rotate_right(node) 
            else:
                node.left=self.rotate_left(node.left)
                return self.rotate_right(node) 
        if b<-1:
            if self.balance_factor(node.right)<=0:
                return self.rotate_left(node) 
            else:
                node.right=self.rotate_right(node.right)
                return self.rotate_left(node) 
        return node 
    def insert(self,root,key):
        if root is None:
            return AVlNode(key) 
        if key<root.key:
            root.left=self.insert(root.left,key)
        elif key>root.key:
            root.right=self.insert(root.right,key) 
        else:
            return root
        self.update_height(root)
        return self.balance(root) 
    def insert_key(self,key):
        self.root=self.insert(self.root,key)
    def delete(self,root,key):
        if root is None:
            return root 
        if key<root.key:
            root.left=self.delete(root.left,key) 
        elif key>root.key:
            root.right=self.delete(root.right,key) 
        else:
            if root.left is None:
                return root.right 
            if root.right is None:
                return root.left 
            temp=self.find_min(root.right) 
            root.key=temp.key 
            root.right=self.delete(root.right,temp.key)
        if not root:
            return root 
        self.update_height(root) 
        return self.balance(root)
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
    def search_key(self,key):
        return self.search(self.root,key)
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
