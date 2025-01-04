# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        res = []
        if not root: return res

        queue = deque()
        queue.append(root)
        while queue:
            lst = []
            for _ in range(len(queue)):
                item = queue.popleft()
                lst.append(item.val)
                if item.left:
                    queue.append(item.left)
                if item.right:
                    queue.append(item.right)
            res.append(lst)

        return res


three = TreeNode(3)
nine = TreeNode(9)
twenty = TreeNode(20)
fifteen = TreeNode(15)
seven = TreeNode(7)

twenty.left = fifteen
twenty.right = seven
three.left = nine
three.right = twenty

foo = Solution()
res = foo.levelOrder(three)

print(res)
        