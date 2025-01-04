# https://leetcode.com/problems/balanced-binary-tree/description/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.imbalance_exists = False

    def isBalanced(self, root: TreeNode) -> bool:
        self.explore(root)
        return not self.imbalance_exists

    def explore(self, node):
        if not node:
            return 0
        
        left = self.explore(node.left)
        right = self.explore(node.right)
        if left is None or right is None:
            return left

        if abs(left - right) > 1:
            self.imbalance_exists = True

        depth = max(left, right) + 1 
        return None if self.imbalance_exists else depth
    


three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)


three.left = nine
three.right = twenty
twenty.left = fifteen
twenty.right = seven

sol = Solution()
res = sol.isBalanced(three)

print(res)