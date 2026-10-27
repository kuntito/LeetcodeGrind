from typing import List


class Solution:
    def leftmostBuildingQueries(
        self,
        heights: List[int],
        queries: List[List[int]]
    ) -> List[int]:
        res = []
        self.heights = heights
        
        for leftPos, rightPos in queries:
            meetPoint = self.getMeetPoint(leftPos, rightPos)
            res.append(meetPoint)
            
        return res
    
    def getBiggerHeight(self, unoIdx, dosIdx):
        rightPos = max(unoIdx, dosIdx)
        rightHeight = self.heights[rightPos]
        
        leftDos = min(unoIdx, dosIdx)
        leftHeight = self.heights[leftDos]

        if rightHeight > leftHeight:
            return rightHeight
        else:
            return leftHeight + 1
            
    
    def getMeetPoint(self, leftPos, rightPos):
        if leftPos == rightPos:
            return leftPos 
        
        biggerHeight = self.getBiggerHeight(leftPos, rightPos)
        furtherPosition = max(leftPos, rightPos)
       
        dim = len(self.heights)
        for pos in range(furtherPosition, dim):
            height = self.heights[pos]
            if height >= biggerHeight:
                return pos
           
        return -1
    
arr = [
    [
        [6,4,8,5,2,7],
        [[0,1],[0,3],[2,4],[3,4],[2,2]]
    ],
    [
        [5,3,8,2,6,1,4,6],
        [[0,7],[3,5],[5,2],[3,0],[1,6]],
    ],
    [
        [1,2,1,2,1,2],
        [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[1,0],[1,1],[1,2],[1,3],[1,4],[1,5],[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[3,0],[3,1],[3,2],[3,3],[3,4],[3,5],[4,0],[4,1],[4,2],[4,3],[4,4],[4,5],[5,0],[5,1],[5,2],[5,3],[5,4],[5,5]],
    ]
]
foo, bar = arr[-1]

sol = Solution()
res = sol.leftmostBuildingQueries(foo, bar)
print(res)