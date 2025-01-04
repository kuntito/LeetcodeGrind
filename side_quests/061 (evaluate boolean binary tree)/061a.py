# https://leetcode.com/problems/evaluate-boolean-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TODO https://neetcode.io/solutions/evaluate-boolean-binary-tree
class Solution:
    def evaluateTree(self, root) -> bool:
        # recursively explore each node and it's children
        # if you reach a leaf node, return it's value `0` or `1`
        if not root: return False
        if not (root.left or root.right):
            return bool(root.val)
        
        # if it's not a leaf node: 
        
        # if node.val == 2: return explore(node.left) OR explore(node.right)
        # else return return explore(node.left) AND explore(node.right)
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        return (left and right) if root.val == 3 else (left or right)
        
        