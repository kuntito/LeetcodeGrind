import heapq

class MedianFinder:
    def __init__(self):
        self.leftSide = []
        self.rightSide = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.leftSide, -1 * num)
        
        self.balanceSides()
        
    def balanceSides(self):
        # there's two rules to balancing.
        # the left side can only be one more than the right side
        # the left side must contain the first half of the distribution.
        
        # which rule should be addressed first?
        # i'd address them separately
        self.balanceDistribution()
        self.balanceSize()
        
    def balanceDistribution(self):
        # we'd only ever need to address the tip of the left side
        # since, we balance on each addition
        # at most, only one number can be out of place
        leftTip = -1 * self.leftSide[0]
        if self.rightSide and leftTip > self.rightSide[0]:
            rightTip = heapq.heappop(self.rightSide)
            heapq.heappush(self.leftSide, -1 * rightTip)
            
    def balanceSize(self):
        while len(self.leftSide) > len(self.rightSide) + 1:
            leftTip = -1 * heapq.heappop(self.leftSide)
            heapq.heappush(self.rightSide, leftTip)

    def findMedian(self) -> float:
        firstNum = -1 * self.leftSide[0]
        
        total = len(self.leftSide) + len(self.rightSide)
        isOdd = total % 2
        
        if isOdd:
            return firstNum
        
        secondNum = self.rightSide[0]
        
        return (firstNum + secondNum)/2
        
            

