# https://leetcode.com/problems/split-array-largest-sum/description/

# TODO look at answer https://neetcode.io/solutions/split-array-largest-sum
# what were you trying to do in `191a.py`
class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        pass
        # to bruteforce this, i'd determine a range
        # the smallest chunk and the largest chunk
        # then check each chunk within `nums`
        # tracking the largest sum seen so far
        
        # i could create a prefix sum to speed up the addition
        prefixSum = self.getPrefix(nums)
        # print(prefixSum)
        
        # min chunk size would be `1`
        # to get the max chunk size, assume every other chunk does the minimum size `1`
        # whatever's left is the max chunk size
        # in essence, `dim - k - 1`, `k-1` represents every other chunk
        
        dim = len(nums)
        
        minSize = 1
        maxSize = dim - (k - 1)
        
        self.largest = float("-inf")
        for size in range(minSize, maxSize + 1):
            self.exploreSum(size, nums, prefixSum)
            
        return self.largest
    
    
    def exploreSum(self, size, arr, prefixSum):
        pass
        dim = len(arr)
        startIdx = size - 1
        for idx in range(startIdx, dim):
            previousPrefix = prefixSum[idx - size] if (idx - size) >= 0 else 0
            currPrefix = prefixSum[idx]
            
            chunkSum = currPrefix - previousPrefix
            if chunkSum > self.largest:
                self.largest = chunkSum
                
        
    def getPrefix(self, nums):
        prefixSum = []
        total = 0
        for n in nums:
            total += n
            prefixSum.append(total)
            
        return prefixSum
    
arr = [
    [[7,2,5,10,8], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)