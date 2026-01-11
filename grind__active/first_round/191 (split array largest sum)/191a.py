# https://leetcode.com/problems/split-array-largest-sum/description/

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        pass
        # you want to divide `nums` into `k` separate chunks such that
        # the `targetChunk` has a sum greater than or equal to all the other chunks
        # several `targetChunks` could exist, but we want to return the
        # one with the smallest sum
        
        # i.e. [3, 2, 1], if `k` was `2`
        # we could have target chunks [3], [3, 2], [2, 1] 
        # in this case, the result would either be [3] or [2, 1]
        # since they both have the smallest sums
        
        # if you could split into `k` subarrays
        # how many different sub arrays could you have
        # i'd say define the range for subarrays
        # the minimum subarray is `1`
        # the largest is going to be whatever's left of `dim`
        # after you remove all the other sub arrays
        # we'd assume every other chunk is of size `1`
        # the largest len for a chunk would be whatever's left
        # i.e. dim - (k-1)
        
        # explore all the ranges
        # check if for each range, it's sum is the max sum seen
        # if yes, append to an array, `candidateChunks`
        # return min(candidateChunks)
        
        self.maxChunks = float("inf")
        self.explore(nums, 0, k, [])
        
        return self.maxChunks
    
    def explore(self, nums, currIdx, chunksLeft, maxSoFar):
        if chunksLeft == 1:
            # if at the last chunk, sum up the rest
            chunkSum = sum(nums[currIdx:])
            
            if not maxSoFar or chunkSum > maxSoFar[-1][-1]:
                self.maxChunks = min(
                    self.maxChunks,
                    chunkSum
                )
            else:
                self.maxChunks = min(
                    self.maxChunks,
                    maxSoFar[-1][-1]
                )
            
            return
        
        dim = len(nums)
        # since, we're exploring all possibilites
        # we take 1, take 2, take 3...n
        # but `n` should be minimized such that there are still enough values
        # for the other chunks
        # TODO what's going on here?
        endRange = dim - (chunksLeft - 1)
    
        for idx in range(currIdx, endRange):
            chunk = nums[currIdx: idx + 1]
            chunkSum = sum(chunk)
            
            pos = (currIdx, idx + 1)
            
            if not maxSoFar or chunkSum > maxSoFar[-1][-1]:
                maxSoFar.append((pos, chunkSum))
                
            # grab a chunk from the next position
            self.explore(nums, idx + 1, chunksLeft - 1, maxSoFar)
            
            # print(currIdx, idx, chunkSum)
            while maxSoFar and maxSoFar[-1][0][1] > idx:
                maxSoFar.pop()
    
arr = [
    [[7,2,5,10,8], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)