# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows
        left, right = 0, cols
        
        res = []
        while top < bottom and left < right:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if len(res) == rows * cols: break

            for i in range(right-1, left-1, -1):
                res.append(matrix[bottom-1][i])
            bottom -= 1

            for i in range(bottom-1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res