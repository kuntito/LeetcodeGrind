# https://leetcode.com/problems/tree-diameter/description/

from collections import defaultdict
from typing import List


# TODO still wrong, rewrite your thought process from the jump!
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        pass
        # i'd say create a graph
        # run dfs on every node, store the longest path found

        graph = self.createGraph(edges)
        n = len(edges) + 1

        # i think we only need to explore the graph once
        # the idea here is at every node, we want to know what it took to get to that node
        # and the deepest you can go from there

        # or we could say we want to know the number of nodes before it
        # and the number of nodes after it
        # with this we can deduce the diameter at that node

        self.maxDiam = 0

        # the recursive function would take four arguments
        # the current node, the number of nodes before, the graph and a set, `seen`
        self.explore(0, 0, graph, set())
        
        return self.maxDiam

    def explore(self, node, nodesBefore, graph, seen):
        seen.add(node)

        # go through each neighbour
        nodesAfter = 0
        for nei in graph[node]:
            if nei in seen:
                continue

            nodesAfter = max(
                nodesAfter, self.explore(nei, nodesBefore + 1, graph, seen)
            )
            
        self.maxDiam = max(self.maxDiam, nodesBefore + nodesAfter)
        
        return nodesAfter + 1

    def createGraph(self, edges):
        graph = defaultdict(list)
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)

        return graph


arr = [
    [[0, 1], [0, 2]],
    [[0, 1], [1, 2], [2, 3], [1, 4], [4, 5]],
]
foo = arr[-1]
sol = Solution()
res = sol.treeDiameter(foo)
print(res)
