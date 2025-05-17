# https://leetcode.com/problems/tree-diameter/

# i want to implemente a function, `treeDiameter`
# it takes a 2d integer array and returns an integer

# the 2d integer array represent the edges of a tree
# each element of the array can be represented as [a, b]
# where `a` and `b` are connected nodes in the tree

# our job is to find the diameter of the tree
# the diameter is the number of edges in the longest path in the tree

# for one, we'd need to construct the tree
# staring a the tree, the longest path would have to exist between two nodes that only have a single edge

# what if a cycle exists?
# would this matter? consider a bruteforce approach where you explore every node
# and you track the furthest you could travel

# using a visiting set to avoid cycles
# this way, the answer should emerge

# TODO, read editorial! your solution is TLE
# having to explore every node for the longest edge is troubling
class Solution:
    def treeDiameter(self, edges: list[list[int]]) -> int:
        pass
        self.dim = len(edges) + 1
        tree = self.createTree(edges)
        
        longest = 0
        visiting = set()
        for i in range(self.dim):
            foo = self.explore(i, visiting, tree)
            if foo > longest:
                longest = foo
                
        return longest - 1
    
    def explore(self, node, visiting, tree):
        if node in visiting:
            return 0
        
        visiting.add(node)
        
        longest = 0
        for nei in tree[node]:
            foo = self.explore(nei, visiting, tree)
            if foo > longest:
                longest = foo
    
        visiting.remove(node)
        
        return longest + 1
    
        
    def createTree(self, edges):
        
        tree = {}
        for i in range(self.dim):
            tree[i] = []
            
        for uno, dos in edges:
            tree[uno].append(dos)
            tree[dos].append(uno)
            
        return tree
    
arr = [
    [[0, 1], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]],
]
foo = arr[-1]
sol = Solution()
res = sol.treeDiameter(foo)
print(res)
