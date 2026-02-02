# https://leetcode.com/problems/maximum-sum-circular-subarray/description/

from typing import List

# i'm given an array of integers, `nums`
# i want to find the subarray with the highest sum

# but there's a catch, the array `nums` should be treated as circular
# the end connects to the beginning

# does this change anything? i think it does.
# consider:

# [4, -5, 2, 3]
# for a linear array, the subarray with max sum is [2, 3] with adds up to `5`

# however, for a circular array.. you can keep going..
# you'd have [2, 3, 4] which sums up to `9`

# so how would you code this.. where would you start?
# i'd say start after a negative.. you can still treat this as a linear array
# if you start after the negative..

# what if there's a line of negatives? it wouldn't matter. 
# the point of the negative is to provide an end to the cycle.

# what if i had a circle of negatives? it wouldn't change anything..
# because we're treating the negative as the end point does not mean we exclude it

# we can set the initial best sum to the first negative number, then omit it from the entire iteration.
# the array starts after the negative and ends before it.

# in a circle of negatives.. if the omitted negative is the answer.
# because we access it at first, we'd have the answer.

# if it's just a random negative.. the postives around it
# would determine the max sum.

# there's no way to lose.
# once we have the linear array, we're back to the `maximum subarray` question.
# track the sum from the start, on each iteration, update max sum..
# once you hit a negative that wipes out the sum,
# restart the sum after the negative..

# curSum = 0
# then start over..

# how did this approach address, a linear array of negatives..
# say [-3, -1, -5]

# we'd start off with `-3`, track it..
# ..um, i wasn't explicit, but we know a sum has been wiped out when it hits negative..
# so on the next iteration, we see `curSum = -3 = wipe out`
# so we reset to zero, `curSum = 0`
# then add the new numebr, `curSum += -1`
# in this case the `curSum` becomes `-1`

# on second thought, we want to confirm the wipeout in each iteration..
# add the number, if wipe out, reset to 0

# so when do we update the maxSum so far..
# we should update it, before the reset..

# but what if, the value before the reset was reduced..
# elaborate..

# say our sum is 10
# next number is -11
# sum would get wiped out since it's not `-1`
# but we'd track `-1`
# then reset..

# what if `10` was our best sum..
# well, if `10` was the best sum
# we'd have reached `10` in the previous iteration..
# it's either we started with `10`, `curSum = 0 and curSum += 10`
# or we added a number to become `10`, `curSum + something = 10`
# in which case, we reach 10..
# track it,
# no need for a reset, move on to the next variable..

# let's try, see how it goes..
# find the index of the first negative number..
# store the value of first negative number somewhere..

# treat `nums` as a linear array that circles round that negative number
# get your result..

# return whichever's higher, your result of first negative number..
# problem solved..

# what if no negative number..
# return sum(nums)
# okay.. 

# error, with the linear array, i calculated the index using the firstNegIdx as starting point
# it should have been `firstNegIdx + 1`

# error, can't initialize current sum and maxSum to `0`
# in the event the array is all negative numbers, you'd end up returning `0` as the best sum
# even though `0` does not exist in the array
# a better approach is to use `float("-inf")`, lowest possible number ever

# pparently `float("-inf")` is not the way to go..
# `float("-inf") + anyNumber` is still equal to `float("-inf")`

# one idea is to bring the check for negative upwards at the start of the array
# not sure what this does to the whole thing...
# and reset curSum and bestSum to `0`
# but all negative sums?

# i think `curSum` can initialize to `0` and bestSum initializes to `float("-inf")`

# nother error, when comparing the linear result sum against first neg val..
# i didn't compare it against first neg val, instead i compared with it `nums[firstNegVal]`

# not sure what happens if i assign `bestSum as firstNegVal`

# still don't work, figure it out
# TODO [-2,4,-5,4,-5,9,4]
# i understand why my idea fails.
# i can't just go round the first negative, because it could be part of the best sum

# consider the example.. [-2,4,-5,4,-5,9,4]
# the best sum starts at the end of the array, `9`, `4` which is `13`
# then circles round to `-2` becomes `11`
# then proceeds to `4`, which becomes `15`
# this is the highest sum throughout the array.

# i simply can't go round the first negative.
# what if i go round the greatest negative, why would you be doing that?
# let's restart the process.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        firstNegIdx = self.getFirstNegIdx(nums)
        if firstNegIdx is None:
            return sum(nums)
        
        startIdx = firstNegIdx + 1
        endIdx = startIdx + len(nums) - 1
        
        bestSum = float("-inf")
        curSum = 0
        for maybeIdx in range(startIdx, endIdx):
            if curSum < 0:
                curSum = 0
                
            actualIdx = maybeIdx % len(nums)
            val = nums[actualIdx]
            
            curSum += val
            
            bestSum = max(
                curSum,
                bestSum
            )
            
        firstNegVal = nums[firstNegIdx]
        return max(bestSum, firstNegVal)
        
    def getFirstNegIdx(self, nums):
        for idx, n in enumerate(nums):
            if n < 0:
                return idx
            
        return None
    
arr = [
    [5,-3,5],
    [-3, -2, -3],
    [-2,4,-5,4,-5,9,4],
]

foo = arr[-1]
sol = Solution()
res = sol.maxSubarraySumCircular(foo)
print(res)
