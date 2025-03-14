# https://leetcode.com/problems/house-robber/description/

class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) <= 2: return max(nums)

        best_sum = [0 for _ in nums]
        best_sum[0] = nums[0]
        best_sum[1] = max(nums[0], nums[1])

        max_sum = best_sum[1]
        for idx in range(2, len(nums)):
            n = nums[idx]
            temp_sum = n + best_sum[idx-2]
            max_sum = max(max_sum, temp_sum)
            best_sum[idx] = max_sum

        return best_sum[-1]


nums = [2, 1, 3, 8]
# nums = [2, 7, 9, 3, 1]

sol = Solution()
res = sol.rob(nums)

print(res)