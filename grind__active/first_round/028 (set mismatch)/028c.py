# https://leetcode.com/problems/set-mismatch/description/

# https://neetcode.io/solutions/set-mismatch
# 07:14
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        dim = len(nums)
        for idx in range(dim):
            n = abs(nums[idx])
            
            n_idx = n - 1
            nums[n_idx] = -nums[n_idx]
            
        print(nums)
    
arr = [
    [1,2,2,4],
    [2, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.findErrorNums(foo)
print(res)