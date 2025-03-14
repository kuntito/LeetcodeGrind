class Solution:
    def rob(self, nums: list[int]) -> int:
        best_sum = [0, 0] + [0 for _ in nums]

        max_sum = 0
        for idx in range(len(nums)):
            n = nums[idx]
            temp_sum = n + best_sum[idx]
            max_sum = max(max_sum, temp_sum)
            best_sum[idx+2] = max_sum

        return best_sum[-1]


nums = [2, 1, 3, 8]
nums = [5, 2, 1, 2]

# nums = [2, 7, 9, 3, 1]

sol = Solution()
res = sol.rob(nums)

print(res)