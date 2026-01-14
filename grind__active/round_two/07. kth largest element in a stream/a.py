# https://leetcode.com/problems/kth-largest-element-in-a-stream/description/

# i want to implement a class that stores integers
# and tracks the kth largest integer it's received.

# how would this work? every new number potentially alters the order of numbers
# how then can we track the kth largest one?

# a heap? how would this help
# i mean we can use a maxHeap to store the integers, and traverse to find the kth largest element

# don't know if it'd be efficient though
# we want to return the kth element every time a new number is added..

# what if you store a minHeap of size `k`
# this way, every new number is compared with the smallest number in the heap, the kth largest element
# if the new number is greater than the kth element
# we pop the kth element from the minHeap
# and add the new number

# any edge cases?
# doesn't look like it, we're guaranteed `k` is at least `len(nums) + 1`
# this approach doesn't work..

# judging whether to add a value by the smallest value in the heap wouldn't work.
# consider the heap with [4, 5, 8]
# and you wanted to add `6`
# actually, it does work

# you'd remove `4` and add `6`
# heapify ensures the smallest element is at the front of the heap
# hence, `[5, 6, 8]`

# right it did work, the problem was the way i wrote the conditionals
# specifically, the conditional to pop from the heap
# i'd only checked to see if the new value is greater than the smallest value
# instead that conditional should've been paired with the array being at capacity
# we only pop when we are at capacity and the new value is greater than the smallest value in the minHeap.

# i used array and minHeap interchangeably

import heapq

class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.minHeap = []
        self.maxElems = k
        
        # first, we'd want to initialize the minHeap with `nums`
        for n in nums:
            self.add(n)

        print(self.minHeap)

    def add(self, val: int) -> int:
        pass
        # here, what are we doing?
        # if len(minHeap) < k? add element
        # else, check if new element is > minHeap[0]
        # if yes, pop from minHeap, add new element
        # else, leave as is..
                
        heapIsUnderCapacity = len(self.minHeap) < self.maxElems        
        newValIsGreaterThanSmallest = val > self.minHeap[0] if self.minHeap else None
        
        if heapIsUnderCapacity or newValIsGreaterThanSmallest:
            if newValIsGreaterThanSmallest and not heapIsUnderCapacity:
                heapq.heappop(self.minHeap)
            
            heapq.heappush(self.minHeap, val)
            
        return self.minHeap[0]
    
arr = [[3, [4, 5, 8, 2]]]
foo, bar = arr[-1]
sol = KthLargest(foo, bar)

print(sol.add(3))
print(sol.add(5))
print(sol.add(10))
print(sol.add(9))
print(sol.add(4))
