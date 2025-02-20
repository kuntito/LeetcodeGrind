# https://leetcode.com/problems/n-queens-ii/description/

# TODO how's this different from n queens i?
# TODO rather than increment, can i return the count?
class Solution:
    def totalNQueens(self, n: int) -> int:
        pass
        # to determine this, you want to attempt placing a queen on every
        # column on the first row
        
        # create a set to store positions the queen can reach, `in_range`
        # once you place a queen,
        # start another recursive call to place a queen on the next row
        # the queen can only be placed in a position not `in_range`
        
        # for each recursive call, pass the number of queens left
        # once you hit `0`
        
        # increment self.res by 1
        # on return from each recursive function, remove that cell and it's range cells
        
        # before adding to `in_range`, get a list of the range cells, `range_lst`
        # append to the set, `in_range`
        # when done, iterate through that list
        # and remove from the set
        
        # you need a set for `seen_rows`, `seen_cols`, `seen_fsd`, `seen_bsd`
        
        # TODO rewrite description
        # you don't need to store all the cells
        # only the description of the lines
        # see `get_range_lines`
        
        self.seen_rows = set()
        self.seen_cols = set()
        self.seen_
        
        self.cols = n
        in_range = set()
        self.exploreRow(n, in_range)
        
    def exploreRow(self, row, in_range):
        if self.row == 0:
            self.res += 1
            return
        
        for ci in range(self.cols):
            pos = (row, ci)
            if pos in in_range:
                continue
            
            range_cells = [pos]
            self.get_range_lines(range_cells)
            
            
    def get_range_lines(self, origin, range_cells):
        pass
        # each line can be described by a formula
        # the vertical line is the column
        # the horizontal line is the row
        # the forward slanting diagonal can be described by the sum of the row and column, they are always equal
        # the backward slanting diagonal can be described by `row - col == 0`
        
        # if the origin cell is `00`
        # row `0` is excluded
        # col `0` is excluded
        # 
        