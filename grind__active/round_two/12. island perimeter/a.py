# https://leetcode.com/problems/island-perimeter/

from typing import List

# i'm given a grid, `rows x columns`
# an integer grid and the cells are either 0s or 1s

# the 0s represent water
# the 1s represent land..

# i'm told there's only island in the grid..
# the island is a series of connected 1s..

# the 1s are connected vertically or horizontally..
# no diagonals..

# i'm to find the perimeter of that island..
# finding the starting point of the island is simple...

# traverse every cell, till you find the first `1`
# after which start an exploration in each cardinal direction..

# yes, but what am i looking for.. what is perimeter...
# the perimeter is the edge count around the cell,

# if i had a one cell, island, the perimeter would be `four`
# how about a two cell island, well, the cells would share an edge, since they're connected..
# so.. that's two edges, down.. meaning 3-1 + 3-1 = 6 edges..

# how about a three cell island.. well, it depends on how they're connected.
# is it? what i know is, for two cells to be connected they need to share an edge..

# so, if you do.. `total edge count - connected edges`, would you get the answer?
# for the case of `3 cell island`, yes..

# but four cell island is different..
# if the cells all form a cube, you lose `8 edges` { might need to draw this out to confirm }
# if the cells line up, you lose `6 edges`, while it's true to connect two cells, you lose two edges..
# one cell can be connected to two cells, as is the case with the four cube..

# this approach wouldn't work..

# another approach, is to take things as they are..
# explore the entire island.. find the cells at have a boundary with water..
# or they have a boundary with the grid edge..

# in english, each cell has four sides.. we want to find the sides..
# that either touch water or touch the grid edge..

# then what, we can find a way to uniquely identify each edge..
# collate them

# so what do we need,
#     a way to know if the next cell is water or a grid edge, it's giving helper function
#     a way to store visited cells

# NB: it helps to sketch out the grid with a sample island
# a good portion of my intuitions came from staring at the island
# from LC's example

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.visited = set()
        self.grid = grid
        
        start_row, start_col = self.get_start_coordinates()
        
        return self.explore(start_row, start_col)
    
    def get_start_coordinates(self):
        for ri, row in enumerate(self.grid):
            for ci, val in enumerate(row):
                if val:
                    return ri, ci
    
    def explore(self, r, c):
        if self.is_invalid(r, c):
            return 1
        
        mitem = (r, c)
        if mitem in self.visited:
            return 0
        
        self.visited.add(mitem)
        
        # explore in all four directions
        collate = sum([
            self.explore(r - 1, c),
            self.explore(r + 1, c),
            self.explore(r, c - 1),
            self.explore(r, c + 1),
        ])
        
        return collate
        
        
    
    # if a cell is invalid, it means the parent cell is an edge
    def is_invalid(self, r, c):
        rows, cols = len(self.grid), len(self.grid[0])
        
        out_of_bounds = r < 0 or r == rows or c < 0 or c == cols
        
        return out_of_bounds or self.grid[r][c] == 0
    
arr = [
    [
        [0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]
    ],
    [[0,1]]
]
foo = arr[-1]
sol = Solution()
res = sol.islandPerimeter(foo)
print(res)