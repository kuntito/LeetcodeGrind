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
        in_map = { elem: i for i, elem in enumerate(inorder) }
        return self.explore(preorder, inorder, in_map)
    
    def explore(self, preorder, inorder, in_map):
        if not preorder:
            return None

        # the first element in `preorder` is always the root
        root = Node(preorder[0])
        
        # the left child of root would be somewhere in the slice `preorder[1:]`
        # since preorder traversal is root => (leftBranch & rightBranch)
        
        # however, the length of this slice is determined by how many elements are in the leftBranch
        # to determine that, use the `inorder` array
        # find the index of root in the inorder array
        # everything in `inorder[:root_inorder_idx]` is the leftBranch of root
        # using this, you can determine the end index of the preorder slice
        
        # `preOrder[1: root_inorder_idx + 1]`
        # `root_inorder_idx + 1` effectively represents the length of the leftBranch
        # since `root` is always at index `0` in `preorder`
                
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