# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        num_map = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in num_map:
                return [num_map[diff], idx]
            num_map[n] = idx        


nums = [2, 7, 11, 15]
target = 9

nums = [3, 2, 4]
target = 6

nums = [3, 3]
target = 6

nums = [-3,4,3,90]
target = 0

sol = Solution()
res = sol.twoSum(nums, target)

print(res)
