# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        res = []
        self.explore_arr(root, res, k)
        return res[-1]

    def explore_arr(self, node: TreeNode, arr: list, k: int):
        if not node:
            return
        
        if self.explore_arr(node.left, arr, k):
            return True
        
        arr.append(node.val)
        if (len(arr) == k):
            return True
        
        if self.explore_arr(node.right, arr, k):
            return True