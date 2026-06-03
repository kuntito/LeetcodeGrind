from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        dim = len(nums)
        
        pair_count = 0
        
        for idx_first in range(dim):
            for idx_second in range(idx_first + 1, dim):
                pair_count += 1
                
                if pair_count == k:
                    first_num = nums[idx_first]
                    second_num = nums[idx_second]
                    
                    return abs(first_num - second_num)