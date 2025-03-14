# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        pass
        # bfs while counting levels
        # return count at the first leaf node
        
        level = 1
        arr = [root]
        
        while arr:
            tmp = []
            for node in arr:
                if node.left is None and node.right is None:
                    return level
                
                if node.left:
                    tmp.append(node.left)
                    
                if node.right:
                    tmp.append(node.right)
            
            arr = tmp
            level += 1
        