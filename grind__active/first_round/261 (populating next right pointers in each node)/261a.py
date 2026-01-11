# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

from collections import deque
class Solution:
    def connect(self, root: Node) -> Node:
        pass
        # you're doing a level order traversal
        # but each level you iterate in reverse
        # in order to assign the next pointer
        
        q = deque([root] if root else [])
        
        while q:
            tmp = deque()
            pass
            # go through `q` in reverse
            # but append the children with `appendleft`
            # you want to main the right order for the children
            while q:
                curr = q.pop()
                
                if curr.right:
                    if tmp:
                        curr.right.next = tmp[0]
                    tmp.appendleft(curr.right)
                    
                    
                if curr.left:
                    if tmp:
                        curr.left.next = tmp[0]
                    tmp.appendleft(curr.left)
                    
            q = tmp
            
        return root