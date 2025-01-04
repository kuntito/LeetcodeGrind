# https://leetcode.com/problems/longest-increasing-subsequence/description/

# TODO https://neetcode.io/solutions/longest-increasing-subsequence
# TODO deep neet's implementation
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)