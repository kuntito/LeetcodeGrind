# https://leetcode.com/problems/non-overlapping-intervals/description/

# TODO https://neetcode.io/solutions/non-overlapping-intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        pass
        intervals.sort()
        print(intervals)
        
        count = 0
        # `prevEnd` represents the ending of the previous interval
        prevEnd = None
        
        for start, end in intervals:
            # it is initialized as the ending of the first interval
            if prevEnd is None:
                prevEnd = end
                continue
            
            # this means the current interval overlaps with the previous one
            if start < prevEnd: 
                # so one of them has to be removed, thereby increasing the count by `1`
                count += 1
                
                # but which interval is removed?
                # the one with the earlier end time, since this reduces the chances of further overlap
                prevEnd = min(end, prevEnd)
            else:
                # in this case, no overlap so `prevEnd` is updated to the current interval's end
                prevEnd = end

                
        return count
            

                        


arr = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[0,2],[1,3],[2,4],[3,5],[4,6]],
    [[1,11],[1,100],[2,12],[11,22]],
]
foo = arr[-1]
sol = Solution()

res = sol.eraseOverlapIntervals(foo)

print(res)