class Solution:
    def rotateTheBox(
        self,
        boxGrid: list[list[str]]
    ) -> list[list[str]]:
        pass
    
        rows, cols = len(boxGrid), len(boxGrid[0])
        
        rotatedGrid = self.get_rotated_grid(cols, rows)

        
        # the normal grid goes row by row
        # each col per row.
        
        # rotated, how'd it go.
        # the first row becomes the last column.
        # the first row, first cell, becomes the last column, first cell.
        
        # essentially, you go through the normal grid the same.
        # but each row reps the last col downwards.
        # each cell reps the first row down wards.
        
        rot_ci = rows - 1
        for row in boxGrid:
            rot_ri = 0
            for val in row:
                rotatedGrid[rot_ri][rot_ci] = val
                
                rot_ri += 1
            rot_ci -= 1

        
        self.make_it_rain(rotatedGrid)
        
        return rotatedGrid
    
    def make_it_rain(self, grid):
        # how do we make it rain.
        # each stone should drop
        # but what's really happening?
        # the obstacle should have no space
        # from itself and it's stones should have no space.
        
        # if this was horizontal how are you doing it.
        # i'd start at the obstacle and move leftwards.
        # i see a stone, i swap it with the first blank space after the obstacle.
        # continue till i run out of cells.
        
        # well do the same
        # but per column.
        
        # run through the cell
        # at every obstacle run this.
        
        for ri, row in enumerate(grid):
            for ci, val in enumerate(row):
                if val == '#':
                    self.bring_stones(ri, ci, grid)
                    
    def bring_stones(self, start_ri, ci, grid):
        # we're going upwards.
        # scratch that, count all the blank cells and stones from this point upwards.
        # then manually fill the first n with blanks and the rest with cells.
        
        # yeah, it's really not that simple.
        # cause obstacles can exist in the same gap.
        
        # TODO start here..
        # it's easier to think about the algo, if i move the stones horizontally
        # or maybe i'm capping.
        
        # in every streak of gaps and stones.
        # all the gaps should come first.
        # that's the algo.
        
        pass
            
            


    def get_rotated_grid(self, rows, cols):
        grid = []
        
        for _ in range(rows):
            row = []
            for _ in range(cols):
                row.append('')
            grid.append(row)
            
        return grid
            
arr = [
    [
        [1, 2, 3],
        [4, 5, 6],
    ],
]
foo = arr[-1]
sol = Solution()

res = sol.rotateTheBox(foo)

                
