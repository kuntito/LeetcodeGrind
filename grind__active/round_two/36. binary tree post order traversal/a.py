# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# what am i doing?
# i'm given a binary tree.
# i want to return an array of its values in a specific order.
# they call it post order... what does that mean?

# for every node.. you want to explore it's left subtree..
# then it's right subtree.. then the parent node..

# when you say, explore, what do you mean..
# we want to append nodes in the order of post order.

# so we always do left subtree first. subtree might be more complicated to grasp.
# but for starters..

# consider this:
#   2
# 4  5

# the post order is [4, 5, 2]
# we check the left child tree first.. (4)
# when we get to that left tree, we check it's own left subtree..
# but it has None, so we know to stop..
# actually, we check it's right subtree too..
# that is also None...
# therefore we can stop at this Node..
# since it has no left or right subtree..

# that's our base case, then we go back to parent (5)
# and explore it's right subtree (5)
# when we get to the right subtree, 
# 
# we explore it's left subtree..
# same story, different node..

# it's a recursive approach and we pass a tracking array..
# you could probably do this with a while loop but that'd be..
# an attempt to glaze myself..

# i think it's worth avoiding that rabbit hole..
# least, for now..

# what do we need for recursion
# * current node
# * trackingArray
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        trackingArr = []
        return self.explore(root, trackingArr)
    
    def explore(self, node, trackingArr):
        if not node:
            return trackingArr
        
        self.explore(node.left, trackingArr)
        self.explore(node.right, trackingArr)
        
        trackingArr.append(
            node.val
        )
        
        return trackingArr
        