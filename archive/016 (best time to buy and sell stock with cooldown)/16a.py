# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.best_sell = [0 for _ in prices]

        foo = 0
        len_prices = len(prices)
        for buy_idx in range(len_prices - 1, -1, -1):
            cost = prices[buy_idx]
            for sell_idx in range(buy_idx + 1, len_prices):
                sell_price = prices[sell_idx] - cost
                if sell_price > 0:
                    foo = max(
                        foo, 
                        sell_price + self.explore_best(sell_idx + 2)
                    )
            self.best_sell[buy_idx] = foo

        return self.best_sell[0]


    def explore_best(self, start_idx):
        if start_idx >= len(self.best_sell):
            return 0
        
        return self.best_sell[start_idx]



arr = [
    [1, 2],
    [2,1,4],
    [6,1,6,4,3,0,2],
    [1,2,4,2,5,7,2,4,9,0],
    [6,1,3,2,4,7],
    [1],
    [1,7,2,4],
    [1,2,3,0,2],
]
foo = arr[-1]
sol = Solution()

print(foo)
print([i for i in range(len(foo))])
print("**************************")
res = sol.maxProfit(foo)
print(res)