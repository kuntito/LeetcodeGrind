# https://leetcode.com/problems/candy/

from typing import List

import heapq

# TODO this works but it seems inefficient.
# find out why and rewrite.
class Solution:
    def candy(self, ratings: List[int]) -> int:
        minHeap = []
        
        for idx, rat in enumerate(ratings):
            heapq.heappush(
                minHeap,
                (rat, idx)
            )
            
        candyGiven = [0 for _ in ratings]
        while minHeap:
            rat, idx = heapq.heappop(minHeap)
            
            highestNeiCandy = self.getCandyForHighestRatedNeighbor(
                idx,
                rat,
                candyGiven,
                ratings
            )
            candyGiven[idx] = highestNeiCandy + 1

        return sum(candyGiven)
    
    def getCandyForHighestRatedNeighbor(self, curIdx, curRat, candyGiven, ratings):
        # first, i'd check the left neighbor
        # if it has a lower rating than curRat
        
        highestNeiCandy = 0
        
        leftNeiRat = ratings[curIdx - 1] if curIdx > 0 else None
        if leftNeiRat is not None:
            if leftNeiRat < curRat:
                highestNeiCandy = candyGiven[curIdx - 1]
                
        rightNeiRat = ratings[curIdx + 1] if curIdx + 1 < len(ratings) else None
        if rightNeiRat is not None:
            if rightNeiRat < curRat:
                highestNeiCandy = max(
                    highestNeiCandy,
                    candyGiven[curIdx + 1]
                )
                
        return highestNeiCandy
    
arr = [
    [1, 0, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.candy(foo)
print(res)