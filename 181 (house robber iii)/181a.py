# https://leetcode.com/problems/house-robber-iii/description/

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
    def rob(self, root: TreeNode) -> int:
        pass
    
        self.explore(root)
        
    # TODO critique your assumptions
    # each node should return it's streak and the streak of it's children
    def explore(self, node):
        if self.is_leaf(node):
            return (node.val, 0)
        
        # here you want to find out which is greater
        # node.val + node.next.next OR node.next
        
        leftRes, leftNextRes = 0, 0
        if node.left:
            leftRes, leftNextRes = self.explore(node.left)
            

        rightRes, rightNextRes = 0, 0
        if node.right:
            rightRes, rightNextRes = self.explore(node.right)
            
        
        
        
        
    def is_leaf(self, node):
        return node.left is None and node.right is None
    
four = TreeNode(4)
one = TreeNode(1)
three = TreeNode(3)

four.left = one
four.right = three

sol = Solution()
sol.rob(four)