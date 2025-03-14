# https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'{self.val}'


class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not subRoot: return True
        if not root: return False

        if self.is_same(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or\
            self.isSubtree(root.right, subRoot)
    

    def is_same(self, one, two):
        if one is None and two is None:
            return True
        if one or two or one.val == two.val:
            return self.is_same(one.left, two.left) and\
                self.is_same(one.right, two.right)
        return False
        

one = TreeNode(1)
second_one = TreeNode(1)

one.left = second_one

sol = Solution()
res = sol.isSubtree(one, second_one)

print(res)