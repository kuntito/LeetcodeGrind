# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/

from collections import Counter

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        pass
        # create a counter from the shorter array
        # create an empty counter
        # iterate through the longer array
        # update the counter
        # while long_counter[n] <= short_counter[n]
        # res.append(n)
        
        res = []
        
        short, longg = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        
        short_counter = Counter(short)
        long_counter = Counter()
        
        for n in longg:
            if n not in short_counter:
                continue
            
            if long_counter[n] == short_counter[n]:
                continue
            
            
            long_counter[n] = long_counter.get(n, 0) + 1
            if long_counter[n] <= short_counter[n]:
                res.append(n)
        
        return res

    
arr = [
    [[4,9,5], [9,4,9,8,4]],
    [[1,2,2,1], [2,2]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.intersect(foo, bar)
print(res)