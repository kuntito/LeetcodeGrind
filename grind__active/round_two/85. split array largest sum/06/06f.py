from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        
        cache = [
            [float("inf")] * (k + 1)
            for _ in range(numsLen)
        ]
        

        for splitsLeft in range(1, k + 1):
            self.populateCache(
                nums,
                splitsLeft,
                cache
            )

        return cache[0][k]

    
    def populateCache(self, nums, splitsLeft, cache):
        numsLen = len(nums)
        
        for curIdx in range(numsLen - 1, -1, -1):
            curSum = 0
            
            endRange = numsLen - (splitsLeft - 1)
            for curNumIdx in range(curIdx, endRange):
                curSum += nums[curNumIdx]
                
                smallestMaxSumAlongRemainingPaths = self.getSmallestMaxAlongAllPaths(
                    curNumIdx + 1,
                    splitsLeft - 1,
                    cache,
                )
                
                maxB = max(
                    curSum, 
                    smallestMaxSumAlongRemainingPaths
                )
                
                cache[curIdx][splitsLeft] = min(
                    cache[curIdx][splitsLeft],
                    maxB
                )
    
    # TODO i get a sense what the cache is doing, i still haven't deeped why
    # it works? rather, why this structure works the way it does?
    # is it the same thing i'm doing while recursing..
    # go through every variation of a particular split sum
    # for each variation, explore all the paths after it
    # conclude on the smallest max and return that?
    def getSmallestMaxAlongAllPaths(self, nextStartIdx, splitsLeft, cache):
        numsLen = len(cache)
        
        # if out of bounds, there's no more paths for smallest max to form
        if nextStartIdx == numsLen:
            return 0
        elif splitsLeft == 0:
            return float("inf")
        else:
            return cache[nextStartIdx][splitsLeft]
    
arr = [
    [[1,2,3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)