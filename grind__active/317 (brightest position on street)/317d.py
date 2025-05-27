# https://leetcode.com/problems/brightest-position-on-street/description/

from collections import defaultdict
import heapq
from typing import List
import sys

# i want to implement a function `brightestPosition`
# it takes a 2d integer array, `lights` and returns an integer

# each element of lights is a list of 2 integers, (position, range)

# position indicates a integer on a number line
# that number can be said to represent a lightbulb
# a lightbulb at `position` and covers the range `(position-range, position+range)`

# our job is to find the brightest position on that number line
# what position has the most lights on it

# if there are multiple of such positions, we should return the smallest one

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        intervals = self.getIntervals(lights)
        intervals.sort()
        
        # print(intervals)
        
        # store the open intervals
        # store the start position of every range
        # the illumination of a start position is a measure of how many unclosed intervals there are
        # store this in a hashmap and track the largest and smallest start
        openIntervals = []
        valMap = defaultdict(int)
        
        res = None
        for start, end in intervals:
            while openIntervals and start > openIntervals[0]:
                heapq.heappop(openIntervals)
            
            heapq.heappush(openIntervals, end)
            
            valMap[start] = len(openIntervals)
            
            if res is None or valMap[start] > valMap[res]:
                res = start
                
        return res
            

    def getIntervals(self, lights):
        intervals = []
        
        for pos, x in lights:
            low = pos - x
            high = pos + x
            
            intervals.append((low, high))
            
        return intervals
    
arr = [
    [[5,2],[-4,2],[1,1]],
    [[1,0],[0,1]],
    [[1,2]],
    [[-3,2],[1,2],[3,3]],
    [[3,4],[2,10],[-4,8],[5,7],[3,6],[3,6]], # TODO wrong assumption
]
foo = arr[-1]
sol = Solution()
res = sol.brightestPosition(foo)
print(res)