# https://leetcode.com/problems/non-overlapping-intervals/description/

# TODO https://neetcode.io/solutions/non-overlapping-intervals
# deep solution
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        pass
        intervals.sort()
        print(intervals)
        
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            # if the current interval does not overlap with the previous interval
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
                
        return res
            

                        


arr = [
    [[1,2],[2,3],[3,4],[1,3]],
    [[1,2],[1,2],[1,2]],
    [[1,11],[1,100],[2,12],[11,22]],
    [[0,2],[1,3],[2,4],[3,5],[4,6]],
]
foo = arr[-1]
sol = Solution()

res = sol.eraseOverlapIntervals(foo)

print(res)