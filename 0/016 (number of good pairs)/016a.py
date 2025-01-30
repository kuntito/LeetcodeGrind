# https://leetcode.com/problems/number-of-good-pairs/description/

import math
class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        num_map = {}
        for idx, n in enumerate(nums):
            if n not in num_map:
                num_map[n] = []
            
            num_map[n].append(idx)
    
        # print(num_map)

        res = 0
        for indices in num_map.values():
            res += math.comb(len(indices), 2)
        
        return res
    
    
arr = [
    [1,2,3,1,1,3],
    [1,1,1,1],
    [1,2,3],
]
foo = arr[-1]
sol = Solution()
res = sol.numIdenticalPairs(foo)
print(res)

