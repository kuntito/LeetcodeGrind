# Definition for a binary tree node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

# https://neetcode.io/solutions/construct-binary-tree-from-preorder-and-inorder-traversal
# 15:04


from collections import Counter

# each recursive function should have a preorder and inorder
# find the index of the root node in `in_map`
# recursive calls for left child should be `preorder[:idx+1]` since `idx`
# represents the number of elements that belong on the left side of root
# inorder should be `inorder[:idx]`
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        pass
        in_map = Counter(inorder)
        
        return self.explore(preorder, inorder, in_map)
    