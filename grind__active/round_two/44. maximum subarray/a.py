# https://leetcode.com/problems/maximum-subarray/description/

from typing import List

# i'm given a list of integers, `nums`, and want to find the subarray
# with the largest sum, and return that sum

# a subarray is a list of back to back elements in `nums`

# for instance:
# if `nums` is [2, 3, 4]

# [2] is a subarray
# [2, 3] is a subarray
# [2, 3, 4] is also a subarray, a array can be a subarray of itself.

# brute force.. from each element
# keep adding.. ideally, if you sum up the entire array
# you should have the largest subarray.

# yes, if all the integers were positive. the negative integers are what change the game.
# if you had `nums = [1, -10, 2]`
# your largest subarray is `[2]`

# okay, what you summed up numbers from the start
# but once you hit a negative, you keep what you've summed
# and restart another sum.

# okay..
# but consider..
# nums = [3, -1, 2]

# taking your approach, i'd have `3`, store it
# restart, now have `-1 + 2` = 1
# and my store would have `1` and `3`, returning `3` as the largest subarray
# but paying attention..

# the largest subarray is the entire array.
# [3, -1, 2]
# when you sum up the elements, you get `4`
# so a negative isn't exactly a problem.

# so why was `nums = [1, -10, 2]` problematic
# i think it's the value of the negative sum
# you best sum was `1` then you hit `-10`
# this takes out your sum and leaves you with `-9`

# the [3, -1, 2] example is different
# because `3 - 1 = 2`, you're still left with a positive sum
# after hitting a negative.. so you can keep going.

# negatives only matter if they wipe out your existing sum.
# okay, so sum from the start, track every sum, say, another variable, `bestSum`

# once, you get wiped out by a negative, restart the calculation.
# do we want to start the new sum with a negative?

# say, [1, -10, 1]
# when we hit `-10`, does the new sum start from `-10`
# i don't see why it should, we can simply start from the next non-negative sum..

# well, what if all the numbers were negative.
# say, [-12, -10, -7]
# in this case, there's no next non-negative sum
# hm..
# i guess for each negative, you still want to start from the next non-negative sum
# but first, you want to compare the current negative with the best sum so far.

# say we start `bestSum = float("-inf")`
# we'd compare it with `-12`, our best sum becomes `-12`
# we try to find the next non-negative number..
# we hit another negative, -10, .. we compare it with best sum
# bestSum becomes `-10`
# we search for the next non-negative..
# i'm starting to see the pattern here..

# we need not.. search for the next non-negative..
# just iterate through the array.

# the next number is either positive or negative
# if positive, we know to start a new sum
# if negative, we check against current best sum, reset our tracker to `0`
# move to next number
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = float("-inf")
        
        trackSum = 0
        for n in nums:
            trackSum += n
            
            bestSum = max(trackSum, bestSum)
            
            # if `trackSum` becomes negative..
            # reset to `0`
            if trackSum < 0:
                trackSum = 0
        
        return bestSum