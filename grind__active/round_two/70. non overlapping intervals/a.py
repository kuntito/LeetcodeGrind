# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List

# i'm given a 2d array of integers, `intervals`
# each element of the array is an interval with [start, end]

# i want to remove the least number of intervals from the 2d array
# such that the rest of the intervals are non-overlapping.

# it's worth noting, two intervals touching don't count as an overlap
# i.e. (2, 3) and (3, 4) are not overlapping.

# but how do i remove this joint?
# what elements do i remove..

# consider
# [[1,2],[2,3],[1,3]]

# for one, it's easier to see clearly if the integers are sorted.
# so, reconsider:
# [[1,2], [1,3], [2,3]]

# all three overlap..
# if i remove [1, 2]

# i'd have [[1, 3], [2, 3]]
# there's still an overlap, so i'd have to remove one of them..

# however, if we rewind, we'd see
# [[1,2], [1,3], [2,3]]
# if i remove [1, 3], 

# i'd be left with:
# [[1, 2], [2, 3]]

# but how do i know that's what i should remove?
# i only know now because trial and error.

# watched neet's tutorial, and the approach was to take each interval one at a time
# whenever an overlap occurs, you know you must remove one interval
# but which one, always remove the one that ends last..

# since it increases the chances of overlapping with something further..
# does that work for your example?

# [[1,2], [1,3], [2,3]]
# well yeah, [1, 2] and [1, 3] overlap
# so i'd remove [1, 3] then move on [2, 3]
# i see the don't overlap, so i'm good.

# how about [[1, 2], [1, 2], [1, 2]]
# first two [1, 2] and [1, 2]
# i'd remove the one than ends last, in this case, they're the same..
# so i'd remove one of them..

# next up is another [1, 2] and [1, 2]
# so..same story again..

# seems, i need to keep a reference to the previous interval on every iteration
# for the current interval, i want to confirm if it starts before the previous one ends..
# if it does, there's an overlap, and i want to remove the one that ends first..

# then update the prevEnd to whichever ends first between them...
# also, need to sort intervals.. first
# the first `prevEnd` is the end of the first interval

# so, it makes sense to iterate from the second element of `intervals` onwards

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        
        removals = 0
        prevEnd = intervals[0][1]
        for curStart, curEnd in intervals[1:]:
            if curStart < prevEnd:
                removals += 1
                # (1, 8), (2, 3), you want the prevEnd to point to `3` not `8`
                prevEnd = min(curEnd, prevEnd)
            else:
                prevEnd = curEnd
                
        return removals
    
arr = [
    [[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]],
]
foo = arr[-1]
sol = Solution()
res = sol.eraseOverlapIntervals(foo)
print(res)