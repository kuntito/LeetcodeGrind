# https://leetcode.com/problems/minimum-height-trees/description/

# TODO are there cycles? innocent until proven guilty
class Solution:
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        pass
        # one dfs call
        # where each node tracks the distance taken to reach it
        # and the furthest distance it can travel
        
        # use a hashmap to store the highest distance for each node
        # track the minimum distance
        # run through all the nodes, and grab the ids of the ones with the shortest distance
        self.minTravel = float("inf")
        
        graph = self.get_graph(n, edges)
        self.travelMap = {}
        
        seen = set()
        self.explore(0, graph, seen, 0)
        
        for i in range(n):
            print(i, '=>', self.travelMap[i])
        # res = [i for i in range(n) if self.travelMap[i] == self.minTravel]
        # return res
        
    def get_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = []
            
            
        for uno, dos in edges:
            graph[uno].append(dos)
            graph[dos].append(uno)
            
        return graph
        
    def explore(self, nodeVal, graph, seen, travelToNode):
        if nodeVal in seen:
            return
        
        seen.add(nodeVal)
        
        totalTravel = travelToNode
        furthestTravel = travelToNode
        
        for nei in graph[nodeVal]:
            if nei in seen: continue
            trav = self.explore(nei, graph, seen, travelToNode + 1)
            travelFromNode = trav - travelToNode
            
            furthestTravel = max(furthestTravel, travelFromNode)
            totalTravel = max(totalTravel, trav)
            
        self.travelMap[nodeVal] = furthestTravel
        self.minTravel = min(
            self.travelMap[nodeVal],
            self.minTravel
        )
        
        return totalTravel
    
arr = [
    [4, [[1,0],[1,2],[1,3]]],
    [6, [[3,0],[3,1],[3,2],[3,4],[5,4]]]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findMinHeightTrees(foo, bar)
print(res)