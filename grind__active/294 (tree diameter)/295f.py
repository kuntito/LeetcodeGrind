# https://leetcode.com/problems/tree-diameter/editorial/

from typing import List

# the diameter of a tree is the number of edges between the farthest two nodes on the tree
# it can be solved using bfs intuition.

# according to leetcode editorial, however you use bfs to explore a tree
# the last node you encounter would be the most extreme node

# knowing this, we'd run bfs twice.
# the first time, we start from any node
# and we determine the most extreme node

# then starting from the determined extreme node
# we run another bfs to determine the second extreme node
# then keep track of how many steps it took to get there
# and voila

# but first we need to create the graph
# the edges are undirected and we have `n` nodes
# where `n = len(edges) + 1`
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        pass
    
        graph = self.getGraph(edges)
        
        # run bfs
        firstExtreme, _ = self.exploreBfs(0, graph)
        _, steps = self.exploreBfs(firstExtreme, graph)
        
        return steps - 1

        
        
    def exploreBfs(self, startNode, graph):
        lst = [startNode]
        
        seen = set() # to store visited nodes
        firstExtreme = None
        steps = 0
        while lst:
            arr = []
            while lst:
                curr = lst.pop()
                firstExtreme = curr
                seen.add(curr)
                
                for nei in graph[curr]:
                    if nei in seen: continue
                    arr.append(nei)
            lst = arr
            steps += 1
                    
        return firstExtreme, steps
    
        
    def getGraph(self, edges):
        n = len(edges) + 1
        graph = { i:[] for i in range(n) }
        
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)
            
        return graph
    
arr = [
    [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]],
    [[0, 1], [0, 2]],
]
foo = arr[-1]
sol = Solution()
res = sol.treeDiameter(foo)
print(res)