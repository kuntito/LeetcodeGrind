# https://leetcode.com/problems/number-of-islands/

from typing import List


# i'm given a grid containing 0s and 1s..
# the 1s represent land, 0s represent water..

# my job is to return the amount of islands within the grid..
# an island is a series of 1s connected vertically or horizontally

# i.e.
# 1 1
# 1 0
# in this grid, there's only one island

# here's another grid,
# 1 1 0
# 1 0 1
# here, we have two islands.. the 1s do not connect diagonally

# how would you approach this
# iterate through every cell in the grid..

# once you hit a cell with 1, start exploring in the cardinal directions..
# keep going as long as there's a `1` and the cell has not been visited...

# which would mean, tracking the visited cells, that's where a set comes in..
# once done.. update the island count..

# you can actually update the island count before the update..
# since, every 1 part of island..

# every unvisited 1...
# we only explore unvisited positions..

# when done, return the result..

# made an error, i didn't check that val was "0" before skipping cell..
# i explored on every cell
# and even when i corrected it, i used `pos == "0"`
# it should be `val`

# and while exploring, i didn't check the current grid was "0" before skipping
# i checked `grid[r][c] == 0`, i used `0` instead of `"0"`

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        seen = set()
        
        islandCount = 0
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                pos = (ri, ci)
                if pos in seen or val == "0": continue
                
                self.explore(ri, ci, grid, seen)
                
                islandCount += 1
                
        return islandCount
    
    def explore(self, r, c, grid, seen):
        pos = (r, c)
        if pos in seen:
            return
        
        rows, cols = len(grid), len(grid[0])
        if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == "0":
            return
        
        seen.add(pos)
        
        self.explore(r - 1, c, grid, seen)
        self.explore(r + 1, c, grid, seen)
        self.explore(r, c - 1, grid, seen)
        self.explore(r, c + 1, grid, seen)
        
arr = [
    [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.numIslands(foo)
print(res)