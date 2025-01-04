# https://leetcode.com/problems/binary-tree-inorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'


class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        arr = []
        if not root:
            return arr
        
        preorder = []
        arr.append(root)

        while arr:
            curr = arr.pop()
            preorder.append(curr.val)

            if curr.right:
                arr.append(curr.right)
            if curr.left:
                arr.append(curr.left)

            
        return preorder
    
one = TreeNode(1)
two = TreeNode(2)
three = TreeNode(3)
four = TreeNode(4)
five = TreeNode(5)
six = TreeNode(6)
seven = TreeNode(7)

# two.left = four
# two.right = five
# three.left = six
# three.right = seven
# one.left = two
# one.right = three

two.left = three
one.right = two

sol = Solution()
res = sol.preorderTraversal(one)
print(res)