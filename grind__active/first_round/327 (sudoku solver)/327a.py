# https://leetcode.com/problems/sudoku-solver/description/
from typing import List

# i'm to implement a function called `solveSudoku`
# the function takes a 9x9 string array
# the array represents a sudoku board with certain positions pre-filled

# my job is to write an algo that solves the sudoku board
# the rules are:
# for each row, the digits 1-9 must occur exactly once
# for each col, the digits 1-9 must occur exactly once
# for each 3x3 sub-box, the digits 1-9 must occur exactly once

# the character '.' indicates an empty cell

# how do i approach this?
# let's try to bruteforce it
# what would this even look like?

# [
#     ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#     ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#     [".", "9", "8", ".", ".", ".", ".", "6", "."],
#     ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#     ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#     ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#     [".", "6", ".", ".", ".", ".", "2", "8", "."],
#     [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#     [".", ".", ".", ".", "8", ".", ".", "7", "9"],
# ]

# say i explore row by row
# for each blank cell, i want to try every posisble number

# for one, i need to know the numbers already on that row
# to know what other numbers i can explore

# i'd also need to know the numbers on that column
# to know what numbers i can explore

# i'd also need to know the numbers on it's 3x3 block
# to know what numbers i can explore

# once i identify the set of numbers
# i can pick one number
# then move to the next blank cell and repeat

# it'd be a backtracking solution
# the path ends if there's a blank cell with no valid options
# or we've explore all cells

# i can use a hashmap to store the values for each row
# i can also use a hashmap to store the values for each column

# but how would i represent the 3x3 sub-box
# consider the indices for a 9x9 board.

# (0,0) (0,1) (0,2) (0,3) (0,4) (0,5) (0,6) (0,7) (0,8)  
# (1,0) (1,1) (1,2) (1,3) (1,4) (1,5) (1,6) (1,7) (1,8)  
# (2,0) (2,1) (2,2) (2,3) (2,4) (2,5) (2,6) (2,7) (2,8)  
# (3,0) (3,1) (3,2) (3,3) (3,4) (3,5) (3,6) (3,7) (3,8)  
# (4,0) (4,1) (4,2) (4,3) (4,4) (4,5) (4,6) (4,7) (4,8)  
# (5,0) (5,1) (5,2) (5,3) (5,4) (5,5) (5,6) (5,7) (5,8)  
# (6,0) (6,1) (6,2) (6,3) (6,4) (6,5) (6,6) (6,7) (6,8)  
# (7,0) (7,1) (7,2) (7,3) (7,4) (7,5) (7,6) (7,7) (7,8)  
# (8,0) (8,1) (8,2) (8,3) (8,4) (8,5) (8,6) (8,7) (8,8)  

# how do i identify each cell's sub-box?

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        pass
