from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.smallestMax = float("inf")
        
        # this is the variable, i compare every chunk sum with
        # it holds the max along each path
        # and is reconciled with `self.smallestMax` at base case
        maxSum = 0
        isFirst = True
        self.explore(nums, k, maxSum, isFirst)
        
        return self.smallestMax
    
    def explore(self, nums, k, maxSumAlongPath, isFirst):
        if k == 1:
            maxSumAlongPath = max(
                maxSumAlongPath,
                sum(nums)
            )
            
            self.smallestMax = min(
                self.smallestMax,
                maxSumAlongPath
            )
            
            return
        
        availSize = len(nums)
        maxChunkSize = availSize - (k - 1)
        
        for sz in range(1, maxChunkSize + 1):
            chunk = nums[:sz]
            chunkSum = sum(chunk)
            
            if isFirst:
                maxSumAlongPath = 0
            
            maxSumAlongPath = max(
                maxSumAlongPath,
                chunkSum
            )
        
            self.explore(
                nums[sz:],
                k-1,
                maxSumAlongPath,
                False
            )
            
arr = [
    [[7, 2, 5, 10, 8], 2],
    # [[1,2,3], 2],
    # [[1, 2, 3, 4, 5], 2]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)