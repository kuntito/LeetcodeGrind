# https://leetcode.com/problems/same-tree/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.explore_nodes(p, q)

    def explore_nodes(self, uno: TreeNode, dos: TreeNode) -> bool:
        if uno is None and dos is None:
            return True
        
        if uno and dos and uno.val == dos.val:
            return self.explore_nodes(
                uno.left if uno.left else None,
                dos.left if dos.left else None,
            ) and self.explore_nodes(
                uno.right if uno.right else None,
                dos.right if dos.right else None,
            )
        return False


two = TreeNode(2)
three = TreeNode(3)
one = TreeNode(1)

one.left = two
one.right = three


deux = TreeNode(2)
trois = TreeNode(3)
un = TreeNode(1)
un.left = deux
un.right = trois

sol = Solution()
res = sol.explore_nodes(un, one)

print(res)