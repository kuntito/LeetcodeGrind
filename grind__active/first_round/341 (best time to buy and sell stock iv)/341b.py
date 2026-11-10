class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        self.bestProfit = 0
        self.prices = prices
        
        transactionsLeft = k
        isBuying = True
        profitSoFar = 0
        
        self.explore(0, transactionsLeft, isBuying, profitSoFar)
        
        return self.bestProfit
        
    def explore(self, startIdx, transactionsLeft, isBuying, profitSoFar):
        dim = len(self.prices)
        if transactionsLeft == 0 or startIdx == dim:
            return
        
        stockPrice = self.prices[startIdx]
        if isBuying:
            # buy on the day
            self.explore(startIdx + 1, transactionsLeft, False, profitSoFar - stockPrice)
            
            # buy on the next day
            self.explore(startIdx + 1, transactionsLeft, True, profitSoFar)
        else:
            newProfit = profitSoFar + stockPrice
            if newProfit > self.bestProfit:
                self.bestProfit = newProfit
            
            # sell on the day
            self.explore(startIdx + 1, transactionsLeft - 1, True, newProfit)

            # sell on the next day
            self.explore(startIdx + 1, transactionsLeft, False, profitSoFar)


arr = [
    [
        2,
        [2, 4, 1],
    ],
    [
        2,
        [3,2,6,5,0,3],
    ]
]
foo, bar = arr[-1]
sol = Solution()

res = sol.maxProfit(foo, bar)
print(res)