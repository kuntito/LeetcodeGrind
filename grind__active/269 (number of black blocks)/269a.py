# https://leetcode.com/problems/number-of-black-blocks/description/

# TODO can i target the black cells individually?
# probably, how about the zero cells
# i think i can math my way into the number of blocks
# the zero blocks would be the count of all the blocks minus the black cell blocks
class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: list[list[int]]) -> list[int]:
        pass
        # create the grid with `m` and `n`
        grid = [[0 for _ in range(n)] for _ in range(m)]
        
        # for row in grid:
        #     print(row)
        # fill in the black coordinates, represent them with `1`s
        for r, c in coordinates:
            grid[r][c] = 1
        # for row in grid:
        #     print(row)
        
        # go through every block, from start row to penultimate row
        # every column from start col to penultimate column
        # this way, every 2x2 block is in bounds
        
        # and count the black squares in it
        # and populate the array accordingly
        
        res = [0 for _ in range(5)]
        
        for ri in range(m-1):
            for ci in range(n-1):
                sq_count = self.count_squares(ri, ci, grid)
                res[sq_count] += 1
                
        return res
                
                
    def count_squares(self, ri, ci, grid):
        positions = (
            (ri, ci),
            (ri, ci + 1),
            (ri + 1, ci),
            (ri + 1, ci + 1),
        )
        
        return sum(grid[r][c] for r, c in positions)
        
            
            
arr = [
    [3, 3, [[0, 0]]],
    [3, 3, [[0,0],[1,1],[0,2]]],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.countBlackBlocks(foo, bar, baz)
print(res)