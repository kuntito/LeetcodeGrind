# https://leetcode.com/problems/subarray-product-less-than-k/

from typing import List

# want to implement `numSubarrayProductLessThanK`, that's a handful of words though.
# want to implement a function, takes two arguments, `nums` and `k`.
# `nums` is an integer array, `k` is an integer. the function takes these arguments and returns an integer.

# but what happens in between? perhaps, the better question is, what does the return integer represent?

# we want to count the number of subarrays, (a range consecutive indices), where the product of their elements is less than `k`.

# consider,
# [1, 2, 3], where k = 3

# [1] is a subarray with product less than `3`
# [2] is also a subarray
# [1, 2], subarray

# there are 3 subarrays less than k, hence, we return `2`
# but how do we solve this?

# pparently, i've tried the bruteforce and ran out of time.
# there a way to optimize this, one insight is, if i have a valid range
# every sub range within it becomes valid.

# there's probably a math function that'd allow me calculate the number of
# subarrays in a given range.
# in some sense, i want to start an iteration for each element
# find out how far i can go without exceeding `k`
# do the math to figure out how many subarrays and submit.

# might work, let's try it out


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        pass
    
        ranges = []
        for idx, n in enumerate(nums):
            distance = self.howFar(idx, nums, k)
            ranges.append(distance)
            
            
    def howFar(self, startIdx, nums, k):
        # what we want is to track the product
        # first, check that the start number doesn't exceed `k`
        
        # then loop through `nums`, if including the next number would
        # cause `product` to overflow, return `product` as is...???
        # no. we want to count, the number of indices in the range.
        
        # so two variables, `product`, `rangeLen`
        # product = nums[startIdx]
        # if product > k:
        #     return 0
        
        rangeLen = 1
        product = 1

        
        dim = len(nums)
        idx = startIdx - 1
        # i'm trying to be clever here so i avoid the initial return
        # if product initially exceeds `k`, but the original might be the simplest.
        while idx < dim and product * nums[idx + 1]