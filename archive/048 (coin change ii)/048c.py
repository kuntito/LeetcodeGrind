# https://leetcode.com/problems/coin-change-ii/description/

class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        rows, cols = len(coins), amount + 1

        arr = [0 for _ in range(cols)]
        arr[0] = 1

        for coin_idx in range(rows):
            coin = coins[coin_idx]
            for am in range(cols):
                if coin <= am:
                    arr[am] += arr[am - coin]

        return arr[-1]



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