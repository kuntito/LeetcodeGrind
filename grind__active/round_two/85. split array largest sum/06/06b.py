from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        arrLen = len(nums)
        
        # 0. you create a 2d grid of infinite floats.
        # you add an extra row, and an extra column.
        # not sure, why yet.
        cache = [
            [float("inf")] * (k + 1)
            for _ in range(arrLen + 1)
        ]
        
        cache[arrLen][0] = 0

        # then you run through each split
        # not variations, but each split of a path
        # the first split up till the kth split
        for splitOrder in range(1, k + 1):
            # then ball through the grid in reverse...
            # bottom row first
            for idx in range(arrLen - 1, -1, -1):
                # for each row, what are we doing?
                curSum = 0
                # TODO start here, need to figure out how this works.
                
                for numIdx in range(idx, arrLen - splitOrder + 1):
                    curSum += nums[numIdx]
                    cache[idx][splitOrder] = min(
                        cache[idx][splitOrder], 
                        max(
                            curSum, 
                            cache[numIdx + 1][splitOrder - 1]
                        )
                    )

        return cache[0][k]
    
arr = [
    [[1,2,3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)