# https://leetcode.com/problems/available-captures-for-rook/description/

class Solution:
    def numRookCaptures(self, board: list[list[str]]) -> int:
        pass
        # find the rook's position
        # explore cardinal directions until you hit
        # a bishop or another pawn
        # if you hit another pawn, increment count by `1`
        
        rookPos = self.findRookPos(board)
        
        cardinals = (
            (1, 0), # up
            (-1, 0), # down
            (0, 1), # right
            (0, -1) # left
        )
        
        res = 0
        for dirc in cardinals:
            res += self.exploreDir(dirc, rookPos, board)
            
        return res
    
    def findRookPos(self, board):
        for ri, row in enumerate(board):
            for ci, val in enumerate(row):
                if val == 'R':
                    return ri, ci
                
    def exploreDir(self, dirc, origin, board):
        incRi, incCi = dirc
        
        
        ri, ci = origin
        while self.is_valid(ri + incRi, ci + incCi, board):
            ri += incRi
            ci += incCi
            val = board[ri][ci]
            if val == 'B':
                break
            if val == 'p':
                return 1
            
        return 0
    
    def is_valid(self, ri, ci, board):
        rows, cols = len(board), len(board[0])
        
        return ri >= 0 and ri < rows and ci >= 0 and ci < cols

    
    
arr = [
    [[".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]],
    [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]],
]
foo = arr[-1]
sol = Solution()
res = sol.numRookCaptures(foo)
print(res)