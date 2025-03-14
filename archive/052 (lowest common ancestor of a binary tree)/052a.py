# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'
    

class Solution:
    def lowestCommonAncestor(self, root: Node, p: Node, q: Node) -> Node:
        p_ancestors = []
        self.get_ancestors(root, p.val, p_ancestors)

        q_ancestors = []
        self.get_ancestors(root, q.val, q_ancestors)
        
        small, big = (p_ancestors, q_ancestors) if len(p_ancestors) < len(q_ancestors) else (q_ancestors, p_ancestors)

        seen = set(small)
        for node in big[::-1]:
            if node in seen:
                return node
        

    def get_ancestors(self, node, target, ancestors):
        if node is None:
            return False
        
        ancestors.append(node)
        
        if node.val == target:
            return True
        
        foo = self.get_ancestors(node.left, target, ancestors)
        if foo:
            return True
        
        bar = self.get_ancestors(node.right, target, ancestors)
        if bar:
            return True
        
        ancestors.pop()
        return False






three = Node(3)
five = Node(5)
one = Node(1)
six = Node(6)
two = Node(2)
zero = Node(0)
eight = Node(8)
seven = Node(7)
four = Node(4)

two.left = seven
two.right = four
five.left = six
five.right = two
one.left = zero
one.right = eight
three.left = five
three.right = one

sol = Solution()
res = sol.lowestCommonAncestor(three, five, four)
print(res)