# https://leetcode.com/problems/binary-tree-inorder-traversal/
class Solution:
    def explore_in_order(self, node, res: list):
        if not node: return

        self.explore_in_order(node.left, res)
        res.append(node.val)
        self.explore_in_order(node.right, res)

    def inorderTraversal(self, root):
        res = []
        self.explore_in_order(root, res)
        return res     