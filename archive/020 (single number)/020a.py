# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        i = 0
        for n in nums:
            i ^= n

        return i

arr = [
    [4, 1, 2, 1, 2],
    [2, 2, 1],
]

foo = arr[-1]
sol = Solution()
res = sol.singleNumber(foo)

print(res)