class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        dim = len(grid)
        self.grid = grid
        islandMap = self.getIslandMap(grid)
        
        largest = 0
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 0:
                    islandSize = self.collateSurroundings(
                        ri,
                        ci,
                        islandMap,
                    ) + 1
                    if islandSize > largest:
                        largest = islandSize
                    
                    
        if largest == 0:
            return dim * dim
        
        return largest
    
    
    def collateSurroundings(self, sRi, sCi, islandMap):
        candidates = [
            (sRi-1, sCi),
            (sRi+1, sCi),
            (sRi, sCi-1),
            (sRi, sCi+1),
        ]
        
        sizeSurrounding = 0
        seen = set()
        for r, c in candidates:
            if self.isInBounds(r, c):
                idIsland = self.grid[r][c]
                if idIsland in seen: continue
                
                if idIsland in islandMap:
                    sizeSurrounding += islandMap[self.grid[r][c]]
                    seen.add(idIsland)
                
                
        return sizeSurrounding
        
        
    def getIslandMap(self, grid):
        islandMap = {}
        
        idIsland = 2
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 1:
                    islandMap[idIsland] = None
                    sizeIsland = self.explore(ri, ci, idIsland, islandMap)
                    islandMap[idIsland] = sizeIsland
                    
                    idIsland += 1
                    
        return islandMap
    
    
    def isInBounds(self, r, c):
        rows, cols = len(self.grid), len(self.grid[0])
        
        return r >= 0 and r < rows and c >= 0 and c < cols
    
    
    def explore(self, sR, sC, idIsland, islandMap):
        if not self.isInBounds(sR, sC):
            return 0
        
        cellVal = self.grid[sR][sC]
        if cellVal in islandMap or cellVal == 0:
            return 0
        
        self.grid[sR][sC] = idIsland
        
        res = 0
        
        res += self.explore(sR - 1, sC, idIsland, islandMap)
        res += self.explore(sR + 1, sC, idIsland, islandMap)
        res += self.explore(sR, sC - 1, idIsland, islandMap)
        res += self.explore(sR, sC + 1, idIsland, islandMap)
        
        return res + 1
        
arr = [
    [[1,1],[1,1]],
    [
        [0,1,0],
        [1,0,1],
        [1,0,0]
    ],
    [[1,1],[1,0]],
    [
        [0,0,0,0,0,0,0],
        [0,1,1,1,1,0,0],
        [0,1,0,0,1,0,0],
        [1,0,1,0,1,0,0],
        [0,1,0,0,1,0,0],
        [0,1,0,0,1,0,0],
        [0,1,1,1,1,0,0]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.largestIsland(foo)
print(res)