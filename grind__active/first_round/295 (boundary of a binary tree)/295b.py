# https://leetcode.com/problems/boundary-of-binary-tree/


from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# TODO might need to deep the description
class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        left_boundary, right_boundary, leaves = [], [], []
        self.preorder(root, left_boundary, right_boundary, leaves, 0)
        return left_boundary + leaves + right_boundary

    def leftChildFlag(self, node, flag):
        if self.isLeftBoundary(flag) or self.isRoot(flag):
            return 1
        elif self.isRightBoundary(flag) and node.right is None:
            return 2
        else:
            return 3

    def rightChildFlag(self, node, flag):
        if self.isRightBoundary(flag) or self.isRoot(flag):
            return 2
        elif self.isLeftBoundary(flag) and node.left is None:
            return 1
        else:
            return 3

    def preorder(self, node, left_boundary, right_boundary, leaves, flag):
        if not node:
            return
        if self.isRightBoundary(flag):
            right_boundary.insert(0, node.val)
        elif self.isLeftBoundary(flag) or self.isRoot(flag):
            left_boundary.append(node.val)
        elif self.isLeaf(node):
            leaves.append(node.val)

        # when we call `preorder` on `root`
        # we'd skip all the ifs above
        self.preorder(
            node.left,
            left_boundary,
            right_boundary,
            leaves,
            self.leftChildFlag(node, flag),
        )
        self.preorder(
            node.right,
            left_boundary,
            right_boundary,
            leaves,
            self.rightChildFlag(node, flag),
        )

    def isLeaf(self, node):
        return node and not node.left and not node.right

    def isRightBoundary(self, flag):
        return flag == 2

    def isLeftBoundary(self, flag):
        return flag == 1

    def isRoot(self, flag):
        return flag == 0


one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)

one.right = two
two.left = three
two.right = four

sol = Solution()
sol.boundaryOfBinaryTree(one)