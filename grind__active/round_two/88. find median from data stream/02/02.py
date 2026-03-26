# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(
            self.maxHeap,
            # Python only has min heap, so negating numbers simulates max heap
            -1 * num 
        )
        
        self.maintainBalance()

    def findMedian(self) -> float:
        # Python only has min heap, so negating numbers simulates max heap
        # when removing number, re-negate to obtain actual number
        tipOne = -1 * self.maxHeap[0]
        
        if len(self.maxHeap) == self.minHeap:
            tipTwo = self.minHeap[0]
            
            return (tipOne + tipTwo) / 2.0
        
        return tipOne

    def maintainBalance(self):
        # what does maintaining balance really look like?
        # it can't just be based on length.
        
        # how so?
        # if maxHeap contains [5]
        # minHeap contains [6]
        
        # and you want to add `8`
        # your assessment says you'd add this to the max heap
        # meaning you'd have [8, 5] then [6]
        # while the distrubution interms of numbers is right.
        
        # it's not the right split you want.
        # you want [6, 5] and [8]
        
        # so how are you really adding new numbers?