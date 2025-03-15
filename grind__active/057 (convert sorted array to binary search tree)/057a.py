# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
# TODO https://neetcode.io/solutions/convert-sorted-array-to-binary-search-tree
class Solution:
    def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
        pass
        # a recursive function, `explore`
        # the middle of the array is the root node
        # the root node's left should point to `explore(nums[:mid])`
        # and the root node's right should point to `explore(nums[mid + 1:])`
        # if the array is empty return `None`
        return self.explore(nums)
        
    def explore(self, arr):
        if not arr: return None
        
        mid = len(arr) // 2
        
        node = TreeNode(
            arr[mid]
        )
        
        node.left = self.explore(arr[:mid])
        node.right = self.explore(arr[mid+1:])
        
        return node