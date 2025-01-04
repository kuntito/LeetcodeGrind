class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        best = 0
        low = prices[0]

        for p in prices:
            low = min(low, p)
            diff = p - low
            best = max(best, diff)


        return best
    
arr = [
    [7,6,4,3,1],
    [7],
    [7,1,5,3,6,4],
]
foo = arr[-1]

sol = Solution()
res = sol.maxProfit(foo)
print(res)