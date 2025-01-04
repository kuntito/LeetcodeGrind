# https://leetcode.com/problems/binary-tree-inorder-traversal/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'


class Solution:
    def inorderTraversal(self, root: Node) -> list[int]:
        inorder = []

        arr = []
        curr = root
        while curr or arr:
            if curr:
                arr.append(curr)
                curr = curr.left
            else:
                curr = arr.pop()
                inorder.append(curr.val)
                curr = curr.right
        return inorder
    

one = Node(1)
two = Node(2)
three = Node(3)

one.right = two
two.left = three

sol = Solution()
res = sol.inorderTraversal(one)

print(res)