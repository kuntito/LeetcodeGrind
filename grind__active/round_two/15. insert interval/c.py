from typing import List

# i know why it works, let me rewrite..
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx, currInterval in enumerate(intervals):
            currStart, currEnd = currInterval
            
            newStart, newEnd = newInterval
            # if the new interval ends before the next one
            if newEnd < currStart:
                res.append(newInterval)
                return res + intervals[idx:]
            
            # this is where the intuition lies, we know `intervals` is sortec
            # now, if we're at this point
            # it means, newInterval doesn't end before current inteval
            # they either overlap or it starts after..
            
            # this condition is checking if the newInterval ends on or after
            # the next one starts, and the new interval starts on or before the current one
            # ends, there's an overlap
            
            # however, i think it's a verbose check
            # currently, it's `newEnd >= currStart and newStart <= currEnd`
            
            # since, we know there's only two scenarios.
            # an overlap or it starts afterwards
            # we simply need to check that new interval starts on or before current one ends.
            # so `newStart <= currEnd`
            if newStart <= currEnd:
                newInterval = [
                    min(newStart, currStart),
                    max(newEnd, currEnd)                    
                ]
            else:
                res.append(currInterval)
                
        res.append(newInterval)
        
        return res
