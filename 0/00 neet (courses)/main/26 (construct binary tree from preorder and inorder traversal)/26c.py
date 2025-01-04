class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder:
            return None
        
        item = preorder[0]
        node = TreeNode(item)

        inorder_idx = inorder.index(item)

        left_end = inorder_idx + 1
        left_preorder = preorder[1:left_end]
        left_inorder = inorder[:inorder_idx]
        node.left = self.buildTree(
            preorder=left_preorder,
            inorder=left_inorder
        )

        right_preorder = preorder[left_end:]
        right_inorder = inorder[inorder_idx + 1:]
        node.right = self.buildTree(
            preorder=right_preorder,
            inorder=right_inorder
        )

        return node


a = [1, 2, 3]
print(a[:0])