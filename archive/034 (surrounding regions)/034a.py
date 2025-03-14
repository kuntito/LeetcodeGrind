# https://leetcode.com/problems/surrounded-regions/description/


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()
        for ri, row in enumerate(board):
            for ci, val in enumerate(row):
                if val == 'X': continue
                region = []
                is_valid = self.explore(ri, ci, board, visited, region, True)
                if is_valid:
                    for r, c in region:
                        board[r][c] = 'X'
        

    def explore(self, start_ri, start_ci, board, visited, region, is_valid):
        if (start_ri, start_ci) in visited: return is_valid
        visited.add((start_ri, start_ci))

        if self.is_near_border(start_ri, start_ci, board):
            is_valid = False

        region.append((start_ri, start_ci))
        neighbours = self.get_valid_neighbours(start_ri, start_ci, board, visited)
        for r, c in neighbours:
            if not self.explore(r, c, board, visited, region, is_valid):
                is_valid = False

        return is_valid

    def get_valid_neighbours(self, start_ri, start_ci, board, visited):
        rows, cols = len(board), len(board[0])

        neighbours = (
            (start_ri - 1, start_ci),
            (start_ri + 1, start_ci),
            (start_ri, start_ci - 1),
            (start_ri, start_ci + 1),
        )

        return (
            (r, c) for r, c in neighbours if r >= 0 and\
                r < rows and\
                c >= 0 and\
                c < cols and\
                (r, c) not in visited and\
                board[r][c] == 'O'
        )

    def is_near_border(self, r, c, board):
        rows, cols = len(board), len(board[0])
        return r == 0 or r == rows - 1 or c == 0 or c == cols - 1



arr = [
    [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"]
    ],
    # [['X']],
    # [
    #     ["O","O","O"],
    #     ["O","O","O"],
    #     ["O","O","O"],
    # ],
    # [
    #     ["O","X","X","O","X"],
    #     ["X","O","O","X","O"],
    #     ["X","O","X","O","X"],
    #     ["O","X","O","O","O"],
    #     ["X","X","O","X","O"]
    # ],
    # [
    #     ["X","O","X"],
    #     ["O","X","O"],
    #     ["X","O","X"]
    # ],
    # [
    #     ["O","O","O","O","X","X"],
    #     ["O","O","O","O","O","O"],
    #     ["O","X","O","X","O","O"],
    #     ["O","X","O","O","X","O"],
    #     ["O","X","O","X","O","O"],
    #     ["O","X","O","O","O","O"]
    # ],
]
foo = arr[-1]
sol = Solution()
sol.solve(foo)

for row in foo:
    print(row)