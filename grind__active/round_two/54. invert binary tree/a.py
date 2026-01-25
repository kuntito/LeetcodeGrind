# https://leetcode.com/problems/invert-binary-tree/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# what we doing?
# i'm given a binary tree, i'm asked to invert it and return it's root..
# what is this inversion?

# inversion is swapping left and right children
# for every node..

# say you have:
#  1
# 2 3

# to invert it, is to turn it to:
#  1
# 3 2

# and we'd do this recursively..
#   1
#  2  3
# 4 5 6 7

# you'd probably start from the last layer
# swap `4` with `5`, `6` with `7`
#   1
#  2  3
# 5 4 7 6

# then their parents.. 
#   1
#  3  2
# 7 6 5 4

# in this example, i've swapped layer by layer but in reality..
# the recursion would explore one subtree first..
# say we reset..

#   1
#  2  3
# 4 5 6 7

# i'd start at node `1`
# explore it's children.. left and right, but one after the other..
# say i pick left first.. node `2`

# now, i'm back in a similar situation as node `1`
# i'm exploring node `2`s children.. left and right.. but one after the other..

# i explore node `4`
# then it's children.. left and right.. but one after the other..
# both children are `None`
# but i'd return either way..

# and it's after this return that the swap happens..
# for the leaf nodes, it's inconsequential..
# `None` is `None`

# but since, it's recursive, we do the same thing in every function call..
# i'd go back to `node 2`, explore it's right child..`5`
# it comes back, nun' much changed..

# now, i swap
#  2
# 5 4
# i keep doing this every where and eventually entire tree is inverted..


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        leftChild = root.left        
        rightChild = root.right
        
        
        root.right = self.invertTree(leftChild)
        root.left = self.invertTree(rightChild)
        
        return root