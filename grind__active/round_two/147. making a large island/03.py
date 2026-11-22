class Solution:
    def largestIsland(self, grid: list[list[int]]) -> int:
        seen = set()
        self.cellToMates = {}
        self.grid = grid
        largest = 0
        
        
        foo = self.getCellToMates(seen)
        if foo > largest:
            largest = foo
        
        # print(self.cellToMates)
        
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 1: continue
                
                foo = self.collateSize(ri, ci) + 1 # for the zero
                if foo > largest:
                    largest = foo
                    
        return largest
    
    def collateSize(self, sRi, sCi):
        candidates = [
            (sRi-1, sCi),
            (sRi+1, sCi),
            (sRi, sCi-1),
            (sRi, sCi+1),
        ]
        
        collations = set()
        for ri, ci in candidates:
            if self.is_in_bounds(ri, ci) and self.grid[ri][ci] == 1:
                collations.update(self.cellToMates[(ri, ci)])
                
        return len(collations)
    
    def getCellToMates(self, seen):
        largest = 0
        for ri, row in enumerate(self.grid):
            for ci, val in enumerate(row):
                if val == 1:
                    cellMates = set()
                    self.explore(
                        ri,
                        ci,
                        seen,
                        cellMates
                    )
                    
                    if len(cellMates) > largest:
                        largest = len(cellMates)
                        
        return largest
                    
    def is_in_bounds(self, ri, ci):
        rows, cols = len(self.grid), len(self.grid[0])
        
        return ri >= 0 and ri < rows and ci >= 0 and ci < cols
    
    def explore(self, sRi, sCi, seen, cellMates):
        mitem = (sRi, sCi)
        if mitem in seen or not self.is_in_bounds(sRi, sCi):
            return
        if self.grid[sRi][sCi] == 0:
            return
        
        if mitem not in cellMates:
            self.cellToMates[mitem] = cellMates
            
        cellMates.add(mitem)
        seen.add(mitem)
            
        self.explore(sRi - 1, sCi, seen, cellMates)
        self.explore(sRi + 1, sCi, seen, cellMates)
        self.explore(sRi, sCi - 1, seen, cellMates)
        self.explore(sRi, sCi + 1, seen, cellMates)
        
        
arr = [
    [
        [0,1,0],
        [1,0,1],
        [1,0,0]
    ],
    [[1,1],[1,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.largestIsland(foo)
print(res)