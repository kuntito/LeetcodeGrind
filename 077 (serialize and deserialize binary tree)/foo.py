# Definition for a binary tree node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

# https://neetcode.io/solutions/construct-binary-tree-from-preorder-and-inorder-traversal
# 15:04


# each recursive function should have a preorder and inorder
# the first element of `preorder` is the root node
# TODO this works, implement it in `077a.py`
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]):
        pass
        if not preorder:
            return None

        in_map = { elem: i for i, elem in enumerate(inorder) }

        root = Node(preorder[0])
        # the left child of root would be in the slice `preorder[1:]`
        # however, the length of this slice is determined by how many elements
        # are leftwared of `root` in the `inorder`
        
        root_inorder_idx = in_map[root.val]
        
        
        root.left = self.buildTree(
            preorder[1: 1 + root_inorder_idx],
            inorder[:root_inorder_idx],
        )
        
        root.right = self.buildTree(
            preorder[1 + root_inorder_idx: ],
            inorder[root_inorder_idx + 1:]
        )
        
        return root
        
arr = [
    [[3,9,20,15,7], [9,3,15,20,7]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.buildTree(foo, bar)