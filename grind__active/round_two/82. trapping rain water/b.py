# https://leetcode.com/problems/trapping-rain-water/

from typing import List

# follow up from a.py

class Solution:
    def trap(self, height: List[int]) -> int:
        rightMostCache = self.getRightMostCache(height)
        
        leftTallest = 0
        totalSpace = 0
        
        for idx, val in enumerate(height):
            rightTallest = rightMostCache[idx]
            
            smallerOne = min(leftTallest, rightTallest)
            curSpace = smallerOne - val
            
            curSpace = max(0, curSpace)
            
            
            leftTallest = max(leftTallest, val)
            totalSpace += curSpace
            
        return totalSpace
    
    def getRightMostCache(self, height):
        tallest = 0
        rightMostCache = []
        
        dim = len(height)
        for idx in range(dim-1, -1, -1):
            rightMostCache.append(tallest)
            
            val = height[idx]
            tallest = max(val, tallest)
    
        return rightMostCache[::-1]
    

arr = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
]
foo = arr[-1]
sol = Solution()
res = sol.trap(foo)
print(res)
