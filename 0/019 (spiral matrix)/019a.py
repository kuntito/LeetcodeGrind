# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        rows, cols = len(matrix), len(matrix[0])
        count = rows * cols
        ri, ci = 0, -1
        step_ri, step_ci = 0, 1
        while count:
            next_pos = (ri + step_ri, ci + step_ci)
            if self.is_valid(next_pos, matrix):
                ri += step_ri
                ci += step_ci
                count -= 1
                res.append(matrix[ri][ci])
                matrix[ri][ci] = None
            else:
                step_ri, step_ci = step_ci, -1 * step_ri

        return res
    
    def is_valid(self, pos, matrix):
        rows, cols = len(matrix), len(matrix[0])
        ri, ci = pos
        if ri < 0 or ri == rows or ci < 0 or ci == cols or matrix[ri][ci] is None:
            return False
        return True
            

arr = [
    [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
    ],
    [[5, 6, 7]],
    [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ],
    [
        [7],
        [9],
        [6]
    ],
    [
        [1,  2, 3, 4],
        [5,  6, 7, 8],
        [9 ,10,11,12],
        [13,14,15,16],
        [17,18,19,20],
        [21,22,23,24]
    ], 
    # [
    #     [1,2],
    #     [3,4]
    # ],
]
foo = arr[-1]
sol = Solution()

res = sol.spiralOrder(foo)
print(res)