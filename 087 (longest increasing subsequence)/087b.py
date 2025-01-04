# https://leetcode.com/problems/longest-increasing-subsequence/description/

# TODO https://neetcode.io/solutions/longest-increasing-subsequence
# TODO this has TLE, compare with `087c.py`
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        res = 0
        for idx in range(len(nums)-1, -1, -1):
            res = max(
                res,
                self.explore(idx, nums, {})
            )
        return res
    
        
    def explore(self, start_idx, nums, memo):
        if start_idx in memo:
            return memo[start_idx]
    
        dim = len(nums)
        main = nums[start_idx]
        
        biggest = 0
        for idx in range(start_idx + 1, dim):
            n = nums[idx]
            if n > main:
                biggest = max(
                    self.explore(idx, nums, memo),
                    biggest
                )
        
        memo[start_idx] = 1 + biggest
        return memo[start_idx]