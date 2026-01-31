# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# i'm given a binary tree.

# i want to find the furthest leaf node from the root
# when i do, i want to return the total nodes from root to furthest leaf node.

# both nodes are inclusive in the total.
# both root, and furthest

# consider:
#  1
# 2 3
# the furthest leaf nodes here are `2` or `3`
# and so the total count from `1` to either of them is `2` nodes.

# hence, we return `2`

# but how do you write this in code?
# from root,
# i don't know how far the left or right sub trees go

# so, i'd have to check both..
# i'd recursively explore each tree
# and return the total nodes along that path..

# on the parent call, i'd return the length of the longest subtree + 1
# `+ 1` to include the parent iself.

# problem solved.

# error, on exploring the left and right children
# i didn't pass left and right nodes..
# i did  `self.maxDepth(root)` instead of `self.maxDepth(root.left)`

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
    
        leftCount = self.maxDepth(root)
        rightCount = self.maxDepth(root)
        
        return 1 + max(leftCount, rightCount)