# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
from typing import Optional

# what's the situation today?

# i'm given a binary tree node and want to find the largest path sum.
# in English?.. the path sum is the total of all the node values along a given path.

# but what is a path.
# a connection from one leaf node to another leaf node.

# consider the tree node:
#    1
#  2   3
# 4 5 6 7

# one path is `4->2->1->3->7`
# because the leaf node `4` connects to the leaf node `7` through `..2->1->3..`

# another path is `4 -> 2 -> 5`
# the leaf node `4` connects with the leaf node `5` through `2`

# and the path sum would be the sum of all the node values along this path.
# i want to search the tree node and find the path with the largest sum.

# how would this go?

# can a path sum be a single node?
# well, it should be.

# consider if the root node was a leaf node.
# the max path sum would have to be the root node.

# but how would you find the largest path sum?
# you'd have to explore every path..

# yeah, but how...
# let's break it down this way..

# starting at the root node..
# you can explore the left subTree or the right subTree

# each of these subTrees have their own largest path sum.
# it's also possible the root node and a combination of left subTree
# or right subTree

# this makes it apparent, the path doesn't necessarily have to be 
# a leaf node connected to another leaf node.

# consider:
#    2
# -10 5

# the best path would be `2 -> 5`
# a path is just a series of connected nodes.

# correction taken. however, the foundations to solving this remain the same.
# at each root node..
# what's the best path in left sub tree
# what's the best path in right sub tree
# can root combine with both or either sub trees to form a greater path

# that's the recursive step..
# okay.. so what are we returning at each step?

# it would have to be .. i want to say the best path sum at that subtree
# isn't that what we want?

# well, yes.. that's what we want from the subtree
# but what would it's parent want?

# consider:
#     1
#   2   3
# 4 5  6  7

# i don't have a good example for this
# but to illustrate this.. each subtree determines the best path at it's root node.
# however, that best path could span the left and right subtrees..

# let's say our root subtree is `rootSub`
# and it's determined it's best path sum and that spans left and right sub trees

# `rootSub`s parent cares about which one of `rootSubs` left and right paths is larger...
# not the span..

# if rootSub is `2`
# the best path sum at that point would be `4 + 2 + 5` =  11

# however, rootSub's parent, `1`
# doesn't care about `11`

# it wants to know, do i go down
# 2 -> 4, OR
# 2 -> 5,

# so each recursive call is returning two things..
# best path sum at that root node..
# the larger path sum between going left or going right

# and what's the base case?
# a leaf node..

# there's nothing left, nothing right..
# so we return `0`

# actually, we return `0, 0`
# best path sum at leaf node, better path sum between leaf nodes left and right paths...

# let me write the code and continue the writing within the function
# for it gets messy.

# error, my code fails for this case.
# where root is a leaf node with value `-3`

# what would this mean?
# the left recursion would return (0, 0)
# the right recursion would return (0, 0)

# so now, i compare bestLeft, bestRight and spanSum..
# in this case span sum would rightfully.. be `-3`

# but since bestLeft and bestRight is `0`
# it would prefer.. the max call would take `0` to be more than `-3`

# returning `0` as the best path sum.

# what would the fix look like?
# am i wrong to return `0` for bestSum

# well, clearly..
# what's the alternative..

# return the truth.
# which is..
# `None`

# okay, so should i also return None
# for the better path..

# well, i can't think of why it would matter right now
# but yes.. None is more accurate than `0`

# might be easier if i just rewrote this joint.

# TODO find the similar question to this..


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def __repr__(self):
        return f"({self.val})"
    

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        bestPathSumAtNode, betterPathFromNode = self.explore(root)
        
        return bestPathSumAtNode
    
    def explore(self, root):
        if not root:
            return 0, 0
        
        bestPathSumAtLeft, betterPathFromLeft = self.explore(root.left)
        bestPathSumAtRight, betterPathFromRight = self.explore(root.right)
        
        # now what do we do?
        # to get the best path sum at this point..
        # it's either:
        #   bestAtLeft alone
        #   bestAtRight alone
        # or something that spans both subtrees..
        
        # what condition would you need to span..
        # if root is +ve and both bests are +ve
        # then we can add them all
        
        # but what if one of them is negative, say bestLeft is -ve
        # in that case, we can add, bestRight and root's value..
        
        # another approach is this..
        # we only want to add node to both best left or best right
        # if both of them are positive
        
        # how about.. root.val + max(bestLeft, 0) + max(bestRight, 0)
        # this handles all situations right..
        
        # if either bestRight or bestLeft is -ve, it becomes `0`
        # and root.val takes the lead..
        
        # but what if root.val is -ve, then it alone would be the spanSum.
        
        # okay, but what if either bestLeft or bestRight were the greater negative
        # that's why we determine best sum here by comparing..
        
        # bestRight, bestLeft and spanSum
        
        # effortless..
        
        spanSum = root.val + max(bestPathSumAtLeft, 0) + max(bestPathSumAtRight, 0)
        
        # error, the best sum at node is either the spanSum, the bestAtLeft or the bestRight 
        # what i did was compare spanSum, with the better path from left and the better path from right.
        
        bestPathSumAtNode = max(
            spanSum,
            bestPathSumAtLeft,
            bestPathSumAtRight
        )
        
        betterPathSumAtNode = max(
            betterPathFromLeft,
            betterPathFromRight
        )
        
        return bestPathSumAtNode, betterPathSumAtNode

    
negTen = TreeNode(-10)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

negTen.left = nine
negTen.right = twenty
twenty.left = fifteen
twenty.right = seven

sol = Solution()
res = sol.maxPathSum(negTen)
print(res)