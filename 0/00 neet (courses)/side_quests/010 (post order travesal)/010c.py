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
        post_order = []
        self.explore_node(root, post_order)
        return post_order

    def explore_node(self, node, post_order: list):
        if not node: return
        if node.right is None and node.left is None:
            post_order.append(node.val)
            return

        self.explore_node(node.left, post_order)
        self.explore_node(node.right, post_order)
        post_order.append(node.val)

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)



five.left = six
five.right = seven
eight.left = nine
two.left = four
two.right = five
three.right = eight
one.left = two
one.right = three

sol = Solution()
res = sol.postorderTraversal(one)

print(res)