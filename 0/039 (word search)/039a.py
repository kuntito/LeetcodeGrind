# https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        for ri, row in enumerate(board):
            for ci, ch in enumerate(row):
                if ch == word[0]:
                    if self.explore(ri, ci, word, board, set()):
                        return True
                    
        return False
    
    
    def explore(self, start_ri, start_ci, word, board, visited):
        if board[start_ri][start_ci] != word[0]: return False

        if len(word) == 1:
            return True
        
        res = False
        visited.add((start_ri, start_ci))
        neighbours = self.get_valid_neighbours(start_ri, start_ci, board, visited)
        for nei in neighbours:
            ri, ci = nei
            if self.explore(ri, ci, word[1:], board, visited):
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