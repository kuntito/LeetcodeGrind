# https://leetcode.com/problems/binary-tree-right-side-view/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        res = []
        if not root: return res

        queue = deque()
        queue.append(root)

        while queue:
            res.append(queue[-1].val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
    
