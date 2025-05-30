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



# 4(2(3)(1))(6(5))

from collections import deque

class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if not s:
            return None
        
        
        return self.explore(deque(s))
        
    def explore(self, queue: deque):
        if queue and queue[0] == '(':
            queue.popleft()
            queue.pop()
        
        if not queue:
            return

        ch = ""
        while queue and queue[0] != '(':
            ch += queue.popleft()
        ch = int(ch)

        node = TreeNode(ch)
        
        if not queue:
            return node
        
        openParen = queue.popleft()
        parens = [openParen]
        leftQueue = deque(parens)
        
        while parens:
            ch = queue.popleft()
            if ch == ')':
                parens.pop()
            if ch == '(':
                parens.append(ch)
            
            leftQueue.append(ch)
              
                        
        node.left = self.explore(leftQueue)
        node.right = self.explore(queue)
        
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
