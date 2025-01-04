# https://leetcode.com/problems/missing-number/description/

import math

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        uno = nums[0]

        for n in nums[1:]:
            uno ^= n

        for n in range(len(nums) + 1):
            uno ^= n

        return uno