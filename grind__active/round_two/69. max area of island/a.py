# https://leetcode.com/problems/max-area-of-island/

from typing import List

# i'm given a 2d grid.
# the grid contains 0s and 1s

# within that grid, a group of 1s is considered an island
# if the 1s are connected vertically or horizontally to each other.

# that said, i want to find the island with the largest area.
# i.e. the most 1s.

# the area is the total number of 1s that make up the island.

# and how would this work in code?
# i'd iterate through every cell
# moment i find a `1`, i'd start an exploration

# downward, leftward, and rightward..
# there's no need for upward, since i'm iterating through the grid
# from top to down.

# for each exploration, i'd find all connecting `1`s and count them.
# i'd need a global variable for storing these counts.

# for the exploration, i'd need a set to store seen positions.
# or i could modify the grid, once i explore a cell, convert it's value to `0`
# that's simpler than passing 'round a set.

# the exploration would be recursive.
# each cell returns the total connecting ones it can reach + 1
# the `+1` indicates the cell itself.

# error, i set explored cells to `0` after checking their neighbours
# i did:
# exploreDown
# exploreLeft
# exploreRight, then set current position to `0`

# this would cause a circular exploration cause if you go left, 
# you can still go right.. back where you started
# so setting current position = 0
# should be done before exploring any neighbour

# error, yes, you do need to explore upwards..
# consider
# 1,0,1
# 1,1,1

# you current implementation would have you exploring only
# 1,0,?
# 1,1,1

# because you never go upward, you'd completely miss the that last `1` on the first row.
# your conclusion of needing to go up because you're going top down, doesn't account for this.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.rows, self.cols = len(grid), len(grid[0])
        
        maxArea = 0
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val:
                    maxArea = max(
                        maxArea,
                        self.explore(ri, ci, grid)
                    )
                
        return maxArea
    
    def explore(self, ri, ci, grid):
        if ri < 0 or ri == self.rows or ci < 0 or ci == self.cols:
            return 0
        
        if grid[ri][ci] == 0:
            return 0
        
        grid[ri][ci] = 0
        
        upCount = self.explore(ri - 1, ci, grid)
        downCount = self.explore(ri + 1, ci, grid)
        rightCount = self.explore(ri, ci + 1, grid)
        leftCount = self.explore(ri, ci - 1, grid)
        
        
        return upCount + downCount + rightCount + leftCount + 1

arr = [
    [
        # [0,0,1,0,0,0,0,1,0,0,0,0,0],
        # [0,0,0,0,0,0,0,1,1,1,0,0,0],
        # [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        # [0,0,0,0,0,0,0,1,1,1,0,0,0],
        # [0,0,0,0,0,0,0,1,1,0,0,0,0],
    ],
    [
        [1,0,1,0,0],
        [1,1,1,0,0],
        [0,0,1,0,0],
    ]
]
foo = arr[-1]
sol = Solution()
res = sol.maxAreaOfIsland(foo)
print(res)