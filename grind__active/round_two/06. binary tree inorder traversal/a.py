# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# i'm given a binary tree node where each node is an integer.
# i want to traverse the teee in-order and return an array of integers
# representing that traversal

# what is in-order traversal? you'd want to start from the leftmost node.
# leftmost? yes, keep going left till you can't no more. once you do that, you've hit rock bottom
# and can now append that node's value to the return array
# you'd return to the parent of that left leaf node

# then append the parent's value to the return array
# after which you explore the right child of the parent
# you don't append the right child's value
# instead you repeat the earlier logic flow..

# you look for the leftmost node, once you find that, you append it to the return array
# and only then can you append the right parent...
# it's a recursive approach, you keep doing this till you run out of nodes..

# leftmost, immediateparent, leftmost immediate parent..
# but this way, we never append any right nodes.. well, the right nodes are the immediate parent

#   1
#  2 3

# here, leftmost is [2]
# immediate parent is `1`, so [2, 1]
# then we explore the right child but don't append it's value until we've explore it's leftmost node
# in this case, no leftmost node so.. we append immediate parent, `3`
# hence, [2, 1, 3]

# any edge cases, an null root node..
# that would be handled by the empty return array
# we'd only ever append the leftmost node and it's immediate parent..

# left out edge case for null root
# turns out empty array didn't handle it, at least not how i intended
# i never checked for null node in the explore function and as a result ran into a failed test case.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.explore(root, res)

        return res
    
    def explore(self, node, res):
        if not node:
            return
        # what is the left most node?
        # the node with no left or right children
        # a leaf node? in every sense, we only say leftmost cause we explore the left branches first
        # so, we'd always hit the leftmost leaf nodes
        
        if node.left is None and node.right is None:
            res.append(
                node.val
            )
            return
            
        if node.left:
            self.explore(node.left, res)
            
        res.append(node.val)
        
        self.explore(node.right, res)
