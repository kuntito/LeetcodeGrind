# https://leetcode.com/problems/minimum-height-trees/description/

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        pass
        # create adjacency graph
        graph = self.get_adjacency(n, edges)
        for k, v in graph.items():
            print(k, '=>', v)
        
        # create a hashmap for (node => minHeight)
        # for each node, explore it's minimum height without cycles
        
    def explore(self, node, graph, seen):
        pass
        seen.add(node)
        if node in seen:
            pass
            # TODO what do you do for cycles?
    
        for nei in graph[node]:
            # node should not explore it's parent
            if nei == node:
                continue
            self.explore(nei, graph, seen)
        
        
        
        
    def get_adjacency(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
            
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)
        
        return graph
    
arr = [
    [4, [[1,0],[1,2],[1,3]]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findMinHeightTrees(foo, bar)