from typing import List


class Solution:
    def leftmostBuildingQueries(
        self,
        heights: List[int],
        queries: List[List[int]]
    ) -> List[int]:
        self.heights = heights
        res = []
        for q in queries:
            aliceBuildIdx, bobBuildIdx = q
            
            aliceBuildHeight, bobBuildHeight = heights[aliceBuildIdx], heights[bobBuildIdx]
            
            if bobBuildHeight >= aliceBuildHeight:
                res.append(bobBuildIdx) 
            else:
                buildIdx = self.findBuildingIdx(
                    startIdx=bobBuildIdx + 1,
                    minHeight=aliceBuildHeight + 1
                )
                res.append(buildIdx)
                
        return res
                
                
    def findBuildingIdx(self, startIdx, minHeight):
        dim = len(self.heights)
        
        for idx in range(startIdx, dim):
            h = self.heights[idx]
            if h >= minHeight:
                return idx
            
        return -1
    
arr = [
    [
        [6,4,8,5,2,7],
        [[0,1],[0,3],[2,4],[3,4],[2,2]],
    ],
    [
        [5,3,8,2,6,1,4,6],
        [[0,7],[3,5],[5,2],[3,0],[1,6]],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.leftmostBuildingQueries(foo, bar)
print(res)