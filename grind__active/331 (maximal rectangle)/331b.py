# https://leetcode.com/problems/maximal-rectangle/description/

from typing import List

# want to implement a function. this function takes
# a 2d string array and returns an integer.

# this array only contains 0s and 1s, and the integer returned
# represents the area of the largest rectangle containing only 1s

# that's a lot of words though
# let's consider this array

# [[0, 1, 1],
# [[0, 1, 1]]

# we want to find the area of the largest rectangle containing only
# 1s. it's easy to see that the largest rectangle

# { draw line round rectangle }

# it has two rows and two columns
# hence, our area would be rowLen * colLen = 4

# that's basically what we have to do
# so how do we write this in code?

# well, for one, we need a way to identify rectangles that only have 1s
# how do we know what a rectangle is?


# not sure, all i know is, we want rectangles that contain only 1s
# so if i traverse each element of the 2d array, once i run into a 1
# i know it could be part of a rectangle

# using this example, my first element is `1`
# [[1, 1, 1],
#  [0, 1, 1]]

# and this could potentially be a rectangle.
# to be fair, `1` in isolation is already a rectangle
# a rectangle with one row and one column

# but we want to know, if it can grow even larger
# for it to be larger, it needs more rows or more columns
# or both


 


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        pass