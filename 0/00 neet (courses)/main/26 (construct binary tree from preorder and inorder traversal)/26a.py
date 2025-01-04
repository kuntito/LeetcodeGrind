# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder: return None

        pre_map = {}
        for idx, elem in enumerate(preorder):
            pre_map[elem] = idx


        in_map = {}
        for idx, elem in enumerate(inorder):
            in_map[elem] = idx

        root = TreeNode(preorder[0])

        for elem in preorder[1:]:
            node = TreeNode(elem)
            self.place(node, root, in_map)

        return root


    def place(self, node, root, in_map):
        if in_map[node.val] > in_map[root.val]:
            if root.right:
                self.place(node, root.right, in_map)
            else:
                root.right = node
        else:
            if root.left:
                self.place(node, root.left, in_map)
            else:
                root.left = node



foo = [3, 9, 20, 15, 7]
bar = [9, 3, 15, 20, 7]

sol = Solution()
res = sol.buildTree(preorder=foo, inorder=bar)
        