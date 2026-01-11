# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

# TODO compare with `095b`
# https://neetcode.io/solutions/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        total = 0
        dim = len(prices)
        for idx in range(dim):
            if idx == 0: continue

            curr = prices[idx]
            prev = prices[idx - 1]
            if curr > prev:
                total += curr - prev
        
        return total