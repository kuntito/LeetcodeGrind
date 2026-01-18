# https://leetcode.com/problems/insert-interval/

from typing import List

# let's have another crack at this..
# new interval either goes before or after an existing interval
# or merges with one or more intervals..

# okay, how do i write this..
# for first case, before or after an interval, how do i do this..
# since intervals are sorted in ascending order by their `start`

# for each interval, find out if new interval fits in front or behind..
# no need for behind, since once we get to the next iteration, it would be taken care of..
# what do you mean?

# consider [firstInterval, secondInterval]
# inserting after `firstInterval` is the same as inserting before `secondInterval`
# so i only need to check for befores..
# well, yes, unless, we want to insert after the last interval..

# i think i can nullify this by checking from the jump.. 
# if the start of new interval is after the end of the last interval..
# append newInterval to the result array..

# this would handle the situation..
# you can simply append to the existing array and return that..

# okay, this way, i've addressed the first case of inserting before or after each interval..
# inserting afters is handled by the insert before of the next interval so i only ever have to check
# for insert befores..

# what else..
# the merge..
# wait, before this, what happens after insert.. well you can append to result array
# then continue the rest of the iteration..

# earlier, i did something where, i simply appended the slice from next index onwards.. [curIdx + 1 : ]
# but you don't want that.. you want current index onwards.. right..
# so the slice is [curIdx: ], it actually passes..

# but let's continue this and write it cleanly..
# the second case.. if it's a merge..
# if it's not an insert before, we check if it's a merge..
# i can make this it's own function..
# so if it's a merge, what do you want to do..
# i want to update new interval and not append any cells..

# so we keep going.. on each iteration, we still check if we can insert before
# this would be obviously False..then we check to merge again..  no, we check to see if we can insert the merge..

# why would we even get to this stage, the natural conclusion is, once you merge
# you want to add, but can't simply add since the merge could extend to the next cell
# i.e. inserting [1, 10] into [[1, 2], [3, 5]] would cross all cells..

# so you check if you can append the merged interval..
# what's this check like, we can append the merge if, the end of the interval < nextInterval[0]

# what if there's no next interval, well, then you can merge..

# okay.. what if you can't insert before, can't merge, simply append the curr interval

# always close, ifs or at least consider closing.. here, after checking if the merged interval can be attended
# i didn't consider the else case, where i want to make the merged interval the new interval..

# nother mistake, when i realize i append the merged interval..
# the workflow should be:
#   append merged interval
#   then add the rest of the array to the result
#   break iteration

# what i did was append the rest of the intervals..
# i should've extended the result array, not add another array into it.

# TODO this works but peep the clean solution, see `c.py`
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        if intervals[-1][1] < newInterval[0]:
            intervals.append(newInterval)
            return intervals
    
        # now, insert before or merge
        
        res = []
        for curIdx, curInterval in enumerate(intervals):
            if self.insertBefore(newInterval, curInterval):
                res.append(newInterval)
                res.extend(intervals[curIdx:])
                
                break
            
            elif self.isOverlap(curInterval, newInterval):
                mergedInterval = self.mergeIntervals(curInterval, newInterval)
                
                if self.canAppendMerge(mergedInterval, curIdx, intervals):
                    res.append(mergedInterval)
                    res.extend(intervals[curIdx + 1: ])
                    break
                else:
                    newInterval = mergedInterval
            else:
                res.append(curInterval)
                
        return res
    
    def insertBefore(self, candidateVal, curVal):
        return candidateVal[1] < curVal[0]
    
    # if sorted, firstVal, secondVal
    # and the end of firstVal >= secondVal's start..
    # there's an overlap
    
    # in summary
    # firstVal: i'm before you, i should end before you..
    # how do you know which is first, you'd have to sort..
    # or.. helper function
    # nah, i'd one line it.. ternary way... 
    # ternary is wrong.. least the way i did it, what i'm doing is unpacking the tuple
    # not getting the first and second..
    def isOverlap(self, valOne, valTwo):
        first = valOne if valOne[0] < valTwo[0] else valTwo
        second = valTwo if first is valOne else valOne
        
        return first[1] >= second[0]
    
    def mergeIntervals(self, valOne, valTwo):
        return [
            min(
                valOne[0],
                valTwo[0],
            ),
            max(
                valOne[1],
                valTwo[1],
            )
        ]
        
    def canAppendMerge(self, mergedInterval, curIdx, intervals):
        if curIdx + 1 == len(intervals):
            return True
        
        curInterval = intervals[curIdx]
        return mergedInterval[1] < curInterval[0]
    
arr = [
    [[[1,3],[6,9]], [2, 5]],
    [[[1,2],[3,5],[6,7],[8,10],[12,16]], [4, 8]],
    [[[1,5]], [0, 0]],
    [[[1,5]], [2, 3]],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.insert(foo, bar)
print(res)