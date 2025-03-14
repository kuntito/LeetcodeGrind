import heapq

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if not self.left:
            heapq.heappush(self.left, -1 * num)
        else:
            leftmost = -1 * self.left[0]
            if num > leftmost:
                heapq.heappush(self.right, num)
            else:
                heapq.heappush(self.left, -1 * num)
        
        self.maintain_balance()

    def maintain_balance(self):
        left, right = len(self.left), len(self.right)
        while abs(left - right) > 1:
            if left > right:
                heapq.heappush(
                    self.right,
                    -1 * heapq.heappop(self.left)
                )
            else:
                heapq.heappush(
                    self.left,
                    -1 * heapq.heappop(self.right)
                )
            left, right = len(self.left), len(self.right)



    def findMedian(self) -> float:
        left, right = len(self.left), len(self.right)
        if left > right:
            res = -1 * self.left[0]
        elif right > left:
            res = self.right[0]
        else:
            res = (-1 * self.left[0] + self.right[0])/2

        return res
    
    
sol = MedianFinder()
sol.addNum(1)
sol.addNum(2)
print(sol.findMedian())
sol.addNum(3)
print(sol.findMedian())