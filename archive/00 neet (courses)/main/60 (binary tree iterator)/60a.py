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
        self.inorder = deque()
        curr = root
        arr = []

        while arr or curr:
            if curr:
                arr.append(curr)
                curr = curr.left
            else:
                parent = arr.pop()
                self.inorder.append(parent.val)
                curr = parent.right


    def next(self) -> int:
        return self.inorder.popleft()

    def hasNext(self) -> bool:
        return bool(self.inorder)
    
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
