# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/description/

# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

# we have a matrix, a 2d grid
# with only 0s and 1s
# each row is sorted in non-decreasing order
# and we want to find the index of the leftmost column with a `1` in it

# caveat is, we don't have direct access to grid
# we have an interface `BinaryMatrix` that exposes two methods
# `get` and `dimensions`

# `get` takes two integer arguments, rowIdx and colIdx and returns the value at said location
# `dimensions` returns a list of two elements, [numRows, numCols]

# how can i find the index of the left most column with a `1` in it
# without making more than 1000 class to the interface, `BinaryMatrix`

# i'd obtain the dimensions, `numRows`, `numCols`
# if i do binary search on every row
# till i find the index of the first `1`

# i know my answer would be <= that rowIdx
# this would be a recursive solution

# the idea there is to bin search every row in order till you find the least `1`
# save the value
# once you have this you've basically narrowed the search
# to a subset of the initial `numRows`, `numCols`
# a subGrid if you will

# now you do the same bin search on every row in that sub grid till you find a `1`
# narrow the search and continue
class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        
        self.rows = rows
        self.binaryMatrix = binaryMatrix
        return self.explore(0, cols)
    
    def explore(self, startRi, cols):
        leastCol = -1
        
        # for every row, conduct a binSearch for a `1`
        for ri in range(startRi, self.rows):
            # `res` would be the column index of the least `1`
            idx = self.binSearch(ri, cols)
            
            # this means we have a candidate, now we narrow the search
            # and try to find a smaller candidate
            if idx != -1:
                cols = idx
                leastCol = idx
        
        return leastCol
    
    def binSearch(self, rowIdx, maxCols):
        left, right = 0, maxCols - 1
        
        least = -1
        while left <= right:
            colIdx = (left + right)//2
            
            val = self.binaryMatrix.get(rowIdx, colIdx)
                
            if val == 0:
                left = colIdx + 1
            else:
                least = colIdx
                right = colIdx - 1
                
        return least