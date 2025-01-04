# https://leetcode.com/problems/number-of-1-bits/description/

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        
        return count



items = [
    128,
    11,
]

sol = Solution()

foo = items[-1]
res = sol.hammingWeight(foo)
print(res)
