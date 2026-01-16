# https://leetcode.com/problems/binary-tree-preorder-traversal/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# i want to traverse a binary tree in preorder and track all the nodes i visit in said order
# what is preorder, root first, left subtree next, then right subtree..

# it screams recursion..
# we'd pass the tracking array to..
# in each recursive call, append root.val to array

# check left subtree..

# base case, if root node is None..
# in which case we go up and check right subtree..
# if nothing.. return

# iteration ends, array is populated..
# everyone's happy

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        self.explore(root, res)
        return res
    
    def explore(self, node, res):
        if not node:
            return
        
        res.append(node.val)
        self.explore(node.left, res)
        self.explore(node.right, res)