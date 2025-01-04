# https://leetcode.com/problems/merge-two-binary-trees/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# TODO https://neetcode.io/practice
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode):
        pass
        # recursively explore both nodes, merge them into `root1`
        # explore their left and right children
        # if both nodes are `None`, return None
        # if either is `None`, consider, it's value `0` and add it to
        # the node with a value
        # if both nodes are valid, add their values
        return self.explore(root1, root2)
        
        
    def explore(self, uno, dos):
        if not uno and not dos:
            return None
        
        if uno and dos:
            uno.val += dos.val
        elif dos:
            uno = TreeNode(
                val=dos.val
            )
            
        uno.left = self.explore(
            uno.left,
            dos.left if dos else None
        )
        
        uno.right = self.explore(
            uno.right,
            dos.right if dos else None
        )
        
        return uno
    

    
TreeNode(1)
TreeNode(3)
TreeNode(2)
TreeNode(5)