class Solution:
    def setZeroes(self, matrix: list):
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows, cols = len(matrix), len(matrix[0])
        rows_explore = set()
        cols_explore = set()

        for ri in range(rows):
            for ci in range(cols):
                if matrix[ri][ci] == 0:
                    rows_explore.add(ri)
                    cols_explore.add(ci)

        for ri in range(rows):
            for ci in range(cols):
                if ri in rows_explore or ci in cols_explore:
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