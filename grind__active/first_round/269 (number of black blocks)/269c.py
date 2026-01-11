# https://leetcode.com/problems/number-of-black-blocks/
from typing import List

# i want to implement a function that returns a list of integers.
# it takes three arguments. two integers, m, and n, and a 2d integer array called `coordinates`.

# `m` and `n` represent the row by column dimensions of the 2d array, `coordinates`

# that's wrong. `m` and `n` represent the row by column dimensions of an unstated grid. we are to assume a grid a of `m by n`, rows and columns.

# and coordinates is an array that contains, well, coordinates.
# each element of the array is like this. [x, y]
# where `x` is a row index
# and `y` is a column index on the unstated grid.

# what these coordinates indicate is the cells on the unstated grid.
# let's give this unstated grid a name. imma call it grid.
# these coordinates indicated the cells on `grid` that are black.

# all coordinates not in `coordinates` indicate their corresponding cells are white.

# but what am i to do with this information?
# well, the question says there's something called a block.
# it's a 2x2 grid overlayed on `grid`

# consider the grid
# 00 01 02
# 10 11 12
# 20 21 22

# the block would overlay
# 00 01
# 10 11

# the block can move within the larger grid in whatever direction.
# it's simplest to say the block moves left to right, that is,
# the next block would be

# 01 02
# 11 12

# at this point, we can't go any rightwards
# so we restart the block movement on the next row
# that is, the next block is

# 10 11
# 20 21

# this way, it's clear to see how the block moves.

# we want to return an array of size 5 such that arr[i] is the number of blocks that contain exactly i black cells

# in english, please.
# we want to return an array of size 5
# okay.. and `arr[i]`, meaning each index of the size 5 array
# would contain the number of blocks the `i` number of black cells

# i.e. 
# arr[0] would contain the number of blocks with zero black cells
# arr[1] would contain the number of blocks with one black cell
# arr[2] would contain the number of blocks with two black cells

# and so on and so forth...
# this looks crazy.

# how to approach the situation. one way is to move each block through the grid, count how many black cells in each block and update the result variable accordingly.

# it's reasonable that the result is of size 5
# since the maximum blocks in 2x2 grid is `4` and the minimum is `0`
# hence the array indices, 0,1,2,3,4

# i think i tried this approach in the previous attempt.
# let me see what i did if it's useful.

# the code in 269a.py is an implementation of this idea.
# but it runs into time limit exceeded error
# 2094 / 2145 

# i'll just read the editorial to speed things up.
# damn, no editorial.

# discussions maybe?
# seems to me, they took a shortcut.
# rather than exploring all the blocks
# they explored each black cell and the blocks it can be in.

# the intuition is every black cell can be in one of four blocks??



class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        pass