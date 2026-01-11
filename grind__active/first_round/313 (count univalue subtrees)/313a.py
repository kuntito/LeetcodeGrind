# https://leetcode.com/problems/count-univalue-subtrees/description/

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
        return f"({self.val})"

# what's the situation?
# we want to implement a function `countUnivalSubtrees` that takes a single argument
# `root`, a binary tree node, a nullable binary tree node

# our job is to examine the binary tree and return the number of uni-value
# subtree. but what is a uni-value sub-tree, a uni-value sub-tree is a sub-tree of `root`
# where all nodes have the same values

# `root` is a sub-tree of itself

# we don't really know if all nodes in a subtree have the same value until we explore every node in the sub-tree
# i'd say we'd apply recursion.
# we want to recursively pass the value of the parent node to every child node
# if parent.val != childNode.val, we return False

# if parent.val == childNode.val is the same, what do we do?
# we return a compound check, we ensure the parent child node is the same, we ensure that the childNodes all have the same value-

# nah, i don't think this would work.
# let's work backwards here. what do we want from each node?
# we want each node to return the number of uni-value subtrees

# let's take a leaf node
# it's definitely a univalue subtree so it should return `1`

# okay what about a root node with two leafs
# two scenarios, one where it's the same value with it's children
# and one where it isn't

# if it's the same value we'd add `1` to the sum of it's childNodes uni-value count
# if not we don't add `1`

# we'd recursively do this and have our result
# TODO rewrite the whole thing, how do you know if a tree is a uni-value
# vis-a-vis, it's children
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.explore(root)[1]
    
    def explore(self, node):
        if not node:
            return True, 0
        
        if node.left is None and node.right is None:
            return True, 1

        leftUni, leftCount = self.explore(node.left, node.val)
        rightUni, rightCount = self.explore(node.right, node.val)

        nodeCount = leftCount + rightCount
        isUni = False
        if leftUni and rightUni and (node.left and node.left == node.val) and (node.right and node.right == node.val):
            isUni = True
            nodeCount += 1

        return isUni, nodeCount


# rootFive = TreeNode(5)
# one = TreeNode(1)

# fiveTwo = TreeNode(5)
# fiveThree = TreeNode(5)
# fiveFour = TreeNode(5)
# fiveFive = TreeNode(5)

# rootFive.left = one
# rootFive.right = fiveTwo

# fiveTwo.right = fiveFive

# one.left = fiveThree
# one.right = fiveFour


rootFive = TreeNode(5)
leftFive = TreeNode(5)
one = TreeNode(1)

rootFive.left = leftFive
rootFive.right = one

sol = Solution()
res = sol.countUnivalSubtrees(rootFive)
print(res)