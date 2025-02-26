# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# TODO look at answer
# https://neetcode.io/solutions/best-time-to-buy-and-sell-stock-ii
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
            cost_price = prices[start_idx]
            
            # `foo` is the maximum you can get if you sell from `startIdx` onwards
            maxSell = self.explore(cost_price, start_idx, False, prices, memo)
            memo[mi] = maxSell
            return memo[mi]
        

        maxProfit = 0
        if not is_buying:
            for idx in range(start_idx, dim):
                sell_price = prices[idx]
                if sell_price < cost_price: continue
                
                # you sold here
                profitSoFar = sell_price - cost_price
                
                # now, exploring what happens if you buy at the next index
                profitSoFar += self.explore(0, idx + 1, True, prices, memo)
                
                maxProfit = max(
                    maxProfit,
                    profitSoFar
                )
                
        memo[mi] = maxProfit
        return memo[mi]
                
        
        
arr = [
    [1, 2, 3],
    [2, 1, 5],
    [7,6,4,3,1],
    [7,1,5,3,6,4],
    [1,2,3,4,5],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProfit(foo)
print(res)