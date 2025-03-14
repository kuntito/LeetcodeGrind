# https://leetcode.com/problems/coin-change/


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount: return 0
        rows = len(coins)
        cols = amount + 1

        dp = [[0 for _ in range(cols)] for _ in range(rows)]

        first_coin = coins[0]
        for am in range(cols):
            if first_coin > am: continue

            new_am = am - first_coin
            if new_am == 0:
                dp[0][am] = 1
            elif new_am and dp[0][new_am]:
                dp[0][am] = 1 + dp[0][new_am]


        for coin_idx in range(1, rows):
            koin = coins[coin_idx]
            for am in range(cols):
                top = dp[coin_idx-1][am]

                curr = 0
                new_am = am - koin
                if new_am == 0:
                    curr = 1
                elif new_am > 0 and dp[coin_idx][new_am]:
                    curr = 1 + dp[coin_idx][new_am]

                if top and curr:
                    dp[coin_idx][am] = min(top, curr)
                else:
                    dp[coin_idx][am] = top or curr

        for rw in dp:
            print(rw)

        last = dp[-1][-1]
        return last if last else -1


arr = [
    [[83, 186, 408, 419], 6249],
    [[1, 2, 3, 7], 10],
    [[1, 2, 5], 5],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.coinChange(foo, bar)
print(res)

[0, 1, 2, 3, 4, 5]
[0, 1, 1, 2, 2, 3]
[0, 1, 1, 2, 2, 1]
