# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> list[list[int]]:
        pass
        # it's giving bfs and deque
        # use a boolean to determine current direction, left or right, `toLeft`
        
        # we place the root in a deque, `bothWays`
        # while `bothWays` has values
        # if `toLeft`
        # go through `bothWays` from ltR
        
        # create a temp queue to append the children
        
        bothWays = deque([root] if root else [])
        toRight = True
        
        res = []
        while bothWays:
            lst = deque()
            tmp = deque()
            # print([x.val for x in bothWays])
            while bothWays:
                curr = bothWays.popleft()
                if toRight:
                    lst.append(curr.val)
                else:
                    lst.appendleft(curr.val)
                
                if curr.left:
                    tmp.append(curr.left)
                if curr.right:
                    tmp.append(curr.right)
                    
            toRight = not toRight
            bothWays = tmp
            res.append(list(lst))
            
        return res


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.left = two
one.right = three

two.left = four
two.right = None

three.left = None
three.right = five

sol = Solution()
res = sol.zigzagLevelOrder(one)

for rw in res:
    print(rw)