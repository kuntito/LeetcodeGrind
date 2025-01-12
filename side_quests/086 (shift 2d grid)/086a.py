# https://leetcode.com/problems/shift-2d-grid/description/

class Solution:
    def shiftGrid(self, grid: list[list[int]], k: int) -> list[list[int]]:
        pass
    
        for _ in range(k):
            self.shift(grid)
                
        return grid
    
    def shift(self, grid):
        rows, cols = len(grid), len(grid[0])
        temp = grid[rows-1][cols-1]
        for ri in range(rows):
            for ci in range(cols):
                pass
                val = grid[ri][ci]
                
                grid[ri][ci] = temp
                temp = val
        
        
arr = [
    [[[1,2,3],[4,5,6],[7,8,9]], 1],
    [[[1]], 1],
    [[[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4],
    [[[1,2,3],[4,5,6],[7,8,9]], 9],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.shiftGrid(foo, bar)

for row in res:
    print(row)