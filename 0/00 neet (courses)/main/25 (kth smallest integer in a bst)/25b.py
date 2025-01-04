class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def kthSmallest(self, root, k: int) -> int:
        stack = [root]
        seen = set()
        seen.add(root)

        count = 0
        while stack:
            cur = stack[-1]
            while cur.left and cur.left not in seen:
                cur = cur.left
                seen.add(cur)
                stack.append(cur)
            else:
                stack.pop()
                count += 1
                if count == k:
                    return cur.val
                if cur.right:
                    stack.append(cur.right)

five = TreeNode(5)
six = TreeNode(6)
three = TreeNode(3)
four = TreeNode(4)
two = TreeNode(2)
one = TreeNode(1)

two.left = one
three.left = two
three.right = four
five.left = three
five.right = six

foo = Solution()
res = foo.kthSmallest(five, 3)

print(res)

