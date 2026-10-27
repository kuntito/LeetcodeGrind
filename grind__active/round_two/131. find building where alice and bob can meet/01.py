from typing import List


class Solution:
    def leftmostBuildingQueries(
        self,
        heights: List[int],
        queries: List[List[int]]
    ) -> List[int]:
        self.heights = heights
        res = []
        
        for leftPos, _ in queries:
            meetPoint = self.getMeetPoint(leftPos)
            res.append(meetPoint)
            
        return res
    
    
    def getMeetPoint(self, startPos):
        startHeight = self.heights[startPos]
        dim = len(self.heights)
        
        for pos in range(startPos, dim):
            curHeight = self.heights[pos]
            if curHeight > startHeight:
                return pos
            
        return -1
    
arr = [
    [
        [6,4,8,5,2,7],
        [[0,1],[0,3],[2,4],[3,4],[2,2]]
    ],
]
foo, bar = arr[-1]

sol = Solution()
res = sol.leftmostBuildingQueries(foo, bar)
print(res)