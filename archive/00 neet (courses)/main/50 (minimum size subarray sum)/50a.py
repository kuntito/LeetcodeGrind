# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        start, temp_sum = 0, 0

        min_len = float("inf")
        for stop, n in enumerate(nums):
            temp_sum += n

            while temp_sum >= target:
                cur_len = (stop - start) + 1
                min_len = min(min_len, cur_len)
                temp_sum -= nums[start]
                start += 1

            stop += 1

        return 0 if min_len == float("inf") else min_len
    
arr = [
    [7, [2,3,1,2,4,3]],
    [4, [1, 4, 4]],
    [11, [1,1,1,1,1,1,1,1]],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.minSubArrayLen(foo, bar)
print(res)