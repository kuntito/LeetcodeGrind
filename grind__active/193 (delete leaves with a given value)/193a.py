# https://leetcode.com/problems/delete-leaves-with-a-given-value/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'
        

class Solution:
    def removeLeafNodes(self, root: TreeNode, target: int):
        pass
    
        # a recursive function that checks the left and right children for leaf nodes
        # each call returns the None if a leaf node is found or the node itself
        
        # i.e. node.left = self.explore(node.left)
        # when node.left and node.right are updated
        # check if `node` is a leaf node and return accordingly
        
        if not root:
            return None
        
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        
        return None if self.is_leaf(root) and root.val == target else root
    
    def is_leaf(self, root):
        return root.left is None and root.right is None

    
one = TreeNode(1)    
two = TreeNode(2)    
three = TreeNode(3)    
twotwo = TreeNode(2)    
twotwotwo = TreeNode(2)    
four = TreeNode(4)

three.left = twotwotwo
three.right = four

two.left = twotwo
one.left = two
one.right = three

sol = Solution()
res = sol.removeLeafNodes(one, 2)
print(res)