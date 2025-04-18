# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
        
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        return f'({self.val})'

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        pass
        # bfs
        # but iterate in reverse for each layer
        # also create the next layer by appending left
        # append the right child, then left child
        
        # hence, deque
        q = deque([root] if root else [])
        
        while q:
            tmp = deque()
            while q:
                # iter in reverse
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
    
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
seven = Node(7)

one.left = two
one.right = three

two.left = four
two.right = five

three.right = seven

sol = Solution()
res = sol.connect(one)

def print_bfs(node):
    arr = [node]
    while arr:
        print([x.next for x in arr])
        tmp = []
        for nei in arr:
            if nei.left:
                tmp.append(nei.left)
            if nei.right:
                tmp.append(nei.right)
            
        arr = tmp
        
# print_bfs(one)
print('#######')
print_bfs(res)