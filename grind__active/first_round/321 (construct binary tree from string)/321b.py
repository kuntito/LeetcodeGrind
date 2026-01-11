# https://leetcode.com/problems/construct-binary-tree-from-string/description/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

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

from collections import deque

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        queue = deque(s)
        
        return self.explore(queue)
    
    def explore(self, queue: deque):
        if queue and queue[0] == ")":
            queue.popleft()
            return
               
        while queue and (not queue[0].isdigit()):
            queue.popleft()
            
        if not queue:
            return
            
        ch = int(queue.popleft())
        
        node = TreeNode(ch)
        
        leftNode = self.explore(queue)
        rightNode = self.explore(queue)
        
        node.left = leftNode
        node.right = rightNode
        
        return node
        

    
arr = [
    "4(2(3)(1))(6(5))",
]
foo = arr[-1]
sol = Solution()
res = sol.str2tree(foo)

queue = deque([res])

while queue:
    temp = deque()
    print(queue)
    while queue:
        node = queue.popleft()
        if node.left:
            temp.append(node.left)
        if node.right:
            temp.append(node.right)
            
    queue = temp
