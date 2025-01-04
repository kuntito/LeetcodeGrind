# https://leetcode.com/problems/find-median-from-data-stream/

import heapq

class MedianFinder:
    def __init__(self):
        self.count = 0
        self.median = None
        self.left_pile = []
        self.right_pile = []

    def addNum(self, num: int) -> None:
        if self.median is None:
            self.median = num
        elif num >= self.median:
            heapq.heappush(self.right_pile, num)
            if not self.is_even():
                heapq.heappush(self.left_pile, -self.median)
                self.median = heapq.heappop(self.right_pile)
        else:
            heapq.heappush(self.left_pile, -num)
            if self.is_even():
                heapq.heappush(self.right_pile, self.median)
                self.median = -heapq.heappop(self.left_pile)
            
        self.count += 1


    def findMedian(self) -> float:
        res = self.median
        if self.is_even():
            res += -(self.left_pile[0])
            res = res / 2

        # print(res)
        return res

    def is_even(self):
        return self.count % 2 == 0


sol = MedianFinder()
sol.addNum(-1)
sol.findMedian()
sol.addNum(-2)
sol.findMedian()
sol.addNum(-3)
sol.findMedian()
sol.addNum(-4)
sol.findMedian()
sol.addNum(-5)
sol.findMedian()

# sol = MedianFinder()
# sol.addNum(1)
# sol.addNum(2)
# sol.findMedian()
# sol.addNum(3)
# sol.findMedian()