# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

from typing import List

# i want to implement a function, `maxProfit`.
# the function takes an integer array and returns an integer.

# the integer array represents a list of stock prices
# each index represents a different day

# my job is to find out the maximum profit a user can achieve if they can complete at most two transactions.

# a transaction is the purchase and sale of a stock
# transaction one must end before transaction two begins.

# how to approach this? i'd say two transactions simplifies things
# for one, i'd explore every starting position, to know the best single transaction

# for each index, i want to know the best single transaction
# for every best single transaction,
# i want to identify the end index of that transaction
# then find the best single transaction after that index

# through all this, i'm tracking the highest total seen so far
# and i'd return that

# to find the best single transaction at a particular index
# i need to know the biggest price that comes after it
# it's giving monotonic stack

# if i reverse-iterate through the integer array, `prices`
# and keep a - what type of array would i need
# i need to know what is the biggest value after the current value

# no, i don't think i need a monotonic anything
# i'd reverse iterate through `prices`, tracking the biggest value seen so far
# i'd store the result in a new array, `biggestAfter`
# where each idx in `biggestAfter` contains the biggest value bigger than `biggestAfter[idx]` or None, if no such value exists


# once i have this, i can get a list of biggest single transactions and their end indices
# using this list, i can then find the biggest single transactions after their end indices
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pass

        bestProfit = self.getBestProfit(prices)
        # print(bestProfit)
        # now, i have the profit at each index and the last index

        bestTransaction = self.getBestTransaction(bestProfit)
        # print(bestTransaction)

        res = 0
        
        for idx, p in enumerate(prices):
            for idxTwo in range(idx+1, len(prices)):
                profitOne = prices[idxTwo] - p
                if profitOne <= 0: continue
                    
                profitTwo = bestTransaction[idxTwo + 1] if idxTwo + 1 < len(prices) else 0
                res = max(res, profitOne + profitTwo)

        return res

    def getBestTransaction(self, bestProfit):
        # how's this different from bestProfit
        # bestProfit tells you the best profit you can make
        # if you buy at a particular index

        # bestTransaction tells you the best transaction in a range
        # bestTransaction[idx] tells you the best transaction
        # possible from `idx to the end of the array`

        res = [0 for _ in bestProfit]

        bestTrans = 0
        dim = len(bestProfit)

        for idx in range(dim - 1, -1, -1):
            if bestProfit[idx] is None:
                res[idx] = bestTrans
                continue

            profit, _ = bestProfit[idx]
            if profit > bestTrans:
                bestTrans = profit

            res[idx] = bestTrans

        return res

    def getBestProfit(self, prices):
        biggestSoFar = [None for _ in prices]

        biggest = (
            float("-inf"),  # biggest price after
            None,  # index of biggest price after
        )

        dim = len(prices)
        for idx in range(dim - 1, -1, -1):
            p = prices[idx]

            if biggest[0] > p:
                profit = biggest[0] - p
                endIdx = biggest[1]
                biggestSoFar[idx] = (profit, endIdx)

            if p > biggest[0]:
                biggest = (p, idx)

        return biggestSoFar


arr = [
    [3, 3, 5, 0, 0, 3, 1, 4],
    [1,2,3,4,5],
    [7,6,4,3,1],
    [3,2,6,5,0,3],
    [6,1,3,2,4,7],
]
foo = arr[-1]
sol = Solution()
res = sol.maxProfit(foo)
print(res)
