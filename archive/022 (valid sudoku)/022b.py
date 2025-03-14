from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        subgrids = defaultdict(set)

        for ri, row in enumerate(board):
            for ci, val in enumerate(row):
                if val == '.': continue

                small_grid_pos = (ri//3, ci//3)
                if val in rows[ri] or\
                    val in cols[ci] or\
                    val in subgrids[small_grid_pos]:
                
                    return False
                
                rows[ri].add(val)
                cols[ci].add(val)
                subgrids[small_grid_pos].add(val)

        # print(subgrids[(0, 0)])

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