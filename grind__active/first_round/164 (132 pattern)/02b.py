class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        shortestAfter = self.getShortestAfter(nums)
        tallestAfter = self.getTallestAfter(nums)
        
        
        for idx, n in enumerate(nums):
            firstGuy = n
            idxTallestGuyAfter = tallestAfter[idx]
            if idxTallestGuyAfter is None: continue
            
            tallestGuyAfter = nums[idxTallestGuyAfter]            
            if tallestGuyAfter <= firstGuy: continue
            
            # now, at this point, we must have a short guy and a taller guy
            # now we need the .. nah, i'm bsing. 
            
            # even if i know the tallest guys index.
            # i don't know if someone after is taller than someone before.
            # 💀
            
            
        
        return False
    
    def getShortestAfter(self, arr):
        shortestAfter = [None for _ in arr]
        
        sidx = None
        dim = len(arr)
        
        for idx in range(dim - 1, -1, -1):
            shortestAfter.append(sidx)
            
            num = arr[idx]
            
            if sidx is None or num < arr[sidx]:
                sidx = idx
                
        return shortestAfter
    
    def getTallestAfter(self, arr):
        tallestAfter = [None for _ in arr]
        
        tidx = None
        dim = len(arr)
        
        for idx in range(dim-1, -1, -1):
            tallestAfter.append(tidx)
            
            num = arr[idx]
            
            if tidx is None or num > arr[tidx]:
                tidx = idx
                
        return tallestAfter
            
            
            
    
arr = [
    [3,1,4,2],
    [1, 2, 3, 4],
]
sol = Solution()
foo = arr[-1]
res = sol.find132pattern(foo)
print(res)