# https://leetcode.com/problems/maximum-profit-from-trading-stocks/description/

from typing import List

# `present` and `future` are prices.
# present[i] is the price of the ith item right now
# future[i] is the price of the ith item next year

# given a `budget`, what's the best way to spend it so we maximize profit?

# say we obtain a new structure, a 2d array, `combined`
# [(costPrice, profit), ...]

# now we want to know the elements of `combined` that give the highest profit
# and lowest cost.


# is there a way to combine these?
# TODO memory limit exceeded
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        combined = self.getCostAndProfit(present, future)
        combined.sort(key=lambda x: x[1])

        # now, we have the items sorted increasing of order of
        # cost to Profit ratio
        # now we explore multiple combinations of this
        # starting with the first
        # we can either pick the first combo or the next one
        # it's sounding like a 0-1 knapsack problem

        # we pick the lest costProfit ratio, deduct the cost from the budget
        # and start another recursive call
        # if we run out money, we stop the exploration
        # we can return the greates profit seen

        memo = {}
        return self.explore(0, combined, budget, 0, memo)

    def explore(self, startIdx, combined, budget, initProfit, memo):
        mitem = (startIdx, budget, initProfit)
        if mitem in memo:
            return memo[mitem]

        if startIdx == len(combined):
            return initProfit


        leastItem = combined[startIdx]
        cost, profit = leastItem

        currProfit = initProfit
        if budget >= cost:
            currProfit = max(
                currProfit,
                self.explore(
                    startIdx + 1,
                    combined,
                    budget - cost,
                    currProfit + profit,
                    memo
                )
            )
            
        currProfit = max(
            currProfit,
            self.explore(startIdx + 1, combined, budget, initProfit, memo)
        )
        
        memo[mitem] = currProfit
        return memo[mitem]

    def getCostAndProfit(self, present, future):
        combined = []

        dim = len(present)
        for idx in range(dim):
            currPrice, laterPrice = present[idx], future[idx]

            margin = laterPrice - currPrice
            if margin <= 0:
                continue

            combined.append((currPrice, margin))

        return combined

arr = [
    [[5,4,6,2,3], [8,5,4,3,5], 10],
    [[2,2,5], [3,4,10], 6],
    [[0], [1], 0],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.maximumProfit(foo, bar, baz)
print(res)