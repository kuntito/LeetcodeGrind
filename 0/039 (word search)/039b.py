# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for ri, row in enumerate(board):
            for ci, ch in enumerate(row):
                if ch == word[0]:
                    if self.explore(ri, ci, 0, word, board, set()):
                        return True
                    
        return False
    
    
    def explore(self, start_ri, start_ci, idx, word, board, visited):
        if board[start_ri][start_ci] != word[idx]: return False

        if idx == len(word) - 1:
            return True
        
        res = False
        visited.add((start_ri, start_ci))
        neighbours = self.get_valid_neighbours(start_ri, start_ci, board, visited)
        for nei in neighbours:
            ri, ci = nei
            if self.explore(ri, ci, idx + 1, word, board, visited):
                res = True
                break
        visited.remove((start_ri, start_ci))
            
        return res

    
    def get_valid_neighbours(self, ri, ci, board, visited):
        rows, cols = len(board), len(board[0])
        neighbours = (
            (ri - 1, ci),
            (ri + 1, ci),
            (ri, ci + 1),
            (ri, ci - 1),
        )

        return [
            (r, c) for r, c in neighbours if r >= 0 and r < rows and c >= 0 and c < cols
            and (r, c) not in visited
        ]
    
arr = [
    [
        [
            ["A","B","C","E"],
            ["S","F","C","S"],
            ["A","D","E","E"]
        ],
        "ABCCED"
    ],
    [
        [
            ["A","B","C","E"],
            ["S","F","E","S"],
            ["A","D","E","E"]
        ],
        "ABCESEEEFS"
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.exist(foo, bar)
print(res)