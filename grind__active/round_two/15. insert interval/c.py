# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         res = []
#         for idx, currInterval in enumerate(intervals):
#             currStart, currEnd = currInterval
            
#             newStart, newEnd = newInterval
#             # if the new interval ends before the next one
#             if newEnd < currStart:
#                 res.append(newInterval)
#                 return res + intervals[idx:]
            
#             # if overlap, update the edges of newInterval
#             if currStart <= newEnd and currEnd >= newStart:
#                 newInterval = [
#                     min(newStart, currStart),
#                     max(newEnd, currEnd)                    
#                 ]
#             else:
#                 res.append(currInterval)
                
#         res.append(newInterval)
        
#         return res
