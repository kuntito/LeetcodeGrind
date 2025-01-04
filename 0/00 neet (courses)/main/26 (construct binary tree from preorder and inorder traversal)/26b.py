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

        # pre_map = {}
        # for idx, elem in enumerate(preorder):
        #     pre_map[elem] = idx


        in_map = {}
        for idx, elem in enumerate(inorder):
            in_map[elem] = idx


        visited = set()
        return self.explore_orders(
            start=0,
            end=len(preorder),
            preorder=preorder,
            inorder=inorder,
            in_map=in_map,
            visited=visited,
        )


    def explore_orders(
        self,
        start: int,
        end: int,
        preorder: list,
        inorder: list,
        in_map: dict,
        visited: set,
    ):
        if start >= end: return None

        item = preorder[start]
        node = TreeNode(item)
        visited.add(item)

        idx = in_map[item] - 1
        num_items_on_left = 0

        while idx > -1 and inorder[idx] not in visited:
            num_items_on_left += 1
            idx -= 1
            

        left_start = start + 1
        left_end = left_start + num_items_on_left
        node.left = self.explore_orders(
            start = left_start,
            end = left_end,
            preorder=preorder,
            inorder=inorder,
            in_map=in_map,
            visited=visited,
        )


        node.right = self.explore_orders(
            start=left_end if left_end > left_start else left_start,
            end=end,
            preorder=preorder,
            inorder=inorder,
            in_map=in_map,
            visited=visited,
        )

        return node