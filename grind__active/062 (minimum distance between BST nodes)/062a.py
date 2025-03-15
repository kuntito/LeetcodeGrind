# https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TODO https://neetcode.io/solutions/minimum-distance-between-bst-nodes
class Solution:
    def minDiffInBST(self, root) -> int:
        pass
    
        arr = []
        self.explore(root, arr)
        
        arr.sort()
        res = abs(arr[0] - arr[1])
        
        for i in range(arr[2:]):
            res = min(
                res,
                abs(arr[i] - arr[i-1])
            )
        
        return res
    
    def explore(self, node, arr):
        if not node:
            return
        
        arr.append(node.val)
        
        self.explore(node.left, arr)
        self.explore(node.right, arr)
            
            
            
zero = TreeNode(0)
one = TreeNode(1)
        
    