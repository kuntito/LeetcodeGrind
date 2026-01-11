# https://leetcode.com/problems/number-of-distinct-islands/description/

from collections import defaultdict

# the overarching idea from 297a.py is correct
# but your idea for identifying an island is wrong
# an island is made up of rows and columns

# ideally, it's a grid in itself
# with ones and zeros, now how would you id the grid?
# for starters, how about we simply obtain the cell positions
# the positions with ones

# while parsing the grid, we'd obtain the position in a array, `positions`
# and set the grid[r][c] = 0, to indicate that it's been visited

# once we have the positions for island, we now have to find a way to store it such that
# we can id any island we want

# off the dome, i'd say we reconstruct the grid
# or at least, know it's bounds
# what's the smallest column idx, largest column index
# smallest row idx
# largest row idx

# using this we can form a grid from the positions
# once we have the grid, we can convert it's values into a string
# each row would be a string of 1s and 0s
# a row could be 01100
# then we'd seperate each row with a comma

# and store this in a set, to indicate the islands we've seen
# every island we find after this would go through the same process
# we'd determine it's id and see if it's unique


class Solution:
    def numDistinctIslands(self, grid: list[list[int]]) -> int:
        pass
        # we need a set to store all the island ids
        seen = set()
    
        # to start, we'd traverse through the entire grid
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == 1:
                    positions = []
                    self.explore(ri, ci, grid, positions)
                    islandId = self.getId(positions)
                    print(islandId)
                    seen.add(islandId)
                    
                    
        return len(seen)
    
    def getGridDimensions(self, positions):
        # first we need the bounds
        # smallest rowidx, largest row index
        
        # smallest colidx, largest col index
        smallRi, largeRi = float("inf"), float("-inf")
        smallCi, largeCi = float("inf"), float("-inf")
        
        for ri, ci in positions:
            smallRi = min(smallRi, ri)
            largeRi = max(largeRi, ri)
            
            smallCi = min(smallCi, ci)
            largeCi = max(largeCi, ci)
            
        # print(smallRi, smallCi)
        # print(largeRi, largeCi)
            
        # now we need to return row count, colCount
        rowCount = (largeRi - smallRi) + 1
        # rowOffset, colOffset
        colCount = (largeCi - smallCi) + 1
        
        return rowCount, colCount, smallRi, smallCi
    
    def getId(self, positions):
        
        rows, cols, rwOff, clOff = self.getGridDimensions(positions)
        
        grid = [['0' for _ in range(cols)] for _ in range(rows)]
        
        for rowIdx, colIdx in positions:
            rowIdx -= rwOff
            colIdx -= clOff
            
            grid[rowIdx][colIdx] = '1'
            
            
        # now we need to concatenate each row
        res = []
        for row in grid:
            line = "".join(row)
            res.append(line)
        
        return ",".join(res)
    
    def explore(self, ri, ci, grid, positions):
        rows, cols = len(grid), len(grid[0])
        
        # if the starting row index and col index are out of bounds,
        # return
        if ri < 0 or ri == rows or ci < 0 or ci == cols:
            return

        # if the starting row index and col index are not a `1`
        # return
        if grid[ri][ci] == 0:
            return
        
        pos = (ri, ci)
        # now, we append the current position (ri, ci) to `positions`
        positions.append(pos)
        
        # mark grid position as visited
        grid[ri][ci] = 0
        
        # explore verticals and horizontals
        self.explore(ri - 1, ci, grid, positions)
        self.explore(ri + 1, ci, grid, positions)
        self.explore(ri, ci - 1, grid, positions)
        self.explore(ri, ci + 1, grid, positions)
        
        

arr = [
    [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
    # [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]],
    # [
    #     [1,0,1],
    #     [1,1,1]
    # ],
]
foo = arr[-1]
sol = Solution()
res = sol.numDistinctIslands(foo)
print(res)
