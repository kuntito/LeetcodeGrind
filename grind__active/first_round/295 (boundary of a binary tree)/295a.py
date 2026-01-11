# https://leetcode.com/problems/boundary-of-binary-tree/description/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        pass
        # we want to find the boundary of a binary tree but what is this boundary?
        # they say it's a concatenation of the root, the left boundary anf the leaves ordered from left to right
        
        # it's still unclear, you've defined a boundary by itself (left boundary).
        
        # the left boundary is the set of nodes where the root node's left child is part
        # if the root's left does not have a left child, then the left boundary is empty
        
        # if a node in the left boundary has a left child, then that child is in the left boundary
        
        # judging off the images, we want all the leaf nodes
        # and we want the leftmost non leaf nodes
        # and the right most non-leaf nodes
        
        # i get the question, but i am unable to write the code
        
        
        self.res = []
        self.explore(root.left, True, False)
        self.explore(root.right, False, True)
        return self.res
        
    def explore(self, node, leftmost, rightmost):
        if not node:
            return
        
        if node.left is None and node.right is None:
            self.res.append(node.val)
            return
        
        if leftmost or rightmost:
            self.res.append(node.val)
        
        self.explore(
            node.left,
            leftmost, 
            rightmost
        )
        
        if leftmost:
            leftmost = False
            rightmost = False
        self.explore(node.right, leftmost, rightmost)