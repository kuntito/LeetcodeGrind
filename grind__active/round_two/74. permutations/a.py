# https://leetcode.com/problems/permutations/
from typing import List

# i'm given an array of integers, `nums`
# i want to find all distinct permutations of the elementes of `nums`
# and return an array of those permutations.

# in clearer terms, i'm returning an array of an array.
# okay, so how would this go?

# what's a permutation?
# a rearrangement.

# a reordering.
# can you illustrate with an example?

# say `nums = [1, 2]`
# the two permutations would be it's default state:
# [1, 2]
# and the rearranged order [2, 1]

# how about [1, 2, 3]
# one permutation is the default state..

# okay, but what else?
# what are we doing when we permute?
# we want to consider every order of the elements.

# for starters, we have [1, 2, 3]
# okay, what else..
# what if we swap `2` and `3`
# then we'd have another one [1,3,2]
# okay..

# what if we swapped `1` and `3`
# then we'd have another one, [3, 1, 2]

# there should be some pattern to this..
# i can't just be randomly swapping elements.

# what if i keep one stagnant? and permute the others..
# well you could but that wouldn't end up being permutation, would it?

# at it's core, you want every element to be in every position
# for a 3-element array
# you have three slots

# _, _, _
# if i place `1` in the first slot
# `2` in the second slot
# `3` in the third slot

# thats one arrangement
# now, i go back track..
# at the second slot, what if i don't put `2`
# and put `3`

# that'd be another permutation..
# 1, 3, 2
# then i back track..

# i'm seeing a pattern here..
# a recursive pattern..

# at each step, i'd have available numbers..
# each step represents a slot..
# at each step, i want to place every available number in the slot

# then continue the recursion with what's left of these available numbers
# for the example above..

# the first step, the available numbers are 1, 2, 3
# i start with `1` = [1]

# then a recursive call,
# now, it's step 2
# the available numbers are 2 and 3
# i pick 2

# now it's step 3, the available number is only 3
# i pick 3

# now i go back to step 2.. previously i picked 2
# so now i pick 3

# picking 3 in step 2 means i approach step 3 with 2
# and so on and so forth..

# when you run out of numbers you note each array.
# that's a unique permutation.

# how would this go in code?

# a tracking array, `trackingArr`
# how would you track the available numbers..
# keep in mind you're removing one number
# exploring forward
# then when exploration returns, you re-add the number.

# say step `1`
# i'd always have 3 elements.

# at first i pick `1`, pass [2, 3] onwards
# when it comes back, i pick `2` then add `1` back to the array
# so i pass [1, 3]
# onwards..

# a deque can help me here..
# at each step, the length of the deque tells me how many elements
# i should remove..

# say i start with [1, 2, 3]
# i know i can only remove 3 elements

# so i remove 1, pass [2, 3]
# when exploration ends, i add `1` to the end of deque
# and pick `2`, so i'd pass [1, 3]

# the problem with this is the recursive calls also do this modification.
# wouldn't that mess things up..

# let's work through it
# you remove 1, pass [2, 3]
# step 2, you remove 2, pass [3]
# step 3, you remove 3, pass [], recursion ends..
# now you come back to step 2, add 2 to the end [3, 2]
# then remove `3`, pass `2` and so on..

# by the time this comes back to step `1`
# the order would be [3, 2], i add `1` to the end
# so i'd pick 3 and repeat the process..
# but by the time it comes back 
# it would return with [1, 2]
# in which case, i'd add `3` to the end, [1, 2, 3]
# then pick `1`

# i'm right back where i started, this wouldn't work
# you want to maintain the order... as you iterate through
# a linked list would've worked best.

# a linked list is messy, how about we just slice the array
# probably less efficient but less messy, after we can then use a linked list.

# okay, let's do it.

# error, i didn't pop the added element on return from exploration

# TODO, this works but could be better..
# https://www.youtube.com/watch?v=FZe0UqISmUw
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        self.res = []
        trackingArr = []
        
        self.explore(nums, trackingArr)
        return self.res
    
    def explore(self, nums, trackingArr):
        if not nums:
            self.res.append(trackingArr[::])
            return
        
        dim = len(nums)
        for idx in range(dim):
            currentPick = nums[idx]
            trackingArr.append(currentPick)
            newSlice = nums[:idx] + nums[idx+1:]
            self.explore(
                newSlice,
                trackingArr    
            )
            trackingArr.pop()
            
arr = [
    [1, 2, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.permute(foo)
print(res)