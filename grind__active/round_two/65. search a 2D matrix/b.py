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

# apparently, this means, treat the entire 2d matrix as a long line of elements
# and perform binary search on that..

# but how exactly would the midpoint work..
# well you could map each coordinate to an array of numbers
# then perform bin search on that array of numbers and 
# use that to find `target`

# you could but O(n) is larger than O(log m*n)
# so this would defeat the purpose
# you want to ball through the array as-is..

# modaran..

# what if i do the same thing as the mapping but without the mapping..
# instead, i'd use a function to map each number to it's respective coordinates..

# how would that work..
# from the jump, i know how many elements are in the array..

# so my bin search is `0..dim-1`
# now when i get mid point, i'd use a function to figure out what coordinates
# mid point points to..
# then return the value..

# that's definitely O(log m*n)
# the calculation is at most O(1)

# let's do this and see..

# TODO figure why it don't work
# i think the reasoning is sound but ... 
# see ..

    # [
    #     [
    #         [1,3,5,7],
    #         [10,11,16,20],
    #         [23,30,34,60]
    #     ],
    #     3,
    # ]
    
# error, the problem was the conditionals for the binary search
# i'd swapped the pointer shifting for when the mid point value was
# not equal to `target`

# a calmer, more methodical approach to this
# would've let me see clearer.

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        
        rows, cols = len(matrix), len(matrix[0])
        right = (rows*cols) - 1
        
        while left <= right:
            midPoint = left + (right - left)//2
            
            val = self.getVal(midPoint + 1, matrix)
            
            if val == target:
                return True
            elif target < val:
                right = midPoint - 1
            elif target > val:
                left = midPoint + 1
                
        return False
    
    def getVal(self, itemNumber, matrix):
        rows, cols = len(matrix), len(matrix[0])
        rowLen = cols
        
        # now, how do i find the coordinates of a cell based on it's number
        # within the entire index..
        
        # we need to know what row it is
        
        # consider
        # 1 2 3
        # 4 5 6
        
        # if i give you `5`
        # what row would it be..
        # if youb mod it by row length
        # 5 mod 3 = 2
        
        # nah you need div mod..
        # quo, rem = divmod(itemNumber, rowLen)
        
        # `quo` tells you how many rows before..
        # `rem` tells you how many elements on the next row..
        
        # what if you have item number as `3`
        # divmod(3, 3) = 1, 0
        # no remainder suggests `quo` tells  you the current row..
        # and the element you want is the last element on row `quo`
        
        # how about divmod(2, 3) = (0, 2)
        # when `quo` is `0` it means there's zero rows before the number
        
        quo, rem = divmod(itemNumber, rowLen)
        
        if rem == 0:
            return matrix[quo-1][-1]
        elif rem > 0:
            return matrix[quo][rem-1]
    
arr = [
    [
        [
            [1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]
        ],
        3,
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.searchMatrix(foo, bar)
print(res)