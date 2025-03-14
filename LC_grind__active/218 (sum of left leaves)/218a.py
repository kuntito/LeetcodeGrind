# https://leetcode.com/problems/sum-of-left-leaves/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.explore(root, False)

    def explore(self, node, isLeft):
        res = 0
        if not node:
            return res

        if isLeft and self.isLeaf(node):
            res += node.val

        res += self.explore(node.left, True)
        res += self.explore(node.right, False)

        return res

    def isLeaf(self, node):
        return node.left is None and node.right is None