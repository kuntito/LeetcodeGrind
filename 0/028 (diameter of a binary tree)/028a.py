# https://leetcode.com/problems/diameter-of-binary-tree/description/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root):
        self.max_depth = 0
        self.explore(root)
        return self.max_depth
    
    def explore(self, node, depth = 0):
        if not node:
            return 0
        
        left = self.explore(node.left, depth + 1)
        right = self.explore(node.right, depth + 1)

        self.max_depth = max(
            left + right,
            self.max_depth,
        )
        return max(left, right) + 1
    
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)

one.left = two
two.right = three

sol = Solution()
res = sol.diameterOfBinaryTree(one)

print(res)