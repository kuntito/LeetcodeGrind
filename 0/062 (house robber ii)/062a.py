# https://leetcode.com/problems/house-robber-ii/

class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(
            self.explore(nums[:-1]),
            self.explore(nums[1:])
        )
    
    def explore(self, nums):
        dim = len(nums)

        after, after_after = 0, 0
        for idx in range(dim-1, -1, -1):
            curr = max(
                after,
                nums[idx] + after_after
            )

            after, after_after = curr, after

        return after
        


arr = [
    [2, 3, 2],
    [1, 2, 3, 1],
    [1, 2, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.rob(foo)
print(res)
