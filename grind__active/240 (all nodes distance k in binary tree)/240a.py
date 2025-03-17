# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> list[int]:
        pass
    
        # traverse all the nodes in the binary tree
        # add a reverse relationship between child and parent
        self.exploreReverseBranch(root, None)
        # print(target)
        
        
        # conduct a bfs from `target` and use a set `seen`
        # to avoid visited nodes
        seen = set()
        queue = deque()
        
        queue.append(target)
        while queue and k > 0:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr in seen:
                    continue
                
                seen.add(curr)
                # append it's neighbours
                neighbours = [curr.left, curr.right, curr.parent]
                for nei in neighbours:
                    if nei and nei not in seen:
                        queue.append(nei)
            
            k -= 1
            
        return [node.val for node in queue]
        
        
        
    def exploreReverseBranch(self, node, parent):
        if not node:
            return
        
        node.parent = parent

        self.exploreReverseBranch(node.left, node)
        self.exploreReverseBranch(node.right, node)
        

zero = TreeNode(0)
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)
eight = TreeNode(8)

two.left = seven
two.right = four

five.left = six
five.right = two

three.left = five
three.right = one

one.left = zero
one.right = eight

sol = Solution()
res = sol.distanceK(three, five, 2)
print(res)