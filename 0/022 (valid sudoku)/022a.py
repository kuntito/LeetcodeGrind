# https://leetcode.com/problems/valid-sudoku/description/


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # rows
        for row in board:
            seen = set()
            for val in row:
                if val == '.': continue
                if val in seen: return False
                seen.add(val)


        # cols
        for ci in range(9):
            seen = set()
            for ri in range(9):
                val = board[ri][ci]
                if val == '.': continue
                if val in seen: return False
                seen.add(val)


        # sub grids
        for big_ri in range(3):
            for big_ci in range(3):
                start_ri = big_ri * 3
                start_ci = big_ci * 3
                seen = set()
                for ri in range(start_ri, start_ri + 3):
                    for ci in range(start_ci, start_ci + 3):
                        val = board[ri][ci]
                        if val == '.': continue
                        if val in seen: return False
                        seen.add(val)

        return True
        

arr = [
    [
        ["8","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
]
foo = arr[-1]
sol = Solution()

res = sol.isValidSudoku(foo)
print(res)