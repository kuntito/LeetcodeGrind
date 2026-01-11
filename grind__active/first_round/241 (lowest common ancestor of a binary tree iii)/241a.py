# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        
    def __repr__(self) -> str:
        return str(self)
    
    def __str__(self) -> str:
        return f'({self.val})'


class Solution:
    def lowestCommonAncestor(self, p: Node, q: Node) -> Node:
        pass
        # find the paths to root for both nodes
        pPath = self.getPath(p)
        qPath = self.getPath(q)
        
        shorter, longer = (qPath, pPath) if len(qPath) < len(pPath) else (pPath, qPath)
        
        # return the first common node in both paths 
        for node in shorter:
            if node in longer:
                return node


    def getPath(self, node) -> set:
        paths = []
        while node:
            paths.append(node)
            node = node.parent
            
        return paths
    
zero = Node(0)
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)

two.left = seven
two.right = four

five.left = six
five.right = two

three.left = five
three.right = one

one.left = zero
one.right = eight

seven.parent = two
four.parent = two

two.parent = five
six.parent = five

five.parent = three
one.parent = three

zero.parent = one
eight.parent = one

sol = Solution()
res = sol.lowestCommonAncestor(five, four)
print(res)