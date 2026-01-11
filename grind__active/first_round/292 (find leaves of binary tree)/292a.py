# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
       
        pass
        # we're given a binary tree and want to collect all leaf nodes
        # well, sort of
        
        # when given the tree, we determine it's current leaf nodes
        # extract them into an array
        
        # thereby revealing a new set of leaf nodes
        # we extract those too
        
        # thereby revealing a new set of leaf nodes
        # we do this until we hit the root node
        
        # how would you do this?
        
        # i suggest using a hashmap
        # or an array really
        
        # what we want is layers of leaf nodes
        # i'd say we traverse the array till we hit a leaf node
        
        # at this point, this would be the first layer, we'd call it layer 0
        
        # we'd have a container for all the layers called `res`
        # when we hit rock bottom, we add that node to `layer 0`
        # we create the layer if it doesn't exist
        # and return the layer index + 1 i.e. 0 + 1
        
        # this means the parent node would be in a layer `1`
        # and we essentially do the same thing
        
        # the caveat here is one subtree can be longer than the other
        # we should always take the longer layer, if there's a differing layer types
        
        res = []
        self.explore(root, res)
        return res
    
    def explore(self, node, res):
        if not node:
            return -1
        # so we need to note when we hit rock bottom
        
        leftDepth = self.explore(node.left, res)
        rightDepth = self.explore(node.right, res)
        
        currDepth = max(leftDepth, rightDepth) + 1
        
        if currDepth == len(res):
            res.append([])
            
        res[currDepth].append(node.val)
        
        return currDepth

sol = Solution()

one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)

one.left = two
one.right = three
two.left = four
two.right = five

res = sol.findLeaves(one)
print(res)