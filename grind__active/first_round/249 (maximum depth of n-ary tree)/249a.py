# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/description/

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root) -> int:
        return self.explore(root)
    
    def explore(self, node):
        if not node:
            return 0
        
        deepest = 0
        for n in node.children:
            deepest = max(
                deepest,
                self.explore(n)
            )
        
        return deepest + 1