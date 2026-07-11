class TreeNode:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data) 
            self.inorder(node.right) 
    def preorder(self,node):
        if node: 
            print(node.data) 
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
                    print(stack[-1].data) 
                    last_visited=stack.pop()
    def inorder_iterative(self,root):
        stack=[] 
        current=root 
        while current is not None or stack:
            while current:
                stack.append(current) 
                current=current.left 
            current=stack.pop() 
            print(current.data)
            current=current.right
    def preorder_iterative(self,root):
        if not root:
            return None
        stack=[root] 
        while stack:
            node=stack.pop()
            print(node.data)
            if node.right:
                stack.append(node.right) 
            if node.left:
                stack.append(node.left) 
