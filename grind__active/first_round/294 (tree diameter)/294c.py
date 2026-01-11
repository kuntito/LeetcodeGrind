# https://leetcode.com/problems/tree-diameter/description/

from collections import defaultdict
from typing import List


# TODO TLE
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        pass
        # i'd say create a graph
        # run dfs on every node, store the longest path found

        graph = self.createGraph(edges)
        n = len(edges) + 1
        
        maxDiam = 0
        memo = {}
        seen = set()
        for node in range(n):
            memo[node] = self.explore(node, graph, seen, memo)
            maxDiam = max(maxDiam, memo[node])
            
        return maxDiam - 1
    
    def explore(self, node, graph, seen, memo): 
        seen.add(node)
        # every node counts as `1`
        maxDepth = 0
        for nei in graph[node]:
            if nei in seen: continue
            maxDepth = max(
                maxDepth,
                self.explore(nei, graph, seen, memo)
            )

        seen.remove(node)
        
        return maxDepth + 1
        


    def createGraph(self, edges):
        graph = defaultdict(list)
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)

        return graph


    
arr = [
    [[0,1],[0,2]],
    [[0,1],[1,2],[2,3],[1,4],[4,5]],
]
foo = arr[-1]
sol = Solution()
res = sol.treeDiameter(foo)
print(res)