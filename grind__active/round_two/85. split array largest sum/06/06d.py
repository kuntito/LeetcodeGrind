from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        
        cache = [
            [float("inf")] * (k + 1)
            for _ in range(numsLen + 1)
        ]
        
        cache[numsLen][0] = 0

        for splitsLeft in range(1, k + 1):
            self.populateCache(
                nums,
                splitsLeft,
                cache
            )

        return cache[0][k]

    
    def populateCache(self, nums, splitsLeft, cache):
        numsLen = len(nums)
        
        for idx in range(numsLen - 1, -1, -1):
            curSum = 0
            endRange = numsLen - (splitsLeft - 1)
            
            for numIdx in range(idx, endRange):
                curSum += nums[numIdx]
                
                cacheItemToCheck = cache[numIdx + 1][splitsLeft - 1]
                
                maxB = max(
                    curSum, 
                    cacheItemToCheck
                )
                
                cache[idx][splitsLeft] = min(
                    cache[idx][splitsLeft],
                    maxB
                )
    
arr = [
    [[1,2,3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)