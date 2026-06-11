# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxPathSum, _ = self.explore(root)
        
        return maxPathSum
        
    def explore(self, root):
        if not root:
            return float("-inf"), float("-inf")
        
        bestSumLeft, betterPathLeft = self.explore(root.left)
        bestSumRight, betterPathRight = self.explore(root.right)
        
        spanSumHere = self.getBestSumHere(
            root.val, 
            betterPathLeft, 
            betterPathRight
        )
        
        bestSumHere = max(
            spanSumHere,
            bestSumLeft,
            bestSumRight,
        )
        
        betterPathHere = self.getBetterPathHere(
            root.val,
            betterPathLeft,
            betterPathRight
        )
        
        return bestSumHere, betterPathHere
        
    def getBestSumHere(self, rootVal, leftPathSum, rightPathSum):
        return rootVal + max(0, leftPathSum) + max(0, rightPathSum)
    
    def getBetterPathHere(self, rootVal, leftPathSum, rightPathSum):
        a = rootVal + max(0, leftPathSum)
        b = rootVal + max(0, rightPathSum)
        
        return max(
            a,
            b    
        )
        
negTen = TreeNode(-10)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

negTen.left = nine
negTen.right = twenty
twenty.left = fifteen
twenty.right = seven

sol = Solution()
res = sol.maxPathSum(negTen)
print(res)