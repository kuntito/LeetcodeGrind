from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.arrLen = len(nums)
        self.nums = nums
        
        self.dpCache = [
            [-1] * (k + 1) for _ in range(self.arrLen)
        ]

        return self.dfs(
            0, k
        )

    def dfs(self, startIdx, splitsLeft):
        if startIdx == self.arrLen:
            return 0
        
        if splitsLeft == 0:
            return float("inf")
        
        if self.dpCache[startIdx][splitsLeft] != -1:
            return self.dpCache[startIdx][splitsLeft]

        res = float("inf")
        curSum = 0
        for j in range(startIdx, self.arrLen - splitsLeft + 1):
            curSum += self.nums[j]
            res = min(
                res, 
                max(
                    curSum,
                    self.dfs(
                        j + 1,
                        splitsLeft - 1)
                    )
                )

        self.dpCache[startIdx][splitsLeft] = res
        return res