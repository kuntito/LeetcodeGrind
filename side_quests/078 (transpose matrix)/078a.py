# https://leetcode.com/problems/transpose-matrix/description/

# TODO https://neetcode.io/solutions/transpose-matrix
class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        pass
        rows, cols = len(matrix), len(matrix[0])
        
        trows, tcols = cols, rows
        tgrid = [[0 for _ in range(tcols)] for _ in range(trows)]
        

        # going down each cell in the first column
        for ri in range(rows):
            # for each cell in the first column, move right
            # arr = []
            for ci in range(cols):
                cell = matrix[ri][ci]
                tgrid[ci][ri] = cell
            # print(arr)

        return tgrid
    
    
arr = [
    [[1,2,3],[4,5,6]],
    [[1,2,3],[4,5,6],[7,8,9]],
    [
        [2,4,-1],
        [-10, 5, 11],
        [18, -7, 6]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.transpose(foo)

for r in res:
    print(r)