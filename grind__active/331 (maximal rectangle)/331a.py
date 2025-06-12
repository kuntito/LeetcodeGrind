# https://leetcode.com/problems/maximal-rectangle/

from typing import List

# i want to implement a function, `maximalRectangle`.
# this functions takes one argument, a 2d array of strings
# and returns an integer

# each string in the 2d array is either a "0" or a "1"
# my job is to find the largest rectangle containing only 1's and return it's area

# how do i achieve this?
# how do you define a rectangle?

# it has four straight sides
# but what does this mean in terms of array positions

# consider
# ["0", "1", "1", "1"]
# ["0", "1", "1", "1"]

# it's easy to see what a rectangle is
# but how do i represent that with code
# perhaps, if i list out the indices with 1s
# the picture becomes clearer

# - 01 02 03
# - 11 12 13

# a rectangle has four sides
# left, top, right, down
# the characteristic of the left side is the same column index
# all the 1s have the same column

# the characteristic of the top side is "same row index"
# all the 1s have the same row index


# the characteristic of the right side is the same column index
# all the 1s have the same column index
# however, this can be said of any line within the rectangle
# for instance, the column 02, 12 also fits the description
# of having the same column index

# well, yes, because column 02, 12 would also be a rectangle
# just not the largest one

# in a sense, i need the longest repeating streak of 1s
# where each row represent
# 

# i need to identify the most consecutive rows
# with the longest same streak on each row

# consider:
# [0, 1, 1, 1]
# [0, 1, 1, 0]
# [0, 1, 1, 0]
# [0, 1, 1, 0]

# the longest streak would be on the first row
# 1, 1, 1
# but it doesn't repeat on the lower rows
# so i go one less from the streak, 1, 1
# this pattern repeats for the next three rows and as such becomes my answer

# in a way for each row, i can find the longest streak
# see how far i can go downwards
# track the result
# reduce the streak and repeat

# there's some room for optimization here
# but let me try this approach out

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass
        # i want to explore each row
        for rowIdx, row in enumerate(matrix):
            self.exploreRowStreak(rowIdx, matrix)
            
    def exploreRowStreak(self, rowIdx, matrix):
        row = matrix[rowIdx]
        # i want to find the streaks on each row
        # then explore each streak downwards
        
        streaks = self.getStreaks(row)
        
    def getStreaks(self, row):
        dim = len(row)
        
        left = 0
        # `left` should be initialized to the first `1`
        while left < dim and row[left] == 0:
            left += 1
        
        streaks = []
        for idx, val in enumerate(row):
            if val == 0:
                # store the current streak
                streaks.append((left, idx))
                # if valid
                left = idx + 1
                
        # what if it was all zeros?
            