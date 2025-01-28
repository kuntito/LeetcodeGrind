# https://leetcode.com/problems/non-decreasing-array/description/

class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:
        pass

        # iterate from behind [-1] and [-2], track the trend
        # count how many times the trend breaks
        # if more than once, return False
    
    
arr = [
    [4, 2, 1],
    [3, 4, 2, 3],
    [4, 2, 3],
]
foo = arr[-1]
sol = Solution()
res = sol.checkPossibility(foo)
print(res)