# https://leetcode.com/problems/design-hit-counter/description/

# what is the question? we want to implement a class called `HitCounter`

# the class tracks hits, would these be website hits, database queries, does it even matter? we know the class takes hits
# and knows the time at which the hit was taken


# we are to implement two methods, `hit` and `getHits`
# `hit` takes one integer argument, `timestamp` which indicates that a hit was made at said time

# multiple hits can occur at the same time but the hits are bound to occur in chronological order, that is, the timestamps would be monotonically increasing

# `getHits` wants to know the amount of hits in the last five minutes
# to do this, we'd need a way to track hits in the order they arrive
# and want to know how many hits in the last five minutes

# if we know the current timestamp
# we can calulate the timestamp, five minutes ago
# by subtracting 300 seconds
# since the timestamps are in seconds granularity (this means the seconds are whole numbers)

# since ...
# we can store unique timestamps in an array
# then use a hashmap to store the number of hits at a particular timestamp

# this way, once we obtain the starting point of the last five minutes
# we can use binary search on the arry to find the insertion point
# then sum up all the hits from that point onwards

# this process can be optimized using a prefix sum too
# let's do the basics first then apply prefix sum

from collections import defaultdict


class HitCounter:

    def __init__(self):
        # for the unique hits
        self.arr = []
        self.counter = defaultdict(int)

    def hit(self, timestamp: int) -> None:
        if not self.arr or timestamp != self.arr[-1]:
            self.arr.append(timestamp)
            
        self.counter[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        fiveMinsInSeconds = 300
        startPoint = (timestamp - fiveMinsInSeconds) + 1
        
        insertionPoint = self.getInsertionPoint(startPoint)
        
        total = 0
        for idx in range(insertionPoint, len(self.arr)):
            ts = self.arr[idx]
            total += self.counter[ts]
            
        print(total)
        return total
    
    def getInsertionPoint(self, target):
        left, right = 0, len(self.arr) - 1
        
        while left <= right:
            idx = (left + right)//2
            value = self.arr[idx]
            
            if target == value:
                return idx
            elif target > value:
                left = idx + 1
            else:
                right = idx - 1
                
        return left
    

sol = HitCounter()
sol.hit(1)
sol.hit(2)
sol.hit(3)
sol.getHits(4)
sol.hit(300)
sol.getHits(300)
sol.getHits(301)