from typing import List

import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pass
        # how do i line them up?
        
        # a min heap?
        # i could try that.
        
        # run through every number from every row
        # store in the min heap
        # store each number in a hashmap too.
        # what's that for?
        # that let's me know what row index the number belongs to.
        
        minHeap = []
        hashMap = {}
        
        for rowIdx, row in enumerate(nums):
            for n in row:
                heapq.heappush(
                    minHeap,
                    n
                )
                
                if n not in hashMap:
                    hashMap[n] = set()
                    
                hashMap[n].add(rowIdx)
        
        
        # now, we have the numbers in a heap
        # pop from the heap, maintaining a sliding window.
        # what shape is this sliding window?
        
        # to be fair, this joint is easier, if it's an array.
        # flatten `nums`
        
        # during the flattening?
        # it would be an O(r x c) for generating the flat.
        # another `nlogn` for sorting
        # then sliding window should be O(n)
        