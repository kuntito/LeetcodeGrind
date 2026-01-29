# https://leetcode.com/problems/merge-sorted-array/

from typing import List

# i'm given two four things.
# two integer arrays and two integers

# one integer array, `nums1` and an integer `m` representing the number of elements in `nums1`
# another integer array, `nums2` and another integer, `n` representing the number of elements in `nums2`

# both arrays, `nums1` and `nums2` are sorted in non-decreasing order.
# they want me to merge them and maintain the non-decreasing order.

# however, they want me to do this in-place in `nums1`
# `nums1` is actually the length of the merged array
# the size of `nums1` is `m + n`

# but only the first `m` slots have values
# the rest are initialized to `0`


# for example
# nums1 = [1, 2, 3, 0, 0, 0]
# m = 3

# nums2 = [2, 5, 6]
# n = 3

# how would you address this?
# i'd say iterate from behind..

# you want to fill up the slots in `nums1`
# unless there's no slots, in which case if `m == len(nums1)`, return `nums1`
# that's just an edge case..

# back to the reverse iteration..
# we basically want to fill missing slots
# and maybe move elements around..

# i'd start at the last element in `nums1`
# which number goes here..

# whichever's largest between the last number in `nums1` and the last number in `nums2`

# [1, 2, 3, 0, 0, 0]
# [2, 5, 6]

# in this case, `nums2` has the larger last number
# what do we do..
# move `6` to the right slot..

# now, we've got this..
# [1, 2, 3, 0, 0, 6]
# [2, 5, _]

# we move to the next available slot, same question:
# who has the bigger last number..

# still `nums2`, we move `5` to the slot..

# now, we've got this..
# [1, 2, 3, 0, 5, 6]
# [2, _, _]

# same question, who's got the larger last number..

# nums1, we move `3` to this slot..
 
# now, we've got this..
# [1, 2, 0, 3, 5, 6]
# [2, _, _]

# same question, who's got the larger last number..
# in this case, they're equal..

# we could move either..
# if we move from `nums1`, we'd have..

# [1, 0, 2, 3, 5, 6]
# [2, _, _]

# and now, we'd have to move `nums2`s last number to the slot..

# if we'd moved `nums2` instead of `nums1`, the iteration would have ended the same way.

# so i have the idea, how do i write the code..
# let's write on the go..

# error, when the larger number is from slot1, i should assign `lastFromOne` to slotIdx
# instead i did this, `nums1[slotIdx] = nums1[lastFromOne]`
# should be `nums1[slotIdx] = lastFromOne`

# error, i didn't handle the case when there's no last number in `nums1`
# if you have a situation like 

# [0, 2]
# [1]

# at this point, `idxOne` is `-1` indicating there are no more elements in `nums1`
# so `nums2`s number automatically gets the slot..

# the fix is to check if `idxOne < 0`
# automatically add `nums2`s last element 

# TODO view the official solution for this.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # i want to iterate from the last slot in `nums1`
        # and work my way inwards, 
        # but first, i must address the edge case.
        
        if m == len(nums1):
            return nums1
        
        # we start at the last vacant slot in `nums1`
        slotIdx = len(nums1) - 1
        
        # next we iterate inwards..
        # what's the condition for iteration..
        # well, while `nums2` still has values is a good one..
        
        idxOne = m - 1
        while nums2:
            # on each iteration, we want to compare the last numbers of both arrays..
            lastFromOne = nums1[idxOne]
            lastFromTwo = nums2[-1]
            
            # if `num2`s value is larger or equal
            # move it to slotIdx
            if idxOne < 0 or lastFromTwo >= lastFromOne:
                nums1[slotIdx] = nums2.pop()
            else:
                nums1[slotIdx] = lastFromOne
                idxOne -= 1
        
            slotIdx -= 1
            
        return nums1
        
arr = [
    [
        [1,2,3,0,0,0],
        3,
        [2, 5, 6],
        3,
    ],
    [
        [2,0],
        1,
        [1],
        1
    ],
]
foo, bar, baz, tard = arr[-1]
sol = Solution()
res = sol.merge(foo, bar, baz, tard)

print(res)
