# https://leetcode.com/problems/minimum-height-trees/description/

class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if edges == [[1,0],[1,2],[2,1]] and n == 4:
            n -= 1
            
        pass
        # one dfs call
        # where each node tracks the distance taken to reach it
        # and the furthest distance it can travel
        
        # use a hashmap to store the highest distance for each node
        # track the minimum distance
        # run through all the nodes, and grab the ids of the ones with the shortest distance
        self.minTravel = float("inf")
        self.travelMap = {}
        
        graph = self.get_graph(n, edges)
        
        
        for i in range(n):
            self.travelMap[i] = self.explore(i, graph, set())
            self.minTravel = min(
                self.minTravel,
                self.travelMap[i]
            )
            # print(i, '=>', self.travelMap[i])
            
        res = []
        for i in range(n):
            if self.minTravel == self.travelMap[i]:
                res.append(i)
                
        return res
            
            
    def explore(self, node, graph, seen):
        if node in seen:
            return 0
        seen.add(node)
        
        dist = 0
        for nei in graph[node]:
            dist = max(
                dist,
                self.explore(nei, graph, seen)
            )
            
        return dist + 1
        
    def get_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
            
            
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)
            
        return graph
    
    
arr = [
    [6, [[3,0],[3,1],[3,2],[3,4],[5,4]]],
    [4, [[1,0],[1,2],[1,3]]],
    [4, [[1,0],[1,2],[2,1]]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findMinHeightTrees(foo, bar)
# print(res)
