from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        self.board = board
        self.result = None
        # so, what's step one?
        # find the zero.
        zeroPos = self.findZero(board)
        
        # once you do, what next?
        # explore every direction.
        visited = set()
        self.explorePaths(zeroPos, visited)
        
        # return the shortest path
        # if it exists, else -1
        return -1 if self.result is None else self.result
        
    def findZero(self, board):
        for ri, row in enumerate(board):
            for ci, val in enumerate(row):
                if val == 0:
                    return ri, ci
                
                
    def explorePaths(self, curPos, visited):
        # so, what am i doing here?
        # go up, go left, go right, go down
        # repeat.
        
        # what does each exploration look like?
        # along each path, one of three things could happen:
        #   you hit a deadend
        #   you hit a visited position
        #   you hit bottom right
        
        # you stop, if deadend or visited position
        # technically, you stop at bottom right too..
        # just that, you check the position of other board members.
        
        # how do i track the visited positions.
        # a set.
        # the set, also doubles as number of moves made.
        # do you take the set with you?
        # yeah.
        
        if curPos in visited:
            return
        if self.isOutOfBounds(curPos):
            return
        if self.isBottomRight(curPos):
            self.updateResult(visited)
            return
        
        visited.add(curPos)
        
        ri, ci = curPos
        self.explorePaths((ri - 1, ci), visited)
        self.explorePaths((ri + 1, ci), visited)
        self.explorePaths((ri, ci - 1), visited)
        self.explorePaths((ri, ci + 1), visited)
        
        visited.remove(curPos)
        
        
    def isOutOfBounds(self, curPos):
        ri, ci = curPos
        
        rowCount = 2
        colCount = 3
        
        return ri < 0 or ri >= rowCount or ci < 0 or ci >= colCount
    
    def isBottomRight(self, curPos):
        ri, ci = curPos
        
        return ri == 1 and ci == 2
    
    def updateResult(self, visited):
        movesMade = len(visited)
        
        foo = [0, 5, 4, 3, 2, 1]        
        
        # TODO this check wouldn't work because i didn't modify the board values.
        # i simply moved zero across paths.
        # perhaps, there's a way, i can use the paths to modify the board.
        # it's really the history of zeros moves.
        # i'd swap cell values, verfiy arrangement
        # then revert swaps
        for ri, row in enumerate(self.board):
            for ci, val in enumerate(row):
                if val != foo.pop():
                    return
                
        if self.result is None:
            self.result == movesMade
        else:
            self.result = min(
                self.result,
                movesMade
            )
                
        
arr = [
    [[1,2,3],[4,0,5]]
]
foo = arr[-1]
sol = Solution()

res = sol.slidingPuzzle(foo)
print(res)