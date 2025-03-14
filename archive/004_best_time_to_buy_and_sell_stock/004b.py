class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l, r = 0, 1

        best = 0
        while r < len(prices):
            uno, dos = prices[l], prices[r]

            if dos > uno:
                best = max(best, dos - uno)
            else:
                l = r
            
            r += 1

        return best
    
arr = [
    [7,6,4,3,1],
    [7,1,5,3,6,4],
    [7],
]
foo = arr[-1]

sol = Solution()
res = sol.maxProfit(foo)
print(res)