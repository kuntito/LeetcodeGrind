# https://leetcode.com/problems/validate-binary-search-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_border = float("-infinity")
        max_border = float("infinity")

        return self.explore(root, min_border, max_border)
    
    def explore(self, node, min_border, max_border):
        if not node: return True
        if node.val >= max_border or node.val <= min_border: return False

        return self.explore(
            node.left,
            min_border,
            node.val
        ) and self.explore(
            node.right,
            node.val,
            max_border
        )
    