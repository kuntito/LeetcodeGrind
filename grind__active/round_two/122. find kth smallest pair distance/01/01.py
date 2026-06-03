from typing import List
import heapq

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        dim = len(nums)
        
        maxHeap = []        
        self.max_size = k
        
        for idx_first in range(dim):
            for idx_second in range(idx_first + 1, dim):                
                first_num = nums[idx_first]
                second_num = nums[idx_second]
                
                distance = abs(first_num - second_num)
                
                self.add_to_heap(distance, maxHeap)
                
        return -1 * maxHeap[0]
                
                
    def add_to_heap(self, new_dist, maxHeap):
        is_full = len(maxHeap) == self.max_size
        
        if is_full and new_dist < (-1 * maxHeap[0]):
            heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, -1 * new_dist)
        elif not is_full:
            heapq.heappush(maxHeap, -1 * new_dist)
        