# https://leetcode.com/problems/coin-change/



class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if not amount: return 0
        rows, cols = len(coins), amount + 1

        temp = [0 for _ in range(cols)]

        for ri in range(rows):
            for am in range(cols):
                top = temp[am]

                new_am = am - coins[ri]
                curr = 0
                if new_am == 0:
                    curr = 1
                elif new_am > 0 and temp[new_am]:
                    curr = 1 + temp[new_am]

                if top and curr:
                    temp[am] = min(top, curr)
                else:
                    temp[am] = top or curr

        res = temp[-1]
        return res if res else -1
    

arr = [
    [[83, 186, 408, 419], 6249],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.coinChange(foo, bar)
print(res)
