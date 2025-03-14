# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: return 0

        xander = root.val
        return self.explore(root, xander)
    
    def explore(self, root, xander):
        xander = max(xander, root.val)
        count = 1 if root.val >= xander else 0

        if root.left:
            count += self.explore(root.left, xander)
        if root.right:
            count += self.explore(root.right, xander)

        return count