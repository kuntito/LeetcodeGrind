# https://leetcode.com/problems/same-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.explore(p, q)
    
    def explore(self, primera, segundo):
        if primera is None and segundo is None:
            return True
        if primera is None or segundo is None or primera.val != segundo.val:
            return False
        
        return self.explore(primera.left, segundo.left) and\
            self.explore(primera.right, segundo.right)