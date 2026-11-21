class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        self.grid = grid
        self.dimRows, self.dimCols = len(self.grid), len(self.grid[0])
        
        ri, ci = 0, 0
        zeroUsed = False
        
        return self.explore(ri, ci, zeroUsed)
    
    def explore(self, sRi, sCi):
        row = self.grid[sRi]

        streakStart, streakEnd = 0, 0        
        for ci in range(sCi, self.dimCols):
            val = row[ci]
            
            if val == 1:
                streakStart