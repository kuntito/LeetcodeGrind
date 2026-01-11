# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/description/

from typing import List

# i want to implement a function that returns an integer.
# this function is called, `maxProfit`, and takes two arguments
# an integer, k, and a list of integers, `prices`

# each element of `prices` represents the stock price for a given day.
# we're not told what stock it is because it's irrelevant, i guess?.

# find the maximum profit you can achieve if you can only complete at most `k` transactions.

# we must sell the stock before we buy again.
# we can't buy or sell simultaneously.

# how do i approach this? off the dome, i'd say explore every possibility.
# i'd buy at every price and explore the next price where i can make a profit.

# all the while tracking how many transactions i've made and how much profit i've made
# i'd keep a global variable, `mostProfit` that keeps track of the most profit i've made
# and return that.

# there'd possibly be some repeated work so memoization should be useful.
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        pass
    
        # first off, i'd declare the global variable
        self.mostProfit = 0
        
        self.prices = prices
        self.maxTransactions = k
        
        # then i want to buy at each price
        for idx, costPrice in enumerate(prices):
            # so i'm buying here
            # and want to explore the next index where i can make a profit
            # i'd use a function, possibly recursive, i need to know
            # the costPrice
            # the next index to start from
            # i need to access `prices`, i could make this global so the function is lean
            
            # what else would i need?
            # the number of transactions made
            # at this point, `0`
            # a transaction is only made after i've sold the stock
            # anything else? let's start and see what happens
            
            self.explore(costPrice, idx + 1, True, 0, 0)
            
    def explore(self, costPrice, startIdx, isSelling, profitSoFar, transactionsMade):
        pass
        # what would be the base case?
        # if the starting index goes out of bounds
        
        # what happens then, we compare the profit so far against the 
        # max profit seen, and make any necessary updates
        
        # that said, i need to pass profitSoFar as an argument
        
        # also, another base case is if we've made `k` transactions
        # and we're currently buying
        
        # how do we know if we're buying or selling, i think a boolean would suffice
        # another argument, `isSelling`
        if startIdx == len(self.prices) or (not isSelling and transactionsMade == self.maxTransactions):
            if profitSoFar > self.mostProfit:
                self.mostProfit = profitSoFar
            return
        
        # now, we ball
        # we're either buying or selling
        
        # let's tackle selling first
        # if we're selling
        
        # think i should change the boolean to `isSelling` since it's more natural
        # to write, the first instance of the function, i sell not buy
        
        # reet, so if i'm selling, i'd -
        if isSelling:
            pass
        else:
            pass