# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# TODO https://neetcode.io/solutions/leaf-similar-trees
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        # write a recursive function that explores each node and appends the value of a leaf node to an array
        # a leaf node is a node whose left and right children are `None`
        uno = self.explore(root1, [])
        dos = self.explore(root2, [])
        
        # `uno` and `dos` are the respective arrays for `root1` and `root2`
        # if their lengths are different: return False
        
        # else zip both arrays and compare their respective elements
        # if `itemUno != itemDos: return False`
        for itemUno, itemDos in zip(uno, dos):
            if itemUno != itemDos:
                return False
            
        return True
    
    def explore(self, node, arr):
        if not node:
            return arr
        
        if not (node.left or node.right):
            arr.append(node.val)
            
        self.explore(node.left, arr)
        self.explore(node.right, arr)
        
        return arr
        