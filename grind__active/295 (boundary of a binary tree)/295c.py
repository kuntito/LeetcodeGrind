# https://leetcode.com/problems/boundary-of-binary-tree/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# we want to implement a function, `boundaryOfBinaryTree` that takes a binary tree node and returns a list of the boundary elements of the tree

# the boundary elements can be understood as drawing a line around the binary tree, every node on that line represents the boundary.

# the return list should contain the left boundary, the leaf nodes and the right boundary in reverse order

# consider
#   1
#  2 3
# 4 5 6

# if we drew a line around the tree
# the left boundary would be [1, 2]
# the leaf nodes would be [4, 5, 6]
# and the right boundary in reverse order would be [3]

# therefore, the final answer would be [1, 2, 4, 5, 6, 3]

# and how would we implement this
# the root is classed as the left boundary
# we iterate through it's left and right child

# but left first,
# if it has no left child, it means there's no left boundary

# but if it does, that left child is part of the boundary
# technically, all left child nodes excep the leaf nodes are in the left boundary

# what if a left node has no left child, then it's right child become the left boundary

# it'd be a recursive solution and we'd need to know if it's the root node
# and if we're in the left boundary


# if the root node is None, simply return an empty list

# TODO doesn't work, i wonder what i missed.
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        self.root = root
        self.leftBoundary = []
        self.leaves = []
        self.rightBoundary = []

        self.leftBoundary.append(root.val)

        # the recursion is the same except for the root
        # at the root, the first time we explore left, isLeft = True, isRight = False

        # and the first time, we explore right, isLeft = False, isRight = True
        self.exploreLeft(root.left, True)
        self.exploreRight(root.right, True)

        # print(self.leftBoundary)
        # print(self.leaves)
        # print(self.rightBoundary)

        return self.leftBoundary + self.leaves + self.rightBoundary

    def exploreLeft(self, node, isLeft):
        if not node:
            return

        # if it's a leaf node
        if node and node.left is None and node.right is None:
            self.leaves.append(node.val)
            return

        if isLeft:
            self.leftBoundary.append(node.val)

        # we explore all nodes, because we need the leaf nodes

        # explore the left node
        self.exploreLeft(node.left, isLeft)

        # explore the right node
        # the right node is only part of the left boundary if there is no left node
        self.exploreLeft(node.right, False if node.left else True)

    def exploreRight(self, node, isRight):
        if not node:
            return

        # if it's a leaf node
        if node and node.left is None and node.right is None:
            self.leaves.append(node.val)
            return

        self.exploreRight(node.left, False if node.right else True)
        self.exploreRight(node.right, isRight)

        # we append the right boundary in post order way
        # since we want the nodes in reverse
        if isRight:
            self.rightBoundary.append(node.val)


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.right = two
two.left = three
two.right = four

sol = Solution()
res = sol.boundaryOfBinaryTree(one)
print(res)
