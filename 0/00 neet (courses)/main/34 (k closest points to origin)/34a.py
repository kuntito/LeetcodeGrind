# https://leetcode.com/problems/k-closest-points-to-origin/description/

import math
import heapq

class Solution:
    def kClosest(self, points: list, k: int) -> list:
        point_distances = []
        distances = {}
        for p in points:
            dist = self.get_distance(p)
            point_distances.append(dist)
            if dist not in distances:
                distances[dist] = []
            distances[dist].append(p)

        heapq.heapify(point_distances)
        res = []
        for _ in range(k):
            dist = heapq.heappop(point_distances)
            res.append(distances[dist].pop())
        
        return res
    

    def get_distance(self, point):
        x, y = point
        return math.sqrt(x*x + y*y)
    

sol = Solution()
points = [[3, 3], [5, -1], [-2, 4]]
k = 2

sol = Solution()
points = [[1, 3], [-2, 2]]
k = 1

res = sol.kClosest(points, k)
print(res)