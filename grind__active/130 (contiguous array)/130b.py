# https://leetcode.com/problems/contiguous-array/description/

from typing import List

# what's the problem? we're given an array of numbers and want to return an integer.

# but what does that
# but what would that integer represent?
# first, we'd need to understand the nature of the given array

# the array contains 1s and 0s. only 1s and 0s.
# we want to find the maximum length of a subarray with equal number of 0s and 1s

# for instance,
# [0, 1]
# the entire array is the maximum subarray with equal number
# of 0s and 1s, therefore, our answer is `2`

# the array
# [0, 1, 0], has three elements
# but the longest subarray with equal numbers of zeros
# can either be [0, 1] or [1, 0]
# no more, no less

# therefore, our answer is also `2`

# in that case, how do we solve this question?
# if the first element is `1`, it's definitely not an answer
# since, i need at least two elements to return an answer
# one hint is our answer would be in multiples of `2`

# not sure, how that is useful but okay
# there's no telling where the subarray starts
# so, bruteforce demands i check from the start of every index

# so what am i checking, i'd explore each index to the end
# and track the best subarray length.

# let's implement this, then dive deeper
# i expect a TLE and rightfully so

# what repeated work am i doing here?
# rather, can i optimize this?

# imma jus read the editorial
# https://leetcode.com/problems/contiguous-array/editorial/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        self.bestLen = 0
        for idx, n in enumerate(nums):
            self.exploreLen(idx, nums)
            
        return self.bestLen
    
    def exploreLen(self, startIdx, nums):
        zerosCount = 0
        onesCount = 0

        dim = len(nums)
        for idx in range(startIdx, dim):
            elem = nums[idx]
            if elem:
                onesCount += 1
            else:
                zerosCount += 1
                
            if onesCount == zerosCount:
                self.bestLen = max(
                    self.bestLen,
                    zerosCount + onesCount
                )
                
arr = [
    [0,1,0],
    [0,1],
    [0,1,1,1,1,1,0,0,0],
]
foo = arr[-1]
sol = Solution()
res = sol.findMaxLength(foo)
print(res)