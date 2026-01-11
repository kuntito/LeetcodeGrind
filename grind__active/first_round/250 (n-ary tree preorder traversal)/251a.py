# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        
        res = []
        
        self.explore(root, res)
        
        return res
    
    def explore(self, node, arr):
        if not node:
            return
        
        arr.append(node.val)

        for c in node.children:
            self.explore(c, arr)