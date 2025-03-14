# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        pass
        
        # TODO at each idx, you want to know how far it can travel left before hitting an index with a lower height and how far it can travel right before hitting an index with a lower height
        
        res = 0
        seen = set()
        for idx, h in enumerate(heights):
            # TODO right direction but this is the wrong condition
            
            if h in seen: continue
            seen.add(h)
            
            left_idx = self.get_left(idx, heights)
            right_idx = self.get_right(idx, heights)
            
            currArea = (right_idx - left_idx + 1) * h
            res = max(res, currArea)
            
        return res
    
    def get_left(self, idx, heights):
        targetHeight = heights[idx]
        
        while idx - 1 > -1 and heights[idx - 1] >= targetHeight:
            idx -= 1
            
        return idx
    
    def get_right(self, idx, heights):
        targetHeight = heights[idx]
        
        while idx + 1 < len(heights) and heights[idx + 1] >= targetHeight:
            idx += 1
        
        return idx
        
            
        
arr = [
    [2,1,5,6,2,3],
    [2, 4],
    [2,1,2],
    [4,7,5,1,8,9,4,4,1,3,5,3,7,9,9,1,4],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
        