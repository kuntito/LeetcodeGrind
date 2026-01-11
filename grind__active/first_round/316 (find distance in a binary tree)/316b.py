# https://leetcode.com/problems/find-distance-in-a-binary-tree/description/

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
        return f"{self.val}"
    
# i'm given a binary tree with unique values in all it's nodes
# my job is to find the number of edges between two nodes `p` and `q`

# this sounds like a common ancestor problem
# or at least a variation of it
# if i find the greatest common ancestor of both nodes


# i don't know the recursive solution to this problem
# i'd find node p and node q
# track all the nodes i took to get there

# find the first common ancestor and determine the number of edges
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        pass
        peeNodes = []
        self.explore(root, p, peeNodes)
        
        queueNodes = []
        self.explore(root, q, queueNodes)
        
        
        # if i convert one of the node paths to a dictionary
        # node -> idx
        
        # then iterate through the second node paths in reverse
        # checking every item in the dictionary
        # till i hit the first one in the dictionary
        # this would be the lowest common ancestor
        
        peeDict = { val: idx for idx, val in enumerate(peeNodes)}
        
        
        edges = 0
        for idx in range(len(queueNodes) - 1, -1, -1):
            node = queueNodes[idx]
            # lowest common ancestor here
            if node in peeDict:
                pEdges = len(peeNodes) - peeDict[node] - 1
                qEdges = len(queueNodes) - idx - 1
                edges = qEdges + pEdges
                break
        
        # count from 
        return edges
        
        
        
    def explore(self, node, val, pathTaken):
        if not node:
            return
        
        pathTaken.append(node)
        if node.val == val:
            return True
        
        if self.explore(node.left, val, pathTaken):
            return True
        
        if self.explore(node.right, val, pathTaken):
            return True
        
        pathTaken.pop()
        
        return False
    
three = TreeNode(3)
five = TreeNode(5)
one = TreeNode(1)
six = TreeNode(6)
two = TreeNode(2)
zero = TreeNode(0)
eight = TreeNode(8)
seven = TreeNode(7)
four = TreeNode(4)

three.left = five
three.right = one

five.left = six
five.right = two

one.left = zero
one.right = eight

two.left = seven
two.right = four

sol = Solution()
res = sol.findDistance(three, 5, 5)
print(res)