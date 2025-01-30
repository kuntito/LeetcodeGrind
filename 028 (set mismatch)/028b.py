# https://leetcode.com/problems/set-mismatch/description/
from collections import Counter

# TODO https://www.youtube.com/watch?v=d-ulaeRBA64
# 04:17
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num_map = Counter(nums)

        res = []
        for n in range(1, len(nums) + 1):
            if num_map[n] == 2 or num_map[n] == 0:
                res.append(n)

        return res
            
    
arr = [
    [1,2,2,4],
    [2, 2], # TODO res should be `[2, 1]`
]
foo = arr[-1]
sol = Solution()
res = sol.findErrorNums(foo)
print(res)