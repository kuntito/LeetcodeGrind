# https://leetcode.com/problems/find-median-from-data-stream/description/

# what's the situation today?

# i want to implement a class that continuously stores integers
# and readily knows the median of all the integers it's stored.

# it has three methods..
# the constructor, `__init__`
# the method to store integers, `addNum`
# and the method that returns the median, `findMedian`

# the median is defined as the middle number
# when all the integers are sorted.

# i.e. in [1, 2, 3]
# `2` is the median

# note, that if the integers are even lengthed..
# i.e. [1, 2, 3, 4]

# the median becomes the average of the two middle numbers
# (2+3)/2

# i want to solve this using two heaps.
# a min heap and a max heap

# such the median would live at the top of either or both heaps.

# here's how it would go..
# you want to know how many elements have been added..

# the length of both heaps could tell you that
# or a helper method..

# okay..
# if both heaps are empty, place the first element in the min heap

# and second element, this goes into the max heap

# okay, let's draw this out
# i have
# minHeap = [2]
# maxHeap = [5]

# now i want to add `6` where should it go?
# ideally it should go to the max heap but why?

# i didn't fully flesh this idea out..
# the idea is to have both heaps represent the sorted integers.

# the min heap stores the first half
# the max heap stores the second half

# if we have an odd number of integers stored, say three integers.
# the min heap would have two elements and the max heap would have one.

# this is as imbalanced as it gets.

# so how do you maintain the balance.
# let's revisit the example.

# first element, `2`
# goes into the minHeap

# second element, this is where it gets tricky..
# what do you want to do..

# you want to know where this fits..
# the simple question would be 
# is current element less than the top of maxHeap..

# if yes, this element should be in the min heap.
# if no, this element should be in the max heap.

# in our case, the max heap is empty.. so we put the second element in this heap.

# our heaps now look like this.
# minHeap = [2]
# maxHeap = [5]

# now, we want to add `6`
# we ask the same question is `6` less than the top of maxHeap
# no, so `6` should be in the max heap.

# minHeap = [2]
# maxHeap = [6, 5]

# but now we have an imbalance..
# how do we address it?

# i want to move `5` to the minHeap..
# perhaps, i should proactively check, is adding to the maxHeap going to cause an imbalance.

# if yes, do what?
# move the smallest number in the max heap to the min heap?
# but how do you get the smallest number in the max heap to begin with?

# in our case, there's only one number in the max heap, `5`
# but in another case, you wouldn't have access to this number.

# only the highest number in the max heap..
# perhaps, i don't need a max heap.

# i need two min heaps..
# think about it

# minHeapOne = [2]
# minHeapTwo = [5]

# the addition logic remains the same..
# i want to add `6`, is `6` less than the top of `minHeapTwo`
# no, so i add `6` to minHeapTwo

# now, i have:
# minHeapOne = [2]
# minHeapTwo = [5, 6]

# imbalance exists.. so i simply remove the top of minHeapTwo and add to minHeapOne

# minHeapOne = [2, 5]
# minHeapTwo = [6]

# and what if i want to add `4`

# same logic, is `4` less than the top of minHeapTwo
# yes, this time we add `4` to minHeapOne

# minHeapOne = [2, 4, 5]
# minHeapTwo = [6]

# imbalance exists, minHeapOne is only allowed to have one element
# more than minHeap two..

# so how would this work..
# i want to remove the biggest element from minHeapOne.

# but i don't have access to the biggest element from minHeapOne.

# another pivot, i want a maxHeap and a minHeap
# but the maxHeap stores the first half of the integers
# the minHeap stores the second half..

# going back here..
# maxHeap = [2]
# minHeap = [5]

# to add 6, you check, is it less than the top of the minHeap
# no, add it to min Heap

# maxHeap = [2]
# minHeap = [5, 6]

# imbalance exists.. pop from minHeap, add to max heap
# now you have

# maxHeap = [5, 2]
# minHeap = [6]

# now, i want to add `4`
# where would this go?

# is it less than the top of minHeap? yes, so it goes in max heap

# maxHeap = [5, 4, 2]
# minHeap = [6]

# imbalance exists, remove the top of `maxHeap`
# add to `minHeap`

# now, we have:
# maxHeap = [4, 2]
# minHeap = [5, 6]

# this way we can always maintain the balance..
# if we have odd number of integers stored..
# the top of maxHeap is our median

# else, sum the top of both heaps, divide by two, you have your median.
# got it.

# Python doesn't have max heaps, how are you storing these?
# negative integers..

# remember to swap the signs when moving between heaps.

# error, to calculate median for even length, i did integer division `//`
# while the question demanded float where necessary..

# this probably happend cause i stopped thinking towards the end.
# i just wanted to get it done.

# TODO error,
# your logic fails to grab the right median
# when you add -1, -2 and -3 in succession.
# the median should be `-2`, the code returns `-1`
# find out why.


# TODO Follow up:

# If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
# If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

import heapq

class MedianFinder:

    def __init__(self):
        self.leftMaxHeap = []
        self.rightMinHeap = []

    def addNum(self, num: int) -> None:
        topLeft = -1 * self.leftMaxHeap[0] if self.leftMaxHeap else None
        topRight = self.rightMinHeap[0] if self.rightMinHeap else None
        
        if topLeft is None:
            heapq.heappush(
                self.leftMaxHeap,
                -1 * num
            )
        elif topRight is None:
            heapq.heappush(
                self.rightMinHeap,
                num
            )
        elif num < self.rightMinHeap[0]:
            heapq.heappush(
                self.leftMaxHeap,
                -1 * num
            )
        else:
            heapq.heappush(
                self.rightMinHeap,
                num
            )
            
        self.balanceHeaps()
        
    def balanceHeaps(self):
        dimLeft = len(self.leftMaxHeap)
        dimRight = len(self.rightMinHeap)
        
        # this one a bit tricky..
        # if the right heap has more items than the left
        # offload the top of right heap to left heap
        if dimRight > dimLeft:
            topRight = heapq.heappop(self.rightMinHeap)
            
            heapq.heappush(
                self.leftMaxHeap,
                -1 * topRight
            )
        elif dimLeft == (dimRight + 2):
            # if left heap has two elements more than right
            # offload the top of left heap to right heap
            topLeft = -1 * heapq.heappop(self.leftMaxHeap)
            
            heapq.heappush(
                self.rightMinHeap,
                topLeft
            )

    def findMedian(self) -> float:
        dimLeft = len(self.leftMaxHeap)
        dimRight = len(self.rightMinHeap)
        
        topLeft = -1 * self.leftMaxHeap[0]
        if dimLeft > dimRight:
            return topLeft
        
        topRight = self.rightMinHeap[0]
        
        return (topLeft + topRight)/2

sol = MedianFinder()
sol.addNum(-1)
sol.findMedian()
sol.addNum(-2)
sol.findMedian()
sol.addNum(-3)
print(sol.findMedian())
# sol.addNum(-4)
# sol.findMedian()
# sol.addNum(-5)
# sol.findMedian()