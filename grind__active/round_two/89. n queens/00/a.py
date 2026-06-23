# https://leetcode.com/problems/n-queens/description/

from typing import List

# what's the situation?
# i'm given an integer, `n`

# and what does `n` mean?
# `n` is the dimensions of a chess board.

# `n by n`, okay..
# i want to place `n` queens on this chess board such that the queens are not attacking each other.

# and how would this go?

# consider n is 4
# the chess board is

# . . . .
# . . . .
# . . . .
# . . . .

# you can place queens on this board like this:

# . Q . .
# . . . Q
# Q . . .
# . . Q .

# and they are not attacking each other.
# so what's the question asking..

# it's asking to return all possible board configurations.
# where the queens don't attack each other.

# and what is the return type like..
# a list of strings.
# the size of the list is `n`

# where each string represents each row on the board.
# for our example, the result would be [".Q..", "...Q", "Q...", "..Q."]

# right, and how would the code go?

# for one, i know if a configuration exists
# a queen must be on each row.

# the way it'd work is..
# i'd explore row by row..
# a recursive approach..

# i'd place the queen on each position on the row
# mark the queens reach..

# then go to the next row..
# here, i want to place the queen on a cell that's out of the prior queen's reach

# and keep going until i hit the last row..
# two things here..

# say you do place all the queens.. how do you end the iteration?
# say you hit row 3 of 4, and see there's no more placements..
# what happens?

# for the second scenario.. simply backtrack..
# no harm no foul

# the backtracking would remove each queen from the placed cell
# and remove it's reach from wherever it was tracked.

# for the case where you reach the last cell..
# it's a recursive function..

# what would happen is a base case...
# `we've run out of rows`
# if you get to this point, it means you've placed `n` queens..

# at this point, we store the configuration.

# what variables do we need..
# board, make it global so `self.board`
# `rowIdx`, this allows us grab the current row..

# we initialize the board to strings of '.'
# when we place a queen, replace it with 'Q'

# and how do we track a queens reach?
# global variables..
# `self.reachedRows`, `self.reachedColumns`

# now, Navdeep Singh, let me know each diagonal has an id.

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

# for forward slanting diagonals i.e.
# 01 -> 10
# 02 -> 11 -> 20

# for each cell, the sum of their row index and column index is the same
# 01 -> 10, the sum is always `1`
# 02 -> 11 -> 20, the sum is always `2`

# this allows me mark that diagonal as reached.

# and for backward slanting diagonals i.e.
# 10 -> 21 -> 32
# 00 -> 11 -> 22 -> 33

# for each cell the difference between the row index and column index is the same
# 10 -> 21 -> 32, the difference is `1`
# 00 -> 11 -> 22 -> 33, the difference is `0`

# this way i can identify these guys..

# for variables, i'd use.. `reachedFsds`, `reachedBsds`
# and i think problem solved..


# TODO see if this is most efficient..
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = self.generateBoard(n)

        self.reachedRows = set()
        self.reachedColumns = set()
        self.reachedFsds = set()
        self.reachedBsds = set()
        
        self.validConfigurations = []
        
        startRowIdx = 0
        self.placeQueenOnRow(startRowIdx)
        
        return self.validConfigurations
        
    def generateBoard(self, n):
        board = []
        
        for _ in range(n):
            row = []
            for _ in range(n):
                row.append('.')
            board.append(row)
            
        return board
    
    def placeQueenOnRow(self, rowIdx):
        dim = len(self.board)
        if rowIdx == dim:
            self.validConfigurations.append(
                [''.join(row) for row in self.board]
            )    
            return
        
        
        row = self.board[rowIdx]
        for colIdx in range(dim):
            if not self.is_valid_pos(rowIdx, colIdx): continue
            
            self.reachedRows.add(rowIdx)
            self.reachedColumns.add(colIdx)
            
            fsdIdentifier = rowIdx + colIdx
            self.reachedFsds.add(fsdIdentifier)
            
            bsdIdentifier = rowIdx - colIdx
            self.reachedBsds.add(bsdIdentifier)
            
            row[colIdx] = 'Q'
            
            self.placeQueenOnRow(rowIdx + 1)
            
            row[colIdx] = '.'
            
            self.reachedRows.remove(rowIdx)
            self.reachedColumns.remove(colIdx)
            self.reachedFsds.remove(fsdIdentifier)
            self.reachedBsds.remove(bsdIdentifier)
            
    def is_valid_pos(self, rowIdx, colIdx):
        if rowIdx in self.reachedRows or\
            colIdx in self.reachedColumns or\
                (rowIdx + colIdx) in self.reachedFsds or\
                    (rowIdx - colIdx) in self.reachedBsds:
                        return False
                    
        return True
                

arr = [
    4,
    2,
    1,
]
foo = arr[-1]
sol = Solution()
res = sol.solveNQueens(foo)

for _ in res:
    print(_)