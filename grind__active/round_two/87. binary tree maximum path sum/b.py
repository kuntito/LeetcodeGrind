# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"({self.val})"

# so what we doing?

# i'm given a node and want to find the best path sum for the given node.
# and how would this go?

# i've deduced that the best path sum either exists in:
#   the left sub tree
#   the right sub tree
#   a span
#       left subTree and root
#       right subTree and root
#       left subTree, right subTree and root..

# so, i have to write the code that reflects this.
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass