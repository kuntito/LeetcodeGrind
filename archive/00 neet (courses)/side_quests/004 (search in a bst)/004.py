# https://leetcode.com/problems/search-in-a-binary-search-tree/


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f'''Node(
    {self.val},
    left={self.left},
    right={self.right}
)'''

class Solution:
    def searchBST(self, root: Node, val: int):
        node = root
        while node:
            if node.val == val:
                return node
            elif val > node.val:
                node = node.right
            else:
                node = node.left

        return node
    

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
seven = Node(7)

two.right = three
two.left = one
four.left = two
four.right = seven

foo = Solution()
val = 28
res = foo.searchBST(four, val)

print(res)