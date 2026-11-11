from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        self.nums = nums
        if self.explore(0, 0):
            return True
        
        if len(nums) > 1 and nums[0] > nums[1]:
            return self.explore(1, 1)
        
        return False
    
    
    def explore(self, startIdx, startingImposters):
        
        impostersFound = startingImposters
        dim = len(self.nums)
        
        lowestSeen = self.nums[startIdx]
        
        for idx in range(startIdx, dim - 1):
            first, second = self.nums[idx], self.nums[idx + 1]
            
            if first > second:
                impostersFound += 1
                
            if second < lowestSeen:
                impostersFound += 1
                
            if impostersFound > 1:
                return False

        return True     
    
    
arr = [
    [3, 4, 2, 3],
    [4, 2, 3],
    [-1,4,2,3]
]
foo = arr[-1]
sol = Solution()

res = sol.checkPossibility(foo)
print(res)
