class Solution:
    def setZeroes(self, matrix: list):
        """
        Do not return anything, modify matrix in-place instead.
        """
        do_first_row = False
        rows, cols = len(matrix), len(matrix[0])
        for ri in range(rows):
            for ci in range(cols):
                if matrix[ri][ci] == 0:
                    matrix[0][ci] = 0

                    if ri > 0:
                        matrix[ri][0] = 0
                    else:
                        do_first_row = True

        for ri in range(1, rows):
            for ci in range(1, cols):                    
                if matrix[ri][0] == 0 or matrix[0][ci] == 0:
                    matrix[ri][ci] = 0

        for ri in range(rows):
            if matrix[0][0] == 0:
                matrix[ri][0] = 0

        if do_first_row:
            for ci in range(cols):
                matrix[0][ci] = 0
                    

arr = [
    [[1,1,1],[1,0,1],[1,1,1]],
    [[0,1,2,0],[3,4,5,2],[1,3,1,5]],
    [[-4,-2147483648,6,-7,0],[-8,6,-8,-6,0],[2147483647,2,-9,-6,-10]],
]
foo = arr[-1]
sol = Solution()

sol.setZeroes(foo)

for row in foo:
    print(row)