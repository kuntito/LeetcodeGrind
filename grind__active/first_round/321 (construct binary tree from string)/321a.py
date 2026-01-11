# https://leetcode.com/problems/construct-binary-tree-from-string/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# i want to implement a function, `str2tree` that takes
# an string argument `s` and returns a TreeNode

# `s` contains numbers and parentheses.
# consider 2(3)(1)

# this means `2` is the root node
# it's left child is `3` and it's right child is `1`

# 4(2(3)(1))(6(5))

# means `4` is the root
# the root can have two outer parentheses after it
# signifying the right subtree and left subtree

# i think this can be addressed in reverse
# i know `4` is the root, 
# i explore the very next opening parentheses
# i see that `2` is the root
# i explore the very next opening parentheses
# see that `3` is the root
# and the next element is a closing parentheses
# so i return a node with three in it


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        return self.explore(s, 0)
    
    def explore(self, chars, idx):
        # what's the base case
        dim = len(chars)
        if idx == dim:
            return
        
        # the first value should always be a number
        ch = int(chars[idx])
        # create a node based on that and explore the left and right child
        node = TreeNode(ch)
        
        # the left child would start from idx += 2
        # cause you skip the opening parentheses
        # however, if chars[idx + 1] == ")"
        # return the node
        
        # it's a leaf node
        # what if there's no value? i.e. s = "4"
        # it's still a leaf node
        
        if idx + 1 == dim or chars[idx + 1] == ')':
            return node
        
        leftNode = self.explore(chars, idx + 2)
        
        # 2(3)(1)
        # you start of at idx == 0, which is `2`
        # for left node, `3`, idx + 2
        # for right node, `1`, idx + 5
        rightNode = self.explore(chars, idx + 5)
        
        node.left = leftNode
        node.right = rightNode
        
        return node
    
arr = [
    "4(2(3)(1))(6(5))",
]
foo = arr[-1]
sol = Solution()
res = sol.str2tree(foo)
