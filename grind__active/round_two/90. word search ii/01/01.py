from typing import List

# TODO rewrite solution...
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        pass
    
        posCache = self.getCharPosCache(board)
        
        self.resultArr = []
        
        seenCells = set()
        for w in words:
            firstCh = w[0]
            if firstCh in posCache:
                positions = posCache[firstCh]
                for pos in positions:                    
                    self.explore(
                        0,
                        pos,
                        w,
                        board,
                        seenCells,
                    )
                    
        return self.resultArr
    
    
    def explore(self, chIdx, pos, w, board, seenCells):
        if chIdx == len(w):
            self.resultArr.append(w)
            return
        if pos in seenCells:
            return
        if self.is_invalid_pos(pos, board):
            return
        
        r, c = pos
        ch = w[chIdx]
        if board[r][c] != ch:
            return
        
        seenCells.add(pos)
        
        self.explore(chIdx + 1, (r, c - 1), w, board, seenCells)
        self.explore(chIdx + 1, (r, c + 1), w, board, seenCells)
        self.explore(chIdx + 1, (r - 1, c), w, board, seenCells)
        self.explore(chIdx + 1, (r + 1, c), w, board, seenCells)
        
        seenCells.remove(pos)
        
        
    def is_invalid_pos(self, pos, board):
        rows, cols = len(board), len(board[0])
        
        r, c = pos
        
        return r < 0 or r == rows or c < 0 or c == cols
    
        
    def getCharPosCache(self, board):
        cache = {}
        
        for ri, row in enumerate(board):
            for ci, ch in enumerate(row):
                if ch not in cache:
                    cache[ch] = []
                    
                cache[ch].append(
                    (ri, ci)
                )
                
        return cache
    
arr = [
    [
        [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ],
        ["oath","pea","eat","rain"],
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findWords(foo, bar)
print(res)