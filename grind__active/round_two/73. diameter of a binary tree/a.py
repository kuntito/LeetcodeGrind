# https://leetcode.com/problems/diameter-of-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

# i want to find the diameter of a binary tree..
# what's this?

# the number of edges on the longest path within the node.
# what's the longest path between the node..

# two tail nodes that connect to each other..
# this isn't very clear

# say you have:
#   1
#  2 3
# 45 67

# one path is 4 -> 2 -> 1 -> 3 -> 6
# another path is 4 -> 2 -> 5
# another one is 6 -> 3 -> 7

# and so on..
# so how would this go..
# for each node, you want to know how deep it's left node goes
# and how deep it's right node goes..

# using this, you know the longest path across this particular node.
# you do this for every node, and should have your solution.

# what does each node return?
# each node returns the longest path from itself to a leaf node.

# but you're summing up the longest paths on left and right subtrees..
# yeah, two separate things..

# the left right plus current node calculation..
# then returning the longest path at that node which would be `node + leftTree longest` or `node + rightTree longest`
# we can return two things..

# the longest from each node downward and the max diameter seen..
# the diameter doesn't need a plus `1`
# since we're dealing with edges

#  1
# 23
# 2 -> 1 -> 3, only has two edges..

# two errors, 

# no return...

# i didn't make the recursive function return the same thing on every return
# the function should return the node count and the diameter at that node..

# for the base case, i did `if not node: return 0`
# and for the left and right explorations..

# i'd done..
# leftCount = self.explore(node.left)
# rightCount = self.explore(node.right)

# meanwhile both calls are expected to return a tuple
# i corrected it with
# leftCount, leftDiam = self.explore(node.left)
# rightCount, rightDiam = self.explore(node.right)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.explore(root)[1]
        
    def explore(self, node):
        if not node:
            return (0, 0)
        
        leftCount, leftDiam = self.explore(node.left)
        rightCount, rightDiam = self.explore(node.right)
        
        longestPathFromHere = max(leftCount, rightCount) + 1
        diameterHere = leftCount + rightCount
        
        bestDiameter = max(diameterHere, leftDiam, rightDiam)
        
        return (
            longestPathFromHere,
            bestDiameter,
        )