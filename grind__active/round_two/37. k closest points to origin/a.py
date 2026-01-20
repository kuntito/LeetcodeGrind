# https://leetcode.com/problems/k-closest-points-to-origin/description/

from typing import List

# i'm given an array of coordinates, `points`
# and an integer `k`

# what do i do with them?
# i want to return the k closest points to the origin (0, 0)

# i'm told the answer is guaranteed to be unique..

# right, how would this go?
# off the dome.. i'd iterate through `points`
# for each one.. i'd calculate it's distance from origin

# then what, that's where a min heap comes in..
# for each point, i'd store an item in the min heap
# [pointDistanceToOrigin, pointCoordinates]
# and at the end of the iteration..

# i'd pop the first `k` elements from the heap
# and everyone goes home safely

# i made an error, where, for the result array..
# i popped each heap item.. 

# [pointDistanceToOrigin, pointCoordinates]
# while that is necessary, what i really want to return is the `pointCoordinates`

# so, [pointDistanceToOrigin, pointCoordinates][1]

import heapq, math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        
        for p in points:
            dist = self.getDistanceToOrigin(p)
            
            heapq.heappush(
                minHeap,
                (dist, p)
            )
            
        res = [heapq.heappop(minHeap)[1] for _ in range(k)]
        return res
    
    def getDistanceToOrigin(self, p):
        x1, y1 = 0, 0
        x2, y2 = p
        
        x_dist = (x1 - x2) ** 2
        y_dist = (y1 - y2) ** 2
        
        return math.sqrt(x_dist + y_dist)
        