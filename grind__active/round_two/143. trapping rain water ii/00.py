from typing import List


class Solution:
    def trapRainWater(
        self,
        heightMap: List[List[int]]
    ) -> int:
        self.grid = heightMap
        
        totalWaterStored = 0
        for ri, row in enumerate(heightMap):
            for ci, square in enumerate(row):
                waterStored = self.checkWaterStored(ri, ci)
                totalWaterStored += waterStored
                
        return totalWaterStored
    
    
    def checkWaterStored(self, ri, ci):        
        leftSquare = self.getSquare(ri, ci - 1)
        rightSquare = self.getSquare(ri, ci + 1)
        downSquare = self.getSquare(ri - 1, ci)
        upSquare = self.getSquare(ri + 1, ci)
        
        surroundingSquares = (leftSquare, rightSquare, downSquare, upSquare)
        
        if all(x is not None for x in surroundingSquares):
            smallestSurroundingSquare = min(surroundingSquares)
            middleSquare = self.getSquare(ri, ci)
            
            if middleSquare < smallestSurroundingSquare:
                return smallestSurroundingSquare - middleSquare
            
        return 0
    
    
    def getSquare(self, ri, ci):
        rows, cols = len(self.grid), len(self.grid[0])
        
        if ri < 0 or ri == rows or ci < 0 or ci == cols:
            return None
        
        return self.grid[ri][ci]