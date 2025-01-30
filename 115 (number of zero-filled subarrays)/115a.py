# https://leetcode.com/problems/number-of-zero-filled-subarrays/description/

import math
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        pass
        # iterate through the array
        # track the lengths of all consecutive zeros
        
        # declare, `res`
        res = 0
        
        # for each length of consecutive zeros, `val`
        # find how many ways you can select `n` zeros i.e. 1 zero, 2 zeros, ..val zeros from `val`
        
        # val comb 1, val comb 2,  etc
        # and add it to `res`
        
        # memoize the result for each `val`
        # to speed things up
        
        memo = {}
        count = 0
        for n in nums:
            if n == 0:
                count += 1
            else:
                if count:
                    if count not in memo:
                        memo[count] = self.get_combinations(count)
                        
                    res += memo[count]
                    
                count = 0

        if count:
            res += memo[count] if count in memo else self.get_combinations(count)             
                

        return res
    
    def get_combinations(self, count):
        if count == 0: return 0
        
        tmp = 0
        for i in range(1, count + 1):
            item = 1 + count - i
            tmp += item
        return tmp
        
        
arr = [
    [0,0,0,2,0,0],
    [1,3,0,0,2,0,0,4],
    [2,10,2019],
]
foo = arr[-1]

sol = Solution()
res = sol.zeroFilledSubarray(foo)
print(res)        
    