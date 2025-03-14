# https://leetcode.com/problems/target-sum/description/

class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        return self.explore(0, 0, nums, target, {})
    
    def explore(self, idx, curr, nums, target, memo):
        foo = (idx, curr)
        if foo in memo:
            return memo[foo]
        if idx == len(nums):
            return 1 if curr == target else 0

        n = nums[idx]

        a = self.explore(idx + 1, curr - n, nums, target, memo)
        b = self.explore(idx + 1, curr + n, nums, target, memo)

        memo[foo] = a + b
        return memo[foo]



    
    
arr = [
    [[2, 2, 2], 2],
    [[1], 1],
    [[1, 1, 1, 1, 1], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findTargetSumWays(foo, bar)
print(res)