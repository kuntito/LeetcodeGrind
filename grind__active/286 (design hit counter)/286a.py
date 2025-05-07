# https://leetcode.com/problems/design-hit-counter/description/

# what is the class meant to do, it counts the number of hits received in the past 5 minutes

# what does in seconds granularity mean? it means whole seconds
# so the class should be designed such that it can be hit
# and it knows the number of hits received in the last 5 minutes

# how can we know the number of hits received in the last five minutes
# well, we know the time stamp is always increasing, so the latest timestamp - 5 minutes is the range of hits, we're interested in

# what if we track the timestamps in increasing order, a minHeap that knows the smallest timestamps in order, we also need to know the latest timestamp

# so to obtain the hits within the last five minutes, we determine the lower boundary
# any timestamp with a hit less than lower boundary should be removed from the `minHeap`

# the length of the minHeap would represent the number of hits in the last five minutes
# so what are we storing in the heap
# a timestamp? we're told several hits may happen at the same timestamp, does this affect the function?

# not really, since the heap handles the sorting

import heapq
class HitCounter:

    def __init__(self):
        self.minHeap = []
        self.latest = None
        

    def hit(self, timestamp: int) -> None:
        self.latest = timestamp
        heapq.heappush(self.minHeap, timestamp)

    def getHits(self, timestamp: int) -> int:
        if not self.minHeap:
            return 0
        
        lowerBoundary = self.latest - 300
        # any hit lower than `lowerBoundary` should be removed
        while self.minHeap and self.minHeap[0] < lowerBoundary:
            heapq.heappop(self.minHeap)
            
        return len(self.minHeap)
    
    # i have misunderstood the question, yet again
    # you want to know the number of hits from `timestamp -> timestamp-300`
    
    # i need a way to track the timestamp hits in chronological order
    # the timestamps already come in chronological order so that shouldn't be an issue
    
    # the issue is how you're storing the hits
    # for starters, multiple hits can occur at the same timestamp
    
    # i'm thinking we use an array to store the based on timestamp
    # the array stores (timestamp, numberOfHits)
    
    # so if we want to get hits within 5 minutes
    # we can use binary search to find the lower boundary
    # sum up all the hits from that point to the upper boundary
    
    # to further optimize things, we could use a prefix array
    # since we know the hits are in chronological order, once we're done with a timestamp, we never have to access it again...