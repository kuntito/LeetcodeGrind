# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        self.prices = prices
        return self.get_best_profit(0, True, {})
    
    def get_best_profit(self, idx, is_buy, memo):
        if idx >= len(self.prices):
            return 0
        if (idx, is_buy) in memo:
            return memo[(idx, is_buy)]
        
        later = self.get_best_profit(idx + 1, is_buy, memo)
        if is_buy:
            # what's the best i can sell at `idx`
            best_sell = self.get_best_profit(idx + 1, False, memo)
            profit_now = best_sell - self.prices[idx]
            memo[(idx, is_buy)] = max(profit_now, later)
        else:
            # after selling here, what's the best i can buy after cooldown
            best_profit_after_sell = self.get_best_profit(idx + 2, True, memo)
            total_sale = best_profit_after_sell + self.prices[idx]
            memo[(idx, is_buy)] = max(total_sale, later)

        return memo[(idx, is_buy)]





arr = [
    [1,2,3,0,2],
]
foo = arr[-1]
sol = Solution()


res = sol.maxProfit(foo)
print(res)