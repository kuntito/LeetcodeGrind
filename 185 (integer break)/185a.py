# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        memo = {1: 1}
        self.n = n
        return self.explore(n, memo)

    def explore(self, num, memo):
        if num in memo:
            return memo[num]

        memo[num] = 0 if num == self.n else num
        for i in range(1, num//2 + 1):
            val = self.explore(i, memo) * self.explore(num - i, memo)
            memo[num] = max(memo[num], val)
        return memo[num]
    
