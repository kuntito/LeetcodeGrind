from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        imposters = 0
        
        
        dim = len(nums)
        for idx in range(dim):
            smallest = self.getSmallest(idx-1, idx-2, nums)
            if smallest is None: continue
            
            cur = nums[idx]
            if cur < smallest:
                imposters += 1
                                
            if imposters > 1:
                break
            
        return imposters <= 1
    
    
    def getSmallest(self, idx, idxTwo, arr):
        first = arr[idx] if idx >= 0 else None
        second = arr[idxTwo] if idxTwo >= 0 else None
        
        if first is None:
            return second
        
        if second is None:
            return first
        
        return min(first, second)
            
            
    
    
arr = [
    [4, 2, 3],
    [-1,4,2,3],
    [3, 4, 2, 3],
]
foo = arr[-1]
sol = Solution()

res = sol.checkPossibility(foo)
print(res)
