# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Node) -> list:
        arr: list[Node] = []
        post_order = []
        if root:
            arr.append(root)

        while arr:
            curr = arr[-1]

            if curr.left is None and curr.right is None:
                post_order.append(
                    arr.pop().val
                )
                continue

            if curr.right:
                arr.append(curr.right)
                curr.right = None
            if curr.left:
                arr.append(curr.left)
                curr.left = None
            
        
        return post_order
    
