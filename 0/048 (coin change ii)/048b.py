# https://leetcode.com/problems/coin-change-ii/description/


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        rows, cols = len(coins), amount + 1

        rowAbove = [0 for _ in range(cols)]

        for ri in range(rows):
            c = coins[ri]
            curr = [0 for _ in range(cols)]
            for am in range(cols):
                if am == 0:
                    curr[0] = 1
                    continue

                curr[am] = rowAbove[am]
                if am >= c:
                    curr[am] += curr[am - c]
            rowAbove = curr

        return rowAbove[-1]
                    



arr = [
    [15, [3, 6]],
    [10, [10]],
    [20, [5, 10]],
    [10, [2, 5, 10]],
    [500, [3,5,7,8,9,10,11]],
    [5, [5, 1, 2]],
    [3, [2]],
    [0, [2]],
    [5, [1, 2, 5]],
]
foo, bar = arr[-1]
sol = Solution()

res = sol.change(foo, bar)
print(res)