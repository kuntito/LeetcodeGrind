from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        numsLen = len(nums)
        
        # step one.
        # create a 2d grid.
        
        # what does each row represent?
        # it's not clear
        # and each column? it would seem the total number of splits plus one.
        # why plus one?
        # it's not clear.
        
        # so, rows is then what?
        # i'd assume each number in `nums`
        # there's also a plus one, an additional rows.
        
        # so we doing each row representing a number from `nums`
        # and every column representing individual splits?
        # not entirely accurate but it's close...
        
        # each column is set to `float("inf")`, by the way
        cache = [
            [float("inf")] * (k + 1)
            for _ in range(numsLen + 1)
        ]
        
        cache[numsLen][0] = 0

        # okay, so we'd pick the first split.
        for splitOrder in range(1, k + 1):
            # then iterate from the last number in `nums`
            for idx in range(numsLen - 1, -1, -1):
                curSum = 0
                # if you remove the other splits, what room
                # would i, `idx`, have to travel?
                endRange = numsLen - (splitOrder - 1)
                
                for numIdx in range(idx, endRange):
                    curSum += nums[numIdx]
                    
                    cacheItemPos = (
                        numIdx + 1,
                        splitOrder - 1
                    )
                    cacheItemToCheck = cache[numIdx + 1][splitOrder - 1]
                    
                    maxB = max(
                        curSum, 
                        cacheItemToCheck
                    )
                    
                    cache[idx][splitOrder] = min(
                        cache[idx][splitOrder],
                        maxB
                    )

        return cache[0][k]
    
arr = [
    [[1,2,3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)