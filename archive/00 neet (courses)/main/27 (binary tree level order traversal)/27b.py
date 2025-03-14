class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        res = []
        if not root: return res

        arr = [root]

        idx = 0
        while idx < len(arr):
            lst = []
            for _ in range(idx, len(arr)):
                item = arr[idx]
                lst.append(item.val)
                if item.left:
                    arr.append(item.left)
                if item.right:
                    arr.append(item.right)
                idx += 1
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