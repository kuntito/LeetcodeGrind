# https://leetcode.com/problems/the-maze/description/

from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        rows, cols = len(maze), len(maze[0])
        
        # duplicating the grid to indicate visited cells
        # `False` means unvisited.
        visit = [[False] * cols for _ in range(rows)]
        
        return self.explore(rows, cols, maze, start, destination, visit)
    
    def explore(self, rows, cols, maze, curr, destination, visit):
        ri, ci = curr
        if visit[ri][ci]:
            return False
        
        if ri == destination[0] and ci == destination[1]:
            return True

        visit[ri][ci] = True
        dirX = [0, 1, 0, -1]
        dirY = [-1, 0, 1, 0]

        for i in range(4):
            r = curr[0]
            c = curr[1]
            
            # Move the ball in the chosen direction until it can.
            while r >= 0 and r < rows and c >= 0 and c < cols and maze[r][c] == 0:
                r += dirX[i]
                c += dirY[i]
                
            # Revert the last move to get the cell to which the ball rolls.
            if self.explore(
                rows,
                cols,
                maze, 
                [r - dirX[i], c - dirY[i]],
                destination,
                visit
            ):
                return True
        return False