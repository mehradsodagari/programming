class Node:
    def __init__(self,data):
        self.data=data 
        self.left=None 
        self.right=None 
    def reconstruct_tree_by_preorder(self,inorder,preorder):
        if not inorder or not preorder or len(inorder)!=len(preorder):
            return None
        root_val=preorder[0] 
        root=Node(root_val)
        mid=inorder.index(root_val)
        root.left=self.reconstruct_tree_by_preorder(inorder[:mid],preorder[1:mid+1])
        root.right=self.reconstruct_tree_by_preorder(inorder[mid+1:],preorder[mid+1:])
        return root 
    def reconstruct_tree_by_postorder(self,inorder,postorder):
        if not postorder or not inorder or len(inorder)!=len(postorder):
            return None 
        root_val=postorder[-1] 
        root=Node(root_val)
        mid=inorder.index(root_val) 
        root.left=self.reconstruct_tree_by_postorder(inorder[:mid],postorder[:mid])
        root.right=self.reconstruct_tree_by_postorder(inorder[mid+1:],postorder[mid:-1])
        return root
