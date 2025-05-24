# https://leetcode.com/problems/find-distance-in-a-binary-tree/description/
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# i'm given a binary tree with unique values in all it's nodes
# my job is to find the number of edges between two nodes `p` and `q`

# this sounds like a common ancestor problem
# or at least a variation of it
# if i find the greatest common ancestor of both nodes
# the answer is one of to things
# `p` and `q` are in different branches of the ancestor (left sub tree or right sub tree)

# OR

# either `p` or `q` is the greatest common ancestor
# in which case?

# okay, an even better idea
# find the greatest common ancestor and track the number of edges from `p` to greatest common ancestor
# do the same for `q`

# sum up the edges, and there you go
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        pass
    
        # not sure how i'd track the edges from common ancestor to `p` and `q`
        # but let me find the common ancestor first
        
        # how would i know if i've found it
        # two scenarios, the `gca` could have either node
        # in it's left and right sub tree
        # or the root is one of `p` and `q` and one of the subtrees must have the other node
        
        
        # `p` and `q` are guaranteed to be in the tree
        # we can use recursion, what would each function return?
        
        # nothing, declare a global variable to store the greatest common ancestor
        
        self.gcm = None
        self.explore(root, p, q)
        
    def explore(self, node, uno, dos):
        if not node:
            return
        
        # if node.val
        
        leftRes = self.explore(node.left, uno, dos)
        rightRes = self.explore(node.right, uno, dos)
        