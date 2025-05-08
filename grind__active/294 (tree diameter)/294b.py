# https://leetcode.com/problems/tree-diameter/description/

from collections import defaultdict
from typing import List


# TODO your assumption or algorithm is wrong
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        pass
        # i'd say create a graph
        # run dfs on every node, store the longest path found

        graph = self.createGraph(edges)
        n = len(edges) + 1

        

        maxDiameter = 0
        seen = set()
        memo = {}
        for node in range(n):
            memo[node] = self.explore(node, graph, seen, memo)
            maxDiameter = max(
                maxDiameter,
                memo[node],
            )

        print(memo)
        return maxDiameter - 1

    def createGraph(self, edges):
        graph = defaultdict(list)
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)

        return graph

    def explore(self, node, graph, seen, memo):
        if node in memo:
            return memo[node]
        
        seen.add(node)

        depth = 0
        for nei in graph[node]:
            if nei in seen: continue
            depth = max(depth, self.explore(nei, graph, seen, memo))

        seen.remove(node)

        return depth + 1
    
arr = [
    [[0,1],[0,2]],
    [[0,1],[1,2],[2,3],[1,4],[4,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.treeDiameter(foo)
print(res)