# https://leetcode.com/problems/largest-rectangle-in-histogram/

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        biggestCliqueSize = 0
        
        dim = len(heights)
        for idx in range(dim):
            # now i want to check from the next index onwards
            # how many items have the same or higher height than
            # the one at `idx`
            mainHeight = heights[idx]
            cliqueMembers = 1
            
            neiIdx = idx
            # move rightwards
            while neiIdx + 1 < dim and heights[neiIdx + 1] >= mainHeight:
                cliqueMembers += 1
                neiIdx += 1
                
            # move leftwards
            neiIdx = idx
            while neiIdx - 1 > -1 and heights[neiIdx - 1] >= mainHeight:
                cliqueMembers += 1
                neiIdx -= 1
                
            cliqueSize = cliqueMembers * mainHeight
            biggestCliqueSize = max(
                biggestCliqueSize,
                cliqueSize,
            )
            
        return biggestCliqueSize
    
arr = [
    [2,4],
    [2,1,5,6,2,3],
    [2,1,2],
]
foo = arr[-1]
sol = Solution()
res = sol.largestRectangleArea(foo)
print(res)
                
            