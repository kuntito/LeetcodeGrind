class Solution:
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        self.nums = nums
        self.uniqueCount = k
        
        self.res = []
        for idx, n in enumerate(nums):
            self.explore(idx)
            
        return self.res
    
    
    def explore(self, startIdx):
        hashmap = {}
        chunk = []
        
        dim = len(self.nums)
        for idx in range(startIdx, dim):
            n = self.nums[idx]
            
            hashmap[n] = hashmap.get(n, 0) + 1
            chunk.append(n)
            
            if len(hashmap) == self.uniqueCount:
                self.res.append(
                    chunk[::]
                )
            elif len(hashmap) > self.uniqueCount:
                break

            
arr = [
    [[1, 2, 3], 2],
    [[1, 2, 1, 2, 3], 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.subarraysWithKDistinct(foo, bar)
print(res)