# https://leetcode.com/problems/set-mismatch/description/
from collections import Counter


class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        num_map = Counter(nums)

        duplicate, omit = None, None
        for n in range(1, len(nums) + 1):
            if num_map[n] == 2:
                duplicate = n
            if num_map[n] == 0:
                omit = n

        return [duplicate, omit]
            
    
arr = [
    [1,2,2,4],
    [2, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.findErrorNums(foo)
print(res)