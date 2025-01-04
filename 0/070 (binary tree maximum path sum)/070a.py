# https://leetcode.com/problems/binary-tree-maximum-path-sum/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        self.maxPath = float("-infinity")
        self.explore(root)
        return self.maxPath
    
    def explore(self, node):
        if not node: return 0

        left = max(self.explore(node.left), 0)
        right = max(self.explore(node.right), 0)
    
        self.maxPath = max(
            self.maxPath,
            left + right + node.val
        )

        return node.val + max(right, left)


neg_ten = TreeNode(-10)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)


neg_ten.left = nine
neg_ten.right = twenty
twenty.left = fifteen
twenty.right = seven


sol = Solution()
res = sol.maxPathSum(neg_ten)
print(res)