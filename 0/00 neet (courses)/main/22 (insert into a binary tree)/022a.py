# https://leetcode.com/problems/insert-into-a-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def explore_insert(self, node: TreeNode):
        if node is None:
            return TreeNode(self.val)
        
        if self.val > node.val:
            node.right = self.explore_insert(node.right)
        else:
            node.left = self.explore_insert(node.left)

        return node

    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        self.val = val
        self.explore_insert(root)
