# https://leetcode.com/problems/min-cost-to-connect-all-points/

import heapq
class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        dim = len(points)
        # for hashing, convert each point to a tuple
        points = [(x, y) for x, y in points]
    
        # create a weighted graph for all the points
        graph = self.create_graph(points)
        print(graph)
        
        # find the MST for all points
        seen = set()
        
        # pick any point as the starting
        # put all it's neighbours in a heap sorted by weights
        # res += `the weight of the current unvisited node`
        
        res = 0
        minHeap = [(0, points.pop())]
        while len(seen) < dim:
            pass
            dist, pt = heapq.heappop(minHeap)
            # TODO continue from here
        
        
    def create_graph(self, points):
        graph = {}
        
        for pt in points:
            graph[pt] = []
        
        dim = len(points)
        for i in range(dim):
            for j in range(i+1, dim):
                ptOne, ptTwo = points[i], points[j]
                dist = self.get_manhattan_distance(
                    ptOne,
                    ptTwo
                )
                
                graph[ptOne].append((ptTwo, dist))
                graph[ptTwo].append((ptOne, dist))
                
        return graph
                
                
                
    def get_manhattan_distance(self, posOne, posTwo):
        x1, y1 = posOne
        x2, y2 = posTwo
        
        return abs(x1 - x2) + abs(y1 - y2)
    


arr = [
    [[0,0],[2,2],[3,10],[5,2],[7,0]],
    [[0,0],[2, 2]],
]
foo = arr[-1]
sol = Solution()
res = sol.minCostConnectPoints(foo)