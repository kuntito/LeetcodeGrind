# https://leetcode.com/problems/min-cost-climbing-stairs/

from typing import List

# i want to climb a stair case..
# i can either take one step or two steps at time..

# i'm given an array of numbers called `cost`,
# each index of `cost` represents the step on a staircase..

# for every step you take, you pay a cost, i.e. `cost[i]`

# the ask is,
# what's the minimum cost it'd take to get to the top of the staircase..

# the fact that, at each step i can either take one step of two steps indicates recursion..
# the fact that, from each step, the same thing can happen, means i can memoize..

# way it looks, i'd have to explore every possibility and track the one with the least..
# from the jump, there's only two possibilities..

# is it cheaper to start with one step, or
# is it cheaper to start with two steps..

# and i want to return whichever is less from these guys..

# one point i misread or rather didn't read cause i was so eager to solve it..
# was i can either start climbing from index = 0 or index = 1

# not sure, how this impacts the function..
# what would the recusive call look like..

# one call with one step
# another call with two steps..

# we'd need `curIdx`

# also, from the examples.. the top of the staircase is out of bounds
# say, `cost = [1, 2, 3]`
# the top of the staircase is outside of this..

# hence, if you start at `2`, then, take two steps, you're now at the top..
# and your total cost is `2`

# ..okay, recursive function, `curIdx`, what else..
# each call should return the total cost from that position..

# and how would you get that..
# well, the cost of value at `curIdx` then the cost of whichever recursive path is less..

# and what happens when you go out of bounds..
# well, return `0`

# and memo, yes, memo.

# also, i initially started two recursive base calls
#    pathOne = self.explore(curIdx + 1, cost, memo)
#    pathTwo = self.explore(curIdx + 2, cost, memo)
# to address, the situation when i start from index = 1
# then i realized, one iteration would suffice.. every iteration
# memoizes the leastCost at that index..

# len(cost) >= 2, so all i needed was to return whichever is less
# between memo[0] and memo[1]

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        curIdx = 0
        memo = {}
        
        self.explore(curIdx, cost, memo)
        
        return min(
            memo[0],
            memo[1]
        )
    
    def explore(self, curIdx, cost, memo):
        if curIdx >= len(cost):
            return 0
        
        if curIdx in memo:
            return memo[curIdx]
        
        curCost = cost[curIdx]
        
        pathOne = self.explore(curIdx + 1, cost, memo)
        pathTwo = self.explore(curIdx + 2, cost, memo)
        
        smallestPath = min(
            pathOne,
            pathTwo
        )
        
        leastCostAtCurIdx = curCost + smallestPath
        memo[curIdx] = leastCostAtCurIdx
        
        return memo[curIdx]