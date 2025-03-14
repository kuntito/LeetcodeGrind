# https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        pass
        # each box has 4 sides
        # and loses a side to every neighbour it has
        # find the first position with `1`
        # explore it the cardinal directions (NEWS)
        # for every valid neighbour the box has, deduct `1` from it's side count
        # store visited positions in set
        # each box should retrieve all it's neighbours including visited ones
        # to update the side count
        # but they should be skipped during exploration
        
        start_pos = self.get_first_one(grid)

        return self.explore(start_pos, grid, set())
    
    def explore(self, pos, grid, seen):
        neighbours = self.get_neighbours(pos, grid)
        seen.add(pos)
        count = 4
        for nei in neighbours:
            count -= 1
            if nei in seen:
                continue
            
            count += self.explore(nei, grid, seen)
            
        return count
    
    def get_neighbours(self, pos, grid):
        rows, cols = len(grid), len(grid[0])
        ri, ci = pos
        neighbours = (
            (ri - 1, ci),
            (ri + 1, ci),
            (ri, ci - 1),
            (ri, ci + 1),
        )
        
        return [(r, c) for r, c in neighbours if r >= 0 and r < rows and c >= 0 and c < cols and grid[r][c] == 1]
        
        
    def get_first_one(self, grid):
        for ri, row in enumerate(grid):
            for ci, col in enumerate(row):
                if col == 1:
                    return (ri, ci)