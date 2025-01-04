# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        rows, cols = len(coins), amount + 1

        dp = [[1 if i == 0 else 0 for i in range(cols)] for _ in range(rows)]

        first_coin = coins[0]
        for am in range(cols):
            if first_coin > am: continue

            dp[0][am] = dp[0][am - first_coin]


        for ri in range(1, rows):
            koin = coins[ri]
            for am in range(cols):
                top = dp[ri-1][am]
                
                new_am = am - koin
                if new_am >= 0:
                    top += dp[ri][new_am]

                dp[ri][am] = top

        return dp[-1][-1]
        



arr = [
    [15, [3, 6]],
    [10, [10]],
    [20, [5, 10]],
    [500, [3,5,7,8,9,10,11]],
    [10, [2, 5, 10]],
    [5, [5, 1, 2]],
    [5, [1, 2, 5]],
    [3, [2]],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.change(foo, bar)
print(res)