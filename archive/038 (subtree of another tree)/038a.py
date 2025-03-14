# https://leetcode.com/problems/subtree-of-another-tree/description/

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
        proposed_roots = []
        self.find(root, subRoot.val, proposed_roots)
        return any(self.is_same(foo, subRoot) for foo in proposed_roots)

    def find(self, node, val, arr):
        if not node:
            return None
        if node.val == val:
            arr.append(node)
        
        self.find(node.left, val, arr)
        self.find(node.right, val, arr)
        
        return None
    

    def is_same(self, one, two):
        if one is None and two is None:
            return True
        if one is None or two is None or one.val != two.val:
            return False
        
        return self.is_same(one.left, two.left) and self.is_same(one.right, two.right)
        

one = TreeNode(1)
second_one = TreeNode(1)

one.left = second_one

sol = Solution()
res = sol.isSubtree(one, second_one)

print(res)