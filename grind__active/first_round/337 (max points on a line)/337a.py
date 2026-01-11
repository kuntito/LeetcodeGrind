# https://leetcode.com/problems/max-points-on-a-line/description/

from typing import List


# i want to implement a function, `maxPoints`.
# this function takes a 2d array of integers called points and returns an integer.

# this function returns an integer and takes one argument, a 2d integer array called points.

# the gist is i want to return the number of points on a straight line.
# each element of `points`, represents a coordinate.

# my job is to count the number of points on the same straight line.
# for example,
# 
# the coordinates `(1, 1)`, `(2, 2)` and `(3, 3)`, when drawn out
# all lie on the same line.
# a diagonal line.

# a remember a concept from a different problem. i think n queens.
# it's really a trick. all diagonals can be described by the interac-

# i'm jumping the gun here.
# i want to count the number of points on a straight line.

# a straight line is in three forms.
# vertical, horizontal and diagonal.

# the ones on a vertical-

# i think a straight line is in two forms.
# or maybe all straight lines are in one form.

# the three forms explanation is clearest in my head.
# the vertical lines share a column
# the horizontal lines share a row
# the diagonal lines can be described with the row-column relationship between successive points.

# let's look at a 3x3 board
# the coordinates of a 3x3 board

# 00 01 02
# 10 11 12
# 20 21 22

# let's consider the diagonal, 00-11-22
# this diagonal can be described by the integer result of 
# `row` minus `col`
# every point on this line has `row - col == 0`

# same can be said of the diagonal, 10-21
# `row - col`  is `1`
# both points, `10` and `21`
# have the same row-col relationship
# hence, can be said to be on a straight diagonal

# consider the diagonal
# 02-11-20
# unlike the first two diagonals, 00-11-22, 10-21
# 
# this one is a forward slanting diagonal
# it can also be identified by the row-column relationship between successive points
# but this time, we add the rows and columns

# 02 = 0 + 2 = 2
# 11 = 1 + 1 = 2
# 20 = 2 + 0 = 2

# does this cover all diagonals? only one way to find out.

# quick clarification, we want to find the straight line with the most points
# and return that value.

# in simpler terms, we want to identify all the straight lines and the number of points on each line then return the most points counted on a single line.



class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        pass
        
        # i can run through all the points
        # for verticals and horizontals, i'd define a hashmap
        # a counter, for each rowIndex and colIndex
        
        # this way i can tell how many points on each vertical line
        # and how many points on each horizontal line
        
        # the diagonals is the tricky one
        # how do i know two points form a diagonal?
        
        # technically, any two points that are not vertical or horizontal must be diagonal.