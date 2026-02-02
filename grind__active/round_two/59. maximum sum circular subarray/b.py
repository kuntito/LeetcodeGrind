# https://leetcode.com/problems/maximum-sum-circular-subarray/

from typing import List

# i'm given an array of integers, `nums`.

# i want to find the subarray with the largest sum.
# however, the array, `nums` is circular.

# meaning, the end of the array connects to the beginning.
# but why would this matter?

# consider the following example.
# nums = [4, -5, 10]
# if `nums` was linear, the subarray with the largest sum would be `[10]`
# but since, it circles.. `10` is connected to `4`

# so the subarray with the largest sum is actually [10, 4]
# which is `14`.

# so how would you solve this?
# if all the numbers were positive, we'd simply add all the numbers and get the result.
# however, negative numbers make things a bit tricky.

# what if you circled round the negative number, since it'd only bring down the sum..
# it makes sense to avoid it.. and if no negative number, sum up the entire array.

# the problem with that is a negative number can be part of the largest sum.
# consider:
# nums = [-2,4,-5,9,4]

# the sub array with the best sum is [9, 4, -2, 4]
# if we circle roung `-2`, best we would get is [9, 4]

# so, what's the approach?
# if we'd circled roung `-5`, we'd have gotten to [9, 4, -2, 4]
# but how would i know to pick `-5` and not `-2`

# well, it's the greater negative, but what if it was part of the sum?
# how so?
# consider:
# nums = [-2, 10, -5, 10, 10]

# how could `-5` be part of the largest sum? it's the largest negative..
# the sub array with the best sum, must be around the largest negative
# because whatever sum you generate around it, will only become lower if it gets to it..

# so am i looking for the largest negative number of a subarray with the greatest negatives..
# [-2, 10, -3, 2, -5, 10, 10]

# i think a series is best, in this case, the greatest negatives is [-3, 2, -5]
# what if the answer was `2`
# this would mean no number around [-3, 2, -5] could get to `2`
# if you consider nums as [-3, 2, -5]
# the largest negative becomes `-5`

# so i want to find the largest negative.. then perform a linear search around it for the subarray
# with the largest sum..

# okay, how do i find the largest negative.. it's basically a search for a negative streak..
# it can't be..

# if you did that for [-3, 2, -5]
# the entire thing is a negative streak.

# i think you just need to find the largest negative number..
# then do a linear sum around that.

# whatever you find must be the result.

# error, again, i set `startIdx = largestNegIdx` instead of `largestNegIdx + 1`

# error, i used the same variable name for two things:
#   def getLargestNegIdx(self, nums):
        # idx = 0
        # lowest = nums[0]
        
        # for idx, n in enumerate(nums):
        #     if n < lowest:
        #         lowest = n
        #         idx = idx
                
        # return idx
        
# i used `idx` to refer to the return index and same time the iterating index. 

# error, sometimes, the best sum is the value at the largest negative index
# what i did was initialize bestSum to that value

# error, sometimes, there's is no negative index,
# in that case, sum up all the values

# TODO, just rewrite this joint
# you're spiralling..
# the last failed test case is `[-1,3,-3,9,-6,8,-5,-5,-6,10]`
# i did iterate around the largest negative value `-6`
# but my assumptions were wrong.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        largestNegIdx = self.getLargestNegIdx(nums)
        if largestNegIdx is None:
            return sum(nums)
        
        startIdx = largestNegIdx + 1
        endIdx = startIdx + len(nums) - 1
        
        bestSum = nums[largestNegIdx]
        curSum = 0
        for idx in range(startIdx, endIdx):
            if curSum < 0:
                curSum = 0
            
            actualIdx = idx % len(nums)
            
            val = nums[actualIdx]
            curSum += val
            

            bestSum = max(
                curSum,
                bestSum
            )

        return bestSum
        
    def getLargestNegIdx(self, nums):
        res = None
        lowest = float("inf")
        
        for idx, n in enumerate(nums):
            if n < 0 and n < lowest:
                lowest = n
                res = idx
                
        return res
    
arr = [
    [5, -3, 5],
    [1,-2,3,-2],
    [-3, -2, -3],
    [3,1,3,2,6],
]

foo = arr[-1]
sol = Solution()
res = sol.maxSubarraySumCircular(foo)
print(res)