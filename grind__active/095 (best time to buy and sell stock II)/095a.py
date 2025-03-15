# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# TODO look at the answer
# https://neetcode.io/solutions/best-time-to-buy-and-sell-stock-ii
# 01:58
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        pass
    
        # you can only buy stock if you don't have any
        # explore all possibilities and cache results
        
        # starting from the first price, check it with other prices on further days
        # if the prices are higher, sell and continue the recursion
        
        return self.explore(0, 0, True, prices, {})
    
    # the function returns the maximum you can buy/sell at a specific index
    def explore(self, cost_price, start_idx, is_buying, prices, memo):
        mi = (start_idx, is_buying)
        if mi in memo:
            return memo[mi]
        
        dim = len(prices)
        if start_idx == dim:
            return 0
    
        
        if is_buying:
            maxProfit = 0
            for idx in range(start_idx, dim):
                cost_price = prices[idx]
                foo = self.explore(cost_price, idx + 1, False, prices, memo)
                maxProfit = max(foo, maxProfit)
            
            memo[mi] = maxProfit
            return maxProfit
        
        maxProfit = 0
        if not is_buying:
            pass
            for idx in range(start_idx, dim):
                sell_price = prices[idx]
                profit = sell_price - cost_price
                if profit:
                    profit += self.explore(0, idx + 1, True, prices, memo)
                    
                maxProfit = max(
                    maxProfit,
                    profit
                )
                
        memo[mi] = maxProfit
        return maxProfit
        
        
arr = [
    [1, 2, 3],
    [1,2,3,4,5],
    [7,6,4,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProfit(foo)
print(res)