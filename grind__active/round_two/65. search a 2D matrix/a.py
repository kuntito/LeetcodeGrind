# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List

# i'm given two things, 
# a 2d array of integers, `matrix`
# and an integer `target`

# in `matrix`,
# each row is sorted in non-decreasing order
# moving downwards, the last integer of each row
# is less than or equal to the first integer of the next row

# my job is to find out if `target` exists in `matrix`
# i'm asked to do it in O(log(m*n)) time

# not sure what that means.. but the sorted nature of the array
# suggests i can use binary search

# but how would it go..
# if `target` exists, it's on one row..

# but which one?
# for target to be on a row..
# the first element of that row must be less than or equal to target
# but multiple rows can fill that criterion
# how do you know which one?

# we can iterate in reverse..
# the first row..

# we want to narrow our search down..
# if we iterate through the matrix in reverse
# we find the first row whose first element is less than or equal to `target`

# at this point, we can conclude..
# if `target` exists, it must be on that row or downwards..

# okay, what next.. well, we check the last element on that row..
# if it's also less than target..
# well it can't be less than `target` else we'd have stopped at that row..

# since, we iterated in reverse..
# the row we stop at must have it's last element greater than or equal to target..
# so that's the row we want to search..
# perform binary search on that row..

# call it a day..

# i did it but my run time is O(m + log(n))

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        searchRow = self.getSearchRow(matrix, target)
        if not searchRow:
            return False
        
        left, right = 0, len(searchRow) - 1
        
        while left <= right:
            midPoint = left + (right - left)//2
            
            midVal = searchRow[midPoint]
            
            if target == midVal:
                return True
            elif target > midVal:
                left = midPoint + 1
            elif target < midVal:
                right = midPoint - 1
                
        return False
                
        
    def getSearchRow(self, matrix, target):
        for row in matrix[::-1]:
            if target >= row[0]:
                return row
    