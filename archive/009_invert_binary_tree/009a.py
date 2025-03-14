# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode):
        return self.explore_inversion(root)
    
    def explore_inversion(self, node):
        if not node: return

        temp = node.left
        node.left = node.right
        node.right = temp

        self.explore_inversion(node.left)
        self.explore_inversion(node.right)

        return node