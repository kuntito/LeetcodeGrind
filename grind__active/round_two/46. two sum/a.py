# https://leetcode.com/problems/two-sum/description/

from typing import List

# i'm given two things, an array of integers, `nums`
# and a number, `target`

# i'm told there are two numbers in `nums` that add up to `target`
# my job is to find those two numbers and return their indices.

# it's worth pointing out, the indices have to be different...
# how would this go..

# i'd have to check each element, at least to get the first number
# once i have the first number, arithmetic reveals what the second number should be..

# so, i'm essentially looking for first number, then find second number.
# off the dome, the first approach is for every number, search for it's second number

# this is a double loop..
# consider:

# nums = [5, 6, 2, 7]
# target = 9

# iterating through `nums`..
# our candidate for first number is `5`, our target is `9`
# so `5` would need a `4` to make `9`

# so our second number would be `4`
# does `4` exist in nums
# we'd have to check..

#  another iteration this time.. our array is [_, 6, 2, 7]
#  we'd check every element and not find a `4`
#  so we know `5` isn't our number

# we continue our iteration, next candidate for first number is `6`
# since target is `9`, we'd need a `3` with a `6`
# we do the same thing, where we check the rest of the array for `3`
# we woudln't find it..

# and thus come back to the first loop.
# at this point, it's obvious we're doing repeated work..
# having to check the rest of the array every time..

# it'd be nice to know if an element is the array once..
# that's where a set comes in..

# if we store every element in a set.. we can check in O(1) time..
# so this would be two passes, one where we populate the set

# another where we do the check..
# i know this, and know it works..

# but the powers above be, Navdeep Singh, revealed, i could do this in one pass..
# by populating the set while checking at the same time..

# the idea is every number you iterate through, `firstNumber`
# you check for it's partner, `secondNumber` in the set, if the partner isn't there..
# you add `firstNumber` to the set..

# but what if the `secondNumber` is in the array and we just haven't seen it yet..
# well, that's where it gets interesting..

# consider [2, 5, 7], target = 9
# at 2, we check for `7` in the set
# it's not there yet.. so we add `2` to the set..

# however, when we get to `7`
# we'd be looking for `2` and yes `2` is in the set..

# so we'd have our two numbers, the tricky part of this is..
# we actually have to reach the `secondNumber` before checking for the first..

# also, we need to return indices not the numbers themselves..
# so a dictionary works better than a set ..
# case closed..


# case reopened, my first approach of: populate set, then iterate would have failed on one edge case
# this: [3, 2, 4]

# if we populate our set, or dictionary, we'd have:
# {3:0, 2:1, 4:2}, [3, 2, 4]

# when we hit `3`, secondNumber would calculate to `3`
# and yes, `3` would exist in the dictionary but remember, we can't use the same index..
# so we would have to check for same index for this kind of situation..

# i know because i'd done this before..


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for idx, n in enumerate(nums):
            secondNumber = target - n
            
            if secondNumber in seen:
                return [idx, seen[secondNumber]]
            
            seen[n] = idx