# https://leetcode.com/problems/brightest-position-on-street/description/

from collections import defaultdict
from typing import List

# what if we determined all the ranges
# sorted them in order
# now we want to find the most overlaps

# we might be able to do it an O(n)
# but let me visualize the intervals

# if you deep it, the most lit position would always be the start of an interval
# so if we track the start of every interval in a dictionary
# every time the start position overlaps the with previous, we incrememnt it
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        pass
        intervals = self.getIntervals(lights)
        intervals.sort()
        
        print(intervals)
        
        mostLit = None
        posMap = defaultdict(int)
        prevEnd = None
        for idx, x in enumerate(intervals):
            start, end = x
            
            posMap[start] += 1
            
            if prevEnd and start <= prevEnd:
                posMap[start] += 1
            
            if mostLit is None:
                mostLit = start
            elif posMap[start] > posMap[mostLit]:
                mostLit = start
                
            if idx + 1 < len(intervals) and end >= intervals[idx + 1][0]:
                posMap[end] += 1
                
            if posMap[end] > posMap[mostLit]:
                mostLit = end
                
            prevEnd = end
            
        return mostLit
 
        
    def getIntervals(self, lights):
        intervals = []
        
        for pos, x in lights:
            low = pos - x
            high = pos + x
            
            intervals.append((low, high))
            
        return intervals

    
arr = [
    [[5,2],[-4,2],[1,1]],
    [[-3,2],[1,2],[3,3]],
    [[1,0],[0,1]],
    [[1,2]],
    [[3,4],[2,10],[-4,8],[5,7],[3,6],[3,6]], # TODO wrong assumption
]
foo = arr[-1]
sol = Solution()
res = sol.brightestPosition(foo)
print(res)