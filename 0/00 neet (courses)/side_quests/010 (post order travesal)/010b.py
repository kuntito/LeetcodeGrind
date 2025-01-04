# https://leetcode.com/problems/binary-tree-postorder-traversal/description/

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
    def postorderTraversal(self, root: Node) -> list:
        arr: list[Node] = []
        post_order = []
        seen = set()

        if root:
            arr.append(root)

        while arr:
            curr = arr[-1]
            seen.add(curr)

            uno = curr.right and curr.right not in seen
            dos = curr.left and curr.left not in seen

            if not (uno or dos):
                post_order.append(
                    arr.pop().val
                )
                continue


            if uno:
                arr.append(curr.right)
            if dos:
                arr.append(curr.left)
            
        
        return post_order
    
one = Node(1)
two = Node(2)
three = Node(3)

two.left = three
one.right = two

sol = Solution()
res = sol.postorderTraversal(one)

print(res)
