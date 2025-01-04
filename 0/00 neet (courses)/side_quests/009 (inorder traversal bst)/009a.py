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
        arr = []
        inorder = []

        if not root:
            return inorder
        arr.append(root)

        seen = set()
        
        while arr:
            curr = arr[-1]
            seen.add(curr)

            if curr.left and curr.left not in seen:
                arr.append(curr.left)
            else:
                curr = arr.pop()
                inorder.append(curr.val)
                if curr.right:
                    arr.append(curr.right)

        return inorder
    
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

# one.left = two
# one.right = three
# two.left = four
# two.right = five

two.left = three
one.right = two

sol = Solution()
res = sol.inorderTraversal(one)

print(res)