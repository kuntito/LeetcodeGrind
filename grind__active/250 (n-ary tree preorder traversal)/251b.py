# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root):
        pass
        # use a stack to track all nodes
        # put `root` in the stack
        # on every iteration, pop the topmost item in the stack
        # and append it's value to the result array, `res`
        # now, reverse iterate through the popped nodes children and 
        # append the children to the stack
        # [4, 2, 3]

        stack = []
        if root:
            stack.append(root)
        
        res = []
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            
            for node in reversed(curr.children):
                stack.append(node)
                
        return res