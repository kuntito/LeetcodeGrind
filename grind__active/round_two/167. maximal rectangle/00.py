class Solution:
    def maximalRectangle(
        self, 
        matrix: list[list[str]]
    ) -> int:
        maxArea = 0
        self.matrix = matrix
            
        
        for ri, row in enumerate(matrix):
            streak = 0
            for ci, dig in enumerate(row):
                if dig == '0':
                    if streak > maxArea:
                        maxArea = streak
                    streak = 0

                    continue

                streak += 1
                if streak > maxArea:
                    maxArea = streak

                maxArea = max(
                    maxArea,
                    self.exploreVertical(ri, ci),
                )

                    
                
                    
                
        return maxArea
        
    
    def exploreVertical(self, startRi, startCi):
        # what are you doing?
        # you want to keep going down,
        # as long as there's a 1.
        # you'd have drawn a column of 1s.
        
        # and after you want to move rightwards.
        # only if the right column of same length
        # only contains 1s.
        
        grid = self.matrix
        rows = len(grid)
        
        maxArea = 0
        
        ri = startRi
        if ri + 1 < rows:
            x = (grid[ri + 1][startCi])
        while ri + 1 < rows and grid[ri + 1][startCi] == '1':
            ri += 1
            
            endRi = ri
            maxArea = max(
                maxArea,
                self.exploreRight(endRi, startRi, grid, startCi),
            )
            
        return maxArea
        
    def exploreRight(self, endRi, startRi, grid, startCi):
        # now, i want to move right wards.
        # and what's the question,
        # i'd move ci forward, and move from startRi to endRi, if i keep getting 1s
        
        cols = len(grid[0])
        ci = startCi
        while ci + 1 < cols and grid[startRi][ci + 1] == '1' and self.isOneCol(ci+1, startRi, endRi, grid):
            ci += 1
          
        endCi = ci
          
        unoRecDim = (endRi - startRi) + 1
        dosRecDim = (endCi - startCi) + 1
        
        return unoRecDim * dosRecDim
    
            
    def isOneCol(self, ci, sRi, eRi, grid):
        for ri in range(sRi, eRi + 1):
            if grid[ri][ci] != '1':
                return False
            
        return True
    
arr = [
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"],
    ],
    [
        ["1","1","1","1","1","1","1","1"],
        ["1","1","1","1","1","1","1","0"],
        ["1","1","1","1","1","1","1","0"],
        ["1","1","1","1","1","0","0","0"],
        ["0","1","1","1","1","0","0","0"]
    ],
    [['1']],
    [['0', '1']],
]
foo = arr[-1]
sol = Solution()
res = sol.maximalRectangle(foo)
print(res)