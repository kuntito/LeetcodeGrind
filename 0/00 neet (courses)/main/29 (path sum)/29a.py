# https://leetcode.com/problems/path-sum/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        return self.explore_sum(root, targetSum)
    

    def explore_sum(self, node: TreeNode, target: int):
        if not node: return False
        if self.is_leaf(node): return (target - node.val) == 0

        new_target = target - node.val
        return self.explore_sum(
            node.left,
            new_target
        ) or self.explore_sum(
            node.right,
            new_target
        )

    
    def is_leaf(self, node):
        return not (node.left or node.right)

        