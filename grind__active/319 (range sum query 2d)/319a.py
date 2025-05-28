# https://leetcode.com/problems/range-sum-query-2d-mutable/description/

from typing import List

# what's the crack?

# i'm given a 2d integer matrix
# i want to implement the class `NumMatrix`
# with two methods, `update` and `sumRegion`

# `update` takes three integer arguments, `row`, `col` and `val`
# they're coordinates for a matrix cell, i.e. matrix[row][col] = val

# `sumRegion` takes four integer arguments
# `row1, col1`
# `row2, col2`

# these coordinates represent the topLeft corner and bottom right corner of a rectangle
# `sumRegion` should return the sum of the integers in this space.

# let me priortize `sumRegion` since it seems simpler
# the bruteforce is go through every element in the rectangle and sum it up
# but prefix sums can help us do better
# if i prefix sum each row, i can run through every row and get the sum in O(1)


# the only problem would be updates, when i update a cell
# i should update the prefix sum on that row, from the specific column onwards
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

        # i need a prefix matrix
        self.prefixMatrix = []

        for row in self.matrix:
            prefixRow = []
            total = 0
            for val in row:
                total += val
                prefixRow.append(total)
            self.prefixMatrix.append(prefixRow)
            


    def update(self, row: int, col: int, val: int) -> None:
        targetRow = self.matrix[row]
        targetPrefixRow = self.prefixMatrix[row]
        
        # we update the col in `targetRow`
        targetRow[col] = val
        
        # then update the prefixes in `targetPrefixRow`
        # if there is a previous column then total would the prefix sum up till the previous column
        total = targetPrefixRow[col - 1] if col > 0 else 0
        for idx in range(col, len(targetRow)):
            total += targetRow[idx]
            targetPrefixRow[idx] = total

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # for this i need to iterate through every row
        # get the sum prefixSum[col2] - prefix[col1-1]

        total = 0
        for ri in range(row1, row2 + 1):
            row = self.prefixMatrix[ri]
            
            endSum = row[col2]
            startSum = row[col1 - 1] if col1 > 0 else 0
            
            rowSum = endSum - startSum
            total += rowSum
        
        # print(total)
        return total


arr = [
    [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5],
    ],
]
foo = arr[-1]
sol = NumMatrix(foo)
sol.sumRegion(2, 1, 4, 3)
sol.update(3, 2, 2)
sol.sumRegion(2, 1, 4, 3)

# for row in sol.prefixMatrix:
#     print(row)
