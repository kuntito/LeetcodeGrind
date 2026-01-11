# https://leetcode.com/problems/moving-average-from-data-stream/description/

import heapq
class MovingAverage:
    def __init__(self, size: int):
        pass
        self.minHeap = []
        self.idx = 0
        self.total = None
        self.maxCap = size
        # we need to track the elements that have been added
        # their total sum and the count
        
        # when we reach max capacity
        # we remove the first element added
        # and add the new one
        
        # how do we remove the first element in O(1)?
        # heap based on latest index
        # have a variable, `idx`
        # that inputs elements into a heap of size `size`
        # once the heap is full we remove the element at the top of the heap

    def next(self, val: int) -> float:
        self.idx += 1
        
        if len(self.minHeap) == self.maxCap:
            topMost = heapq.heappop(self.minHeap)
            self.total -= topMost[1]
            
        if self.total is None:
            self.total = sum(self.minHeap)
            
        heapq.heappush(self.minHeap, (self.idx, val))
        self.total += val
        
        return self.total / len(self.minHeap)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)