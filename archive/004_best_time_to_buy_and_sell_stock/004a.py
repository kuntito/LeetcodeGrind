# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        smalls = []
        smallest = prices[0]
        for p in prices:
            smallest = min(smallest, p)
            smalls.append(smallest)


        best = 0
        largest = prices[-1]
        for idx in range(len(prices)-1, -1, -1):
            p = prices[idx]
            largest = max(largest, p)
            best = max(best, largest - smalls[idx])

        return best
    

arr = [
    [7,1,5,3,6,4],
    [7,6,4,3,1],
]
foo = arr[-1]

sol = Solution()
res = sol.maxProfit(foo)
print(res)