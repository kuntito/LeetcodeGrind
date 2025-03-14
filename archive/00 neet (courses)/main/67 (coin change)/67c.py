# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        col_count = amount + 1
        dp = [col_count for _ in range(col_count)]
        dp[0] = 0

        for am in range(1, col_count):
            for c in coins:
                if am >= c:
                    dp[am] = min(
                        dp[am],
                        1 + dp[am - c]
                    )

        last = dp[-1]
        return last if last < col_count else -1

arr = [
    [[2], 3],
    [[83, 186, 408, 419], 6249],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.coinChange(foo, bar)
print(res)
