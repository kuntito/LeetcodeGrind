# https://leetcode.com/problems/maximum-subarray/description/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum = nums[0]
        temp = 0
        
        for n in nums:
            temp = max(temp, 0) + n
            max_sum = max(temp, max_sum)

        return max_sum


arr = [
    [2, 3],
    [5,4,-1,7,8],
    [0, 5, 8, -9, 9, -7, 3, -2],
    [-2,1,-3,4,-1,2,1,-5,4],
]
foo = arr[-1]

sol = Solution()
res = sol.maxSubArray(foo)

print(res)