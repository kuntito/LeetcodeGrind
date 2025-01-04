# https://leetcode.com/problems/range-sum-of-bst/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# TODO https://neetcode.io/solutions/range-sum-of-bst
class Solution:
    def rangeSumBST(self, root, low: int, high: int) -> int:

        return self.explore(root, low, high)
    
    def explore(self, node, low, high):
        if not node:
            return 0
        
        total = 0
        if low <= node.val <= high:
            total += node.val
            
        total += self.explore(node.left, low, high)
        total += self.explore(node.right, low, high)
        
        return total
    
    