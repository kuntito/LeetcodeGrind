# https://leetcode.com/problems/merge-intervals/

from typing import List

# i'm given a 2d array of intervals.., `intervals`
# each element of the array is [start, end]

# i'm post to merge all overlapping intervals and 
# return an array of non-overlapping intervals

# Nb:
# (1, 4) and (4, 5) are considered overlapping since they touch at the `4`s
# how would you approach this, i'd sort the intervals..

# this way i know the start time for every interval is sorted..
# i'd create a result array then iterate through `intervals`
# for every interval, i'd check if it ends before the next one..

# if it does, add it to result array
# if not, merge with next interval.. and proceed iteration
# by merge, i mean, update next inteval in place, so it has the new boundaries..

# say i had 
# (1, 4), (4, 5)
# i'd realize (1, 4) overlaps with the next interval (4, 5)
# so i'd turn (4, 5) into (1, 5)

# then proceed to next iteration which would now be (1, 5)
# then continue the same process..

# error, i didn't sort `intervals`
# error, i assumed the merge only entailed updating the start of nextVal to curStart
# i.e. nextVal[0] = curStart, since the intervals are sorted, `curStart` is bound to be less than or equal
# to nextVal's start, while True, this says nothing about curEnd

# for all we know, we could have..
# [2, 6], [3, 4], my previous approach would have updated to [2, 4]
# but what we want it [2, 6]

# it works but i wonder if there was more optimal solution from last time..

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        
        res = []
        dim = len(intervals)
        for idx, curVal in enumerate(intervals):
            curStart, curEnd = curVal
            
            nextIdx = idx + 1
            nextVal = intervals[nextIdx] if nextIdx < dim else None
            
            # if next val exists, and the current val overlaps with it..
            # update nextVal
            if nextVal and curEnd >= nextVal[0]:
                nextVal[0] = curStart
                nextVal[1] = max(curEnd, nextVal[1])
            else:
                res.append(curVal)
                
        return res