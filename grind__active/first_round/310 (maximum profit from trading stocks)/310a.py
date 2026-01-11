# https://leetcode.com/problems/maximum-profit-from-trading-stocks/

from typing import List

# what's the challenge?
# i want to implement a function `maximumProfit`
# it takes three arguments, two integer arrays, `present` and `future`
# and a third integer, `budget`

# the return type is of type `int`

# `present` and `future` are two sides of the same coin
# where `present[i]` represents the current price of the ith stock
# and `future[i]` represents the price of the stock a year into the future

# we can buy each stock at most once, and `budget` is how much we currently have
# we want to find out the most profit we can make

# this question is tagged as medium but.. it seems easier than that
# since we want to maximize profit, we should create another list
# that calculates the profit from each stock. the idea is to pick the most profitable stocks within our budget

# the list is a summary of the most profitable stock, to make sure it's within our budget
# we also need the `costPrice` for each stock.
# each element of this list would contain a tuple of two elements
# (profit, costPrice)

# once we have this, we'd sort this new list in descending order of profit
# now we need to to take `n` stocks such that we maximize our profit
# okay, this might be the tricky part
class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        pass
    
        # let's obtain the combined first, then proceed
        combined = []
        dim = len(future)
        
        for idx in range(dim):
            curr = present[idx]
            later = future[idx]
            
            margin = later - curr
            # we only want the profits so...
            if margin > 0:
                combined.append((margin, curr))
                
        # now that we have the combination, which bit is tricky
        # say we have
        # [(5, 3), (3, 2), (3, 1)]
        
        # if our budget was `3` and we picked the biggest one,
        # we'd have a profit of `5`
        
        # but picking the other two elements is more profitable
        # since we can afford it and the total profit is 3 + 3
        # whihc is `6`
        
        # without thinking too much, i'd try the bruteforce approach
        # where i'd take an item and explore every other combination
        # to see which one works best
        
        # so i'd take a `5` at a cost of `3`
        # if i have change i'd explore the rest of the array, if not
        # i move to the next element
        
        # it's giving traces of dp
        # what if we iterate backwards and find out the most we can buy with this budget
        # let's not complicate this and start from the beginning
        # you've combined the arrays
        
        combined.sort()
        for idx, item in enumerate(combined):
            profit, cost = item
            if cost > budget:
                continue
            
            self.explore(budget, idx)
        
arr = [
    [[5,4,6,2,3], [8,5,4,3,5], 10],
]
foo, bar, baz = arr[-1]
sol = Solution()
sol.maximumProfit(foo, bar, baz)