# https://leetcode.com/problems/binary-search-tree-iterator/description/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'

from collections import deque

class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self.go_left(root)

    def go_left(self, node: TreeNode):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        top = self.stack.pop()
        right_child = top.right
        if right_child:
            self.go_left(right_child)
        return top.val

    def hasNext(self) -> bool:
        return bool(self.stack)
    

three = TreeNode(3)
seven = TreeNode(7)
nine = TreeNode(9)
fifteen = TreeNode(15)
twenty = TreeNode(20)

fifteen.left = nine
fifteen.right = twenty
seven.right = fifteen
seven.left = three

sol = BSTIterator(seven)
print(sol.next())
print(sol.next())
sol.hasNext()
print(sol.next())
sol.hasNext()
print(sol.next())
sol.hasNext()
print(sol.next())
print(sol.hasNext())
