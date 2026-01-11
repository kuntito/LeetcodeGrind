# https://leetcode.com/problems/count-univalue-subtrees/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        isUni, count = self.explore(root)
        
        return count
    
    def explore(self, node):
        if not node:
            return False, 0
        
        isNodeUni = True
        
        leftCount = 0
        if node.left:
            isLeftUni, leftCount = self.explore(node.left)
            if node.left.val != node.val or not isLeftUni:
                isNodeUni = False
        
        rightCount = 0
        if node.right:
            isRightUni, rightCount = self.explore(node.right)
            if node.right.val != node.val or not isRightUni:
                isNodeUni = False
                
        count = leftCount + rightCount + (1 if isNodeUni else 0)
        return isNodeUni, count
        
rootFive = TreeNode(5)
one = TreeNode(1)

fiveTwo = TreeNode(5)
fiveThree = TreeNode(5)
fiveFour = TreeNode(5)
fiveFive = TreeNode(5)

rootFive.left = one
rootFive.right = fiveTwo

fiveTwo.right = fiveFive

one.left = fiveThree
one.right = fiveFour


sol = Solution()
res = sol.countUnivalSubtrees(rootFive)
print(res)
