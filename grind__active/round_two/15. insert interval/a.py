from typing import List

# what are we doing here..

# i'm given a array of intervals.. each interval is an array
# with two values, `start` and `end`

# none of the intervals in the array are overlapping. that said, i'm then given another interval and asked to insert it into the array..

# if any intervals overlap, i should merge them
# for instance, 

# if the array is [(1, 2), (4, 5)]

# and i'm given (3, 5) to insert..
# this overlaps with (4, 5)
# so the new interval should a merge of them..

# (3, 5) merges with (4, 5)
# and i'd have (3, 5)

# hence the result array would be [(1, 2), (3, 5)]

# how would you write this in code..
# i'd iterate through the entire array..

# to find the overlap, or insertion point,
# i'm considering the start and end of our new interval..

# what if the interval fits best at the start..

# say, arr = [(4, 5)]
# and you want to insert (1, 2)

# how would you address this..
# this can still be addressed in one pass..

# while i'm at (4, 5)
# before that, i'd create the result array, `res`

# while i'm at (4, 5), i'm comparing the the start of the new interval with the start of this

# i'm also comparing the end of the new interval with the start of this.. in essence, i want to see if there's an overlap...

# for the start..

# what am i talking about?
# for each interval, i iterate through, i'm asking one of two questions..

# 1. do i insert the new interval before this?
# 2. do i merge it with this...

# and the moment, i insert the new interval
# or i complete a merge, the problem ends, since i can append whatever's left in the array to `res`


# so let's address the questions one at a time..
# if i want to insert..

# it would mean, the end of `newInterval` is less than the start of current interval.. if this is the case..
# add to `res`, append the rest of the array to `res`
# case closed..

# i just thought of an edge case, there's a third condition, kind of..
# i know i said:
# 1. do i insert the new interval before this?
# 2. do i merge it with this...

# but what if i want to insert after the current interval?
# i ignored this case, since this condition is always addressed at the next interval..

# consider intervals [a, b]
# asking should i insert after `a`
# is the same as should i insert before `b`

# so this case would be handled when i reach `b`.
# the problem is at the last element..

# what if i want to insert after `b`?
# how would that go?

# let's keep this in mind, i can write a simple check for this..
# rather than force the loop to be dynamic to accept this..

# let's deal with the merge situation..
# if it's a merge.. how would you even find out..

# (2, 5)
# (3, 8)

# a merge means the lesser end, is less than the bigger end.
# for interval one, (2, 5), end is 5
# for interval two, (3, 8), end is 8

# 5 < 8, okay.. but what if inteval two was (6, 8)
# 5 would still be less than 8, but this wouldn't be an interval..

# so it's conditions, once the intervals are sorted by start..

# if startOne  < startTwo and endOne < end Two?? 
# still can be true without an interval (1, 2), (3, 4)

# the interval exists because somebody crosses the other
# how about if `endOne` is greater than `startTwo`

# i think this works.. because the intervals are sorted..
# we know, `startOne < startTwo`

# but since `endOne` > `startTwo`
# it means the second interval, starts before the first one ends..

# hence.. interval..

# okay, so once we have the interval what next, we can determine the new interval
# (
#     min(startOne, startTwo),
#     max(endOne, endTwo),
# )

# okay, so what do we do with this.. add it to res?
# i'm tempted to say yes but what if the merge extends to the next array?

# what do you mean
# consider the array [(2, 5), (6, 8)]

# and the insertion is (3, 10)
# in this case, we would rightfully merge with (2, 5)
# but if we insert... how would we consider that (6,8) fits into the mix too..
# well we can check with the next element if it exists..

# if there's an overlap there, we'd simply update the insert inteval to now be (2, 10)
# and work with the same logic..

# we keep doing this till we find out the next interval is not merging or there is no next interval
# at which point we add..

# also, we could just check at the start, for the edge case i mean
# if new interval's start is after arr[-1].end, then just append it to the array
# and call it a day..

# TODO look at solution for clean logic implementation...

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        if newInterval[0] > intervals[-1][1]:
            intervals.append(newInterval)
            return intervals
        
        
        res = []
        for idx, inval in enumerate(intervals):
            pass
            # if insert before
            if newInterval[1] < inval[0]:
                res.append(newInterval)
                
                # i want to append the slice from this index onwards..
                res.extend(intervals[idx:])
                return res
            
            is_merge, newInterval = self.is_overlap(inval, newInterval)
            # if merge
            if is_merge:
                if (idx + 1 == len(intervals)) or (newInterval[1] < intervals[idx + 1][0]):
                    res.append(newInterval)
                    # i want to append the slice..
                    res.extend(intervals[idx + 1:])
                    return res
            else:
                res.append(inval)
                
        return res
                
    def is_overlap(self, ivOne, ivTwo):
        arr = [ivOne, ivTwo]
        arr.sort()
        
        endOne = arr[0][1]
        startTwo = arr[1][0]
        
        is_merge = endOne >= startTwo
        if is_merge:
            newInterval = [
                min(arr[0][0], arr[1][0]),
                max(arr[0][1], arr[1][1]),
            ]
        else:
            newInterval = ivTwo
        
        return is_merge, newInterval

arr = [
    [[[1,3],[6,9]], [2, 5]],
    [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]],
    [[[1,5]], [0, 0]]
]
foo, bar = arr[-1]
sol = Solution()

res = sol.insert(foo, bar)
print(res)