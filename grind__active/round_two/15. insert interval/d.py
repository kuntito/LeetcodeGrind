from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for idx, curInval in intervals:
            curStart, curEnd = curInval
            
            newStart, newEnd = newInterval
            
            if newEnd < curStart:
                res.append(newInterval)
                res.extend(intervals[idx:])
                return res
            
            if newStart <= curEnd:
                newInterval = [
                    min(curStart, newStart),
                    max(curEnd, newEnd)
                ]
            else:
                res.append(curInval)
                
        res.append(newInterval)
        
        return res