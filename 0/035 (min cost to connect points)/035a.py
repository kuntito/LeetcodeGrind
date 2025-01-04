# https://leetcode.com/problems/min-cost-to-connect-all-points/description/

import heapq

class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        points = [tuple(p) for p in points]

        adj = {}
        for p in points:
            adj[p] = []
        
        for i in range(len(points)):
            start = points[i]
            for j in range(i+1, len(points)):
                end = points[j]
                dist = self.get_distance(start, end)

                adj[start].append((dist, end))
                adj[end].append((dist, start))


        minHeap = []
        seen = set()
        first = points[0]
        seen.add(first)

        for nei in adj[first]:
            heapq.heappush(minHeap, nei)

        res = 0
        while len(seen) != len(points):
            dist, item = heapq.heappop(minHeap)

            if item in seen:
                continue
            seen.add(item)

            for nei in adj[item]:
                heapq.heappush(minHeap, nei)

            res += dist

        return res


    def get_distance(self, start, end):
        x1, y1 = start
        x2, y2 = end

        return abs(x1-x2) + abs(y1-y2)

arr = [
    [[0,0],[2,2],[3,3],[2,4],[4,2]],
    [[0,0],[2,2],[3,10],[5,2],[7,0]],
    [[3,12],[-2,5],[-4,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.minCostConnectPoints(foo)
print(res)