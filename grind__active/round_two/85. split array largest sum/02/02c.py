from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.smallestMax = float("inf")
        self.prefixSum = self.getPrefixSum(nums)
        
        maxSum = 0
        isFirst = True
        
        dim = len(nums)
        self.explore(0, dim, k, maxSum, isFirst)
        
        return self.smallestMax
    
    def getPrefixSum(self, nums):
        prefixSum = []
        
        total = 0
        for n in nums:
            total += n
            prefixSum.append(total)
            
        return prefixSum
    
    
    def getChunkSum(self, startIdx, endIdx):
        endPrefixSum = self.prefixSum[endIdx]
        preStartPrefixSum = self.prefixSum[startIdx - 1] if startIdx > 0 else 0
        
        return endPrefixSum - preStartPrefixSum
    
    
    def explore(self, startIdx, endIdx, k, maxSumAlongPath, isFirst):
        if k == 1:
            chunkSum = self.getChunkSum(startIdx, endIdx)
            maxSumAlongPath = max(
                maxSumAlongPath,
                chunkSum
            )
            
            self.smallestMax = min(
                self.smallestMax,
                maxSumAlongPath
            )
            
            return
        
        availSize = (endIdx - startIdx) + 1
        maxChunkSize = availSize - (k - 1)
        
        for curIdx in range(startIdx, maxChunkSize):
            
            chunkSum = self.getChunkSum(startIdx, curIdx)
            
            if isFirst:
                maxSumAlongPath = 0
            
            maxSumAlongPath = max(
                maxSumAlongPath,
                chunkSum
            )
        
            self.explore(
                curIdx + 1,
                endIdx,
                k-1,
                maxSumAlongPath,
                False
            )
            
arr = [
    [[7, 2, 5, 10, 8], 2],
    # [[1,2,3], 2],
    [[1, 2, 3, 4, 5], 2]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)