# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List

# i'm given two things:
# an array of integers, `nums` and an integer `k`

# i'm asked to return the kth largest element in `nums`
# i'm asked to do it without sorting..

# i'm considering using a heap..
# not sure if using a heap counts as sorting, since heaps inherently sort items..

# let's start somewhere.. then optimize..
# how would a heap help you here..

# i'd iterate through `nums`
# maintaining a heap of size `k`

# what kind of heap?
# since we want the kth largest number..
# this is the number.. um.. we talking descending order right..
# so a minHeap.. the kth element would always be on top of the heap..

# okay, but how would you add elements to the heap..
# when would you need to update the heap..

# say k = 2
# minHeap = [3, 4]

# the second largest number is `3`
# but what if i want to add `5` to the heap..
# what happens.. well, adding `5` would mean `3` can no longer be the second largest number
# it's looking like for every number larger..

# let's rewind a bit.. the first `k` elements you add to the heap
# the element on top of the heap would be the kth smallest element..
# however, for any new number you add

# if it's less than element on top of the heap, let's call it, `topMost`
# any new number less than `topMost` should not be in the heap, it doesn't contribute..

# any number equal to `topMost` also doesn't contribute..
# yeah, so.. only numbers greater than `topMost` deserve to be in the heap..
# i believe.. this case is closed..

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        
        for n in nums:
            if len(minHeap) < k or n > minHeap[0]:
                if len(minHeap) == k:
                    heapq.heappop(minHeap)
                
                heapq.heappush(minHeap, n)
                
        return minHeap[0]
    