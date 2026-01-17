# https://leetcode.com/problems/last-stone-weight/description/

from typing import List

# i'm given an array of integers where each integer represents the weight of a stone..
# we play a game with the stones, on each turn of the game, we pick the largest two stones
# and smash them together..

# when we do things, one of two things can happen..
# when we smash the stones, i mean..

# one, if the stone weights are equal, we simply move to the next turn of the game..
# however, if they're unequal, we take the absolute difference of said weights, 
# and add this difference back into the array

# to drive the point home, if the two largest stones are 4 and 4
# we move to the next turn of the game, if the next largest stones are 3 and 1
# we take the abs difference , (3-1) = 2
# add two back into the array..

# it's screaming maxHeap, this allows us to track the largest element at any point in time
# the game is played until we run out of stones or there's only one stone left..
# if we run out of stones, return 0
# if only one stone left, return it's weight

# okay, implementation, set up the maxHeap, in Python, only min heaps
# the trick is to store the negated numbers to simulate a max heap
# while a min heap would store [2, 3]
# if we negate the numbers, we'd have the min heap store [-3, -2]
# simulating a maxHeap

# but we'd have to remember to un-negate the numbers when we need them.
# what's the loop..
# while `len(maxHeap) > 1`...
# grab the top two, smash them.. you know the drill..

import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-x for x in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            uno = -1 * heapq.heappop(maxHeap)
            dos = -1 * heapq.heappop(maxHeap)
            
            # think i can summarize the two smashing scenarios..
            # get the abs diff, only add to maxHeap, if greater than `0`
            absDiff = abs(uno - dos)
            if absDiff:
                heapq.heappush(maxHeap, -1 * absDiff)
            
        return -1 * maxHeap[0] if maxHeap else 0