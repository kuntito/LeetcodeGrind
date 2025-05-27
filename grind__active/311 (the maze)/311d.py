# https://leetcode.com/problems/the-maze/description/

from typing import List


class Solution:
    def hasPath(
        self, maze: List[List[int]], start: List[int], destination: List[int]
    ) -> bool:
        self.rows, self.cols = len(maze), len(maze[0])
        self.maze = maze

        seen = set()

        start = tuple(start)
        destination = tuple(destination)

        return self.explore(start, destination, seen)

    def explore(self, currPos, destination, seen):
        if currPos in seen:
            return False

        if currPos == destination:
            return True

        seen.add(currPos)

        # for `currPos`, you want to explore all four directions till you hit a wall

        dirs = ((0, -1), (0, 1), (-1, 0), (1, 0))
        
        
        for d in dirs:
            incRi, incCi = d
            
            ri, ci = currPos
            
            while self.isValid(ri + incRi, ci + incCi):
                ri += incRi
                ci += incCi
                
            if self.explore(
                (ri, ci),
                destination,
                seen
            ): return True
            
        return False
            
    def isValid(self, ri, ci):
        if ri < 0 or ri == self.rows or ci < 0 or ci == self.cols or self.maze[ri][ci]:
            return False
        return True
        
arr = [
    [[
        [0,0,1,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [1,1,0,1,1],
        [0,0,0,0,0]
    ], [0, 4], [4, 4]],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.hasPath(foo, bar, baz)
print(res)