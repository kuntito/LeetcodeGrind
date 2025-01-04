# https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        target_rows = set()
        target_cols = set()
        for ri in range(rows):
            for ci in range(cols):
                if matrix[ri][ci] == 0:
                    target_rows.add(ri)
                    target_cols.add(ci)


        for ri in target_rows:
            for ci in range(cols):
                matrix[ri][ci] = 0

        
        for ci in target_cols:
            for ri in range(rows):
                matrix[ri][ci] = 0

arr = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
]
foo = arr[-1]

sol = Solution()
sol.setZeroes(foo)
for row in foo:
    print(row)
