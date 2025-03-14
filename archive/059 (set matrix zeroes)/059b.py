# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        
        do_first = any(matrix[0][ci] == 0 for ci in range(cols))
        for ri in range(1, rows):
            for ci in range(cols):
                if matrix[ri][ci] == 0:
                    matrix[0][ci] = 0
                    matrix[ri][0] = 0

        # doing rows
        for ri in range(1, rows):
            if matrix[ri][0] == 0:
                self.do_rows(ri, matrix)

        # doing columns
        for ci in range(cols):
            if matrix[0][ci] == 0:
                self.do_columns(ci, matrix)
        
        if do_first:
            for ci in range(cols):
                matrix[0][ci] = 0


    def do_rows(self, ri, matrix):
        cols = len(matrix[0])
        for ci in range(1, cols):
            matrix[ri][ci] = 0


    def do_columns(self, ci, matrix):
        rows = len(matrix)
        for ri in range(1, rows):
            matrix[ri][ci] = 0



arr = [
    [[1],[0]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
    [[1,1,1],[1,0,1],[1,1,1]],
]
foo = arr[-1]

sol = Solution()
sol.setZeroes(foo)
for row in foo:
    print(row)
