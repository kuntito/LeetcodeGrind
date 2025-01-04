# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen_window = set()
        first = 0

        for second, n in enumerate(nums):
            diff = second - first
            if diff > k:
                seen_window.remove(nums[first])
                first += 1
            
            if n in seen_window:
                return True
            
            seen_window.add(n)
        
        return False
            