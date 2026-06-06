from typing import List
import heapq

class Solution:
    def kthSmallestProduct(
        self,
        nums1: List[int],
        nums2: List[int], 
        k: int
    ) -> int:
        self.maxSize = k
        maxHeap = []
        
        for numOne in nums1:
            for numTwo in nums2:
                product = numOne * numTwo
                
                self.addToHeap(maxHeap, product)
                
        return -1 * maxHeap[0]
    
    
    def addToHeap(self, maxHeap, newItem):
        if len(maxHeap) == self.maxSize:
            if newItem < (-1 * maxHeap[0]):
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap, -1*newItem)
        else:
            heapq.heappush(maxHeap, -1*newItem)
        