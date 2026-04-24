# https://leetcode.com/problems/subarrays-with-k-different-integers/

from typing import List


class Solution:
    def subarraysWithKDistinct(
        self,
        nums: List[int],
        k: int
    ) -> int:
        # so, how do i explore every subarray
        # i'd start with the single element subarrays
        # then increment the number of subarray elements by 1
        
        # what do you mean? i'd be running several iterations through `nums`
        # i'd go through every index and pick subarrays.
        
        # the first pass, at each index, i'd pick one integer
        # then assess the subarray
        
        # the next pass, at each index, 
        # i'd pick two consecutive integers starting from each index
        # then assess the subarray
        
        # i'd keep doing this till i hit the subarray with `len(nums)` elements
        # this way, i'd have assessed all the subarrays to see if the meet the criterion.
        
        dim = len(nums)
        
        valid_subarr_count = 0
        for subarr_len in range(1, dim + 1):
            for idx in range(dim):
                endRange = idx + subarr_len
                if endRange > dim:
                    break
                
                subarray = nums[idx: endRange]
                # print(subarray)
                
                if self.is_subarr_meet_condition(subarray, k):
                    valid_subarr_count += 1
                    
        return valid_subarr_count
    
    def is_subarr_meet_condition(self, subarray, k):
        return len(set(subarray)) == k
    
    
arr = [
    [[1, 2, 3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.subarraysWithKDistinct(foo, bar)
print(res)
