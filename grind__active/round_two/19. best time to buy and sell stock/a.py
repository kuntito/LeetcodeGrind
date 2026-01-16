# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List

# i'm given an array of integers, `prices`
# each integer represents the stock price on a given day..

# the days are sequential in the array...

# and we want to find out the max profit we can get
# if we can only buy once..

# what comes to mind is iterate through all the prices
# and at each price, you ask the question..
# what's the lowest price i've seen before this..

# the lowest price before guarantees the max profit..
# so i'd also have to track the number max profit as i go along..

# since, that'd change too..

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        maxProfit = 0
        
        for p in prices:
            profit = p - lowestPrice
            maxProfit = max(
                profit,
                maxProfit
            )
            
            lowestPrice = min(
                lowestPrice,
                p
            )
            
        return maxProfit
    
arr = [
    [7,6,4,3,1],
    [7,1,5,3,6,4],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProfit(foo)
print(res)