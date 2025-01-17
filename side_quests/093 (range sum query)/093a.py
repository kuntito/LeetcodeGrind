# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefixSum = matrix
        
        # iterate through every column in each row from behind
        # determine the prefix sum and update the values in `self.prefixSum`
        rows = len(matrix)
        for ri in range(rows):
            pass

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass



matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
sol = NumMatrix(matrix)
sol.sumRegion(2, 1, 4, 3)
sol.sumRegion(1, 1, 2, 2)
sol.sumRegion(1, 2, 2, 4)