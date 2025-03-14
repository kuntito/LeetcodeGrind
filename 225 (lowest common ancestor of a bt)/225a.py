# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/description/?envType=study-plan-v2&envId=amazon-spring-23-high-frequency

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        return f'({self.val})'
        
    def __repr__(self):
        return str(self)
        

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'list[TreeNode]') -> 'TreeNode':
        if len(nodes) == 1:
            return nodes[0]

        # create a structure where every node knows it's parents
        # get the paths for all nodes
        # find the first common node between them
        
        graph = self.createGraph(root)
        
        firstPath = [] # to preserve order of elements
        
        # add the node itself as part of it's path
        node = nodes[0]
        firstPath.append(node)
        while graph[node] != node:
            node = graph[node]
            firstPath.append(node)
            
        # print(firstPath)
            
            
        # get paths for all other nodes
        allPaths = []
        for n in nodes[1:]:
            path = set()
            
            # add the node itself as part of it's path
            path.add(n)
            while graph[n] != n:
                n = graph[n]
                path.add(n)
                
            allPaths.append(path)
            
        # for p in allPaths:
        #     print(p)
        
        
        for node in firstPath:
            # print(node)
            if all(node in s for s in allPaths):
                return node
            
        
    def createGraph(self, node):
        pass
        graph = {}
        
        self.exploreForParent(node, node, graph)
        
        return graph
        
    def exploreForParent(self, parent, node, graph):
        if not node:
            return
        
        graph[node] = parent
        
        self.exploreForParent(node, node.left, graph)
        self.exploreForParent(node, node.right, graph)
        
        
three = TreeNode(3)
five = TreeNode(5)
one = TreeNode(1)
six = TreeNode(6)
two = TreeNode(2)
zero = TreeNode(0)
eight = TreeNode(8)
seven = TreeNode(7)
four = TreeNode(4)

three.left = five
three.right = one

five.left = six
five.right = two

one.left = zero
one.right = eight

two.left = seven
two.right = four

sol = Solution()
# res = sol.lowestCommonAncestor(three, [seven, six, two, four])
res = sol.lowestCommonAncestor(three, [four, seven])

print('res is', res)
