class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new_node = TreeNode(val)
        if root is None:
            return new_node
        
        temp = root
        while True:
            if val > temp.val:
                if temp.right:
                    temp = temp.right
                else:
                    temp.right = new_node
                    return root
            else:
                if temp.left:
                    temp = temp.left
                else:
                    temp.left = new_node
                    return root