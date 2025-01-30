# https://leetcode.com/problems/symmetric-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TODO https://neetcode.io/solutions/symmetric-tree
class Solution:
    def isSymmetric(self, root) -> bool:
        pass
    
        if not root:
            return True
        
        # recursively explore alternative child nodes
        # starting with `root.left` and `root.right`
        # if they're not equal, return False
        # if equal
        # explore (one.left and two.right) then (one.right and two.left)
        return self.explore(root.left, root.right)
        
    def explore(self, one, two):
        if one is None and two is None:
            return True
        
        if (bool(one) ^ bool(two)) or one.val != two.val:
            return False
        
        return self.explore(one.left, two.right) and\
            self.explore(one.right, two.left)
            

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(4)
f = TreeNode(4)
g = TreeNode(3)

a.left = b
a.right = c

b.left = d
b.right = e

c.left = f
c.right = g

sol = Solution()
res = sol.isSymmetric(a)
print(res)