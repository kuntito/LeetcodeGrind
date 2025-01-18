# https://leetcode.com/problems/range-sum-query-2d-immutable/description/

# https://neetcode.io/solutions/range-sum-query-2d-immutable
# 07:19, implement your own version
class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.prefixSum = matrix
        
        # starting from behind, in each row, iterate through every column
        # determine the prefix sum and update the values in `self.prefixSum`
        for ri, row in enumerate(matrix):
            tmp = 0
            for ci in range(len(row) - 1, -1, -1):
                tmp += row[ci]
                self.prefixSum[ri][ci] = tmp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass
        res = 0
        # iterate through each row in range(row1, row2 + 1)
        # to get the sum of the column range
        cols = self.matrix[0]
        for ri in range(row1, row2 + 1):
            row = self.prefixSum[ri]
            prefixAfterCol2 = row[col2+1] if col2 + 1 < len(cols) else 0
            res += row[col1] - prefixAfterCol2
            
        print(res)
        return res



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