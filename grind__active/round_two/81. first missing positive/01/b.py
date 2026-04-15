# https://leetcode.com/problems/first-missing-positive/

from typing import List

# there's a list of integers.
# i want to find the smallest positive integer missing from the list.


# how do i go about this?
# what do i need to know to solve this?

# the question demands i do this in O(n) time and O(1) space.

# O(n) run time suggests i iterate over the list.
# of course, i should but what am i looking for?

# the smallest positive intger missing.
# if i find a number `5` in the list, what does that tell me?
# it tells me `5` is not the number.
# what i'm looking for is either higher than `5` or lower than `5`

# why does higher matter, shouldn't it always be lower?
# well, i should.. check lower first..
# the only time i would need to check higher is if all the lower numbers also exist.

# i.e. the list container, 4, 3, 2, 1
# at that point, i know the smallest missing positive integer must be greater than `5`

# but if we can't track the numbers we've seen..
# how do i go about this?

# one approach from an earlier attempt, maybe an unrelated question..
# but the approach was to use the list as a storage for seen numbers..
# would this be O(1)? yes.

# O(1) means memory usage remains the same even if input grows.

# okay, so what's the concept here?
# i want to map every number to it's index.

# and how does this help?
# there's two classes of numbers:

# numbers that can be mapped to an index, and
# numbers that can't

# if the list is of size `3`
# the only numbers that can map to an index are numbers
# `0`, `1` and `2`

# so what are we doing here..
# once we map all the numbers to their index.

# all the numbers that can't be mapped are removed from the list.
# and what would this mean?

# the list is in one of two states:
# either all indices have elements
# or there's gaps in between elements.

# in the first case, we iterate over every element
# realize there's no gap.
# what that means is
# the next positive integer after the last number in the list
# is what we want.

# that's the smallest positive integer not in the list.
# okay.. i see the point..

# and for the second case, the first gap we find..
# is the smallest positive integer in the list.

# we simply used the indices as a natural sorting order
# and the list as it's own storage.

# it's efficiency in a different form.

# i would've used a set to store positive integers.
# then find the smallest one not in there but this solution is much more elegant.

# okay, how do i place a number at it's index?
# you iterate through every number
# if it's within bounds, it can be placed.
# if not, set that index to `None`

# okay.. and the placement..
# consider
# [1, 0]

# i get to `1`, it's within bounds, where should it go
# index1
# i go to index1 and meet `0`
# what do i do?
# i have to move `0` before i can place `1`
# where should `0` be, index0, i get there and i meet `1`
# this becomes recursive..

# the way it should go is..
# from the first time i learn i need to move `1`
# i should set it's index value to `None`

# this way when i get to index1 and meet 0
# i can move 0 to index0, where `1` was.
# once, i've placed 0

# i can come back to index 1 and place 1
# i continue my iteration...
# this time, i meet 1 at index 1
# it's within bounds but it's also where it needs to be..
# so problem solved.

# then i'd iterate through the array again..
# to find the first missing slot or return the next integer after the last number.

# case closed.

# error, i defined the place fn as `place` but in the main call
# i referred to `placeNum`

# perhaps, i was too excited.

# error,
# since i'm setting numbers to None to indicate absence..
# some calls to `isWithinBounds` take None and throw a type error.

# i should've taken more care when defining the function.
# or defining the overall approach.

# error, i wrote this
# `if n is None or n > 0`
#  to skip the first element in nums

# i didn't think it through but the intention was 
# `0` was either placed or it was None..
# in which case, we don't want to return it as our result..

# so the actual condition should be 
# if idx == 0: continue

# if n == 0: should also work, since at this point, if 0 existed
# it would be at index 0 but `idx == 0` reads better.

# error,
# the implementation breaks when the list is [1]
# after the first iteration, the list rightly becomes [None]

# but the return statement was
# return nums[-1] + 1

# which assumed the last number would always be there...
# it's an edge case really since, the only time we don't have a last number
# and finish iteration would be when the list contained a single element

# our return should be `len(nums)`

# TODO rewrite this.
# another edge case breaks it.

# why did i miss it? how can i avoid it next time?

# [1]
# and [2, 1]

# they seem to be different flavors of the same problem.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        self.isWithinBounds = lambda x: x >= 0 and x < len(nums)
        
        for idx, n in enumerate(nums):
            if idx == n: continue
            
            self.placeNum(idx, n, nums)
            
        for idx, n in enumerate(nums):
            if idx == 0: continue
            if n is None:
                return idx
            
        return len(nums)
    
    # i want to place the curNum at it's own index.
    # to be fair, i think the isWithinBounds check should happen here
    # not in the loop
    def placeNum(self, curIdx, curNum, nums):
        if curNum is None:
            return
        # since, we know we're moving curNum else where..
        # we set it's index value to None..
        
        # we don't always move it..
        # okay, if we move it, we set it to None.
        
        # if we don't move it, setting it to None doesn't harm us.
        # since, we'd end up assigning it to the same index
        
        # in summary, always set it to None
        
        nums[curIdx] = None
        
        if self.isWithinBounds(curNum):
            curNumDestIndex = curNum
            
            existingValue = nums[curNumDestIndex]
            existingValueIndex = curNumDestIndex
            
            self.placeNum(existingValueIndex, existingValue, nums)
            
            nums[curNum] = curNum


        # what if the existing value is not within bounds
        # then we just assign `n` to the index.
        
        # and if it is within bounds, we change the current index of `n` to None
        # then we place the existing value where it belongs
        # then we assign `n` to it's current index.
        
        # this method needs `n`s current index too
        # i should rename `n` to `curNum`
        # and it's index, `curIdx`


arr = [
    [1, 2, 0],
    [1],
]
foo = arr[-1]
sol = Solution()
res = sol.firstMissingPositive(foo)
print(res)