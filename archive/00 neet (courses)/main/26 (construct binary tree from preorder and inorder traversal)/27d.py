from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(
        self, 
        preorder: List[int],
        inorder: List[int]
    ) -> Optional[TreeNode]:
        return self.explore(preorder, inorder)
    
    def explore(
        self,
        preorder: List[int],
        inorder: List[int]
    ):
        if not preorder:
            return None
        
        rootVal = preorder[0]
        
        # find rootVal in `inorder`
        idx = inorder.index(rootVal)
        
        leftInorder = inorder[:idx]
        rightInorder = inorder[idx+1:]
        
        leftPreorder = preorder[1:len(leftInorder) + 1]
        rightPreorder = preorder[len(leftInorder) + 1:]
        
        leftSubtree = self.explore(leftPreorder, leftInorder)
        rightSubtree = self.explore(rightPreorder, rightInorder)
        
        node = TreeNode(rootVal)
        
        node.left = leftSubtree
        node.right = rightSubtree
        
        return node
        
        