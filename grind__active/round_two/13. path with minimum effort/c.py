# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List, OrderedDict


# rewriting this to now track the effort of each path
# dropping OrderedDict for a custom class that allows me track 
# max effort seen across any given path..

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])
        self.grid = heights
        sr, sc = 0, 0
        seen = OrderedDict()
        
        self.explore(sr, sc, seen)
        
    def explore(self, r, c, seen: OrderedDict):
        pos = (r, c)
        if pos in seen or self.is_out_of_bounds(*pos):
            return
        
        seen[pos] = self.grid[r][c]
        
        if r == self.rows - 1 and c == self.cols - 1:
            print(seen.values())
            del seen[pos]
            return
        
        self.explore(r - 1, c, seen)
        self.explore(r + 1, c, seen)
        self.explore(r, c - 1, seen)
        self.explore(r, c + 1, seen)
        
    
        del seen[pos]

        
    def is_out_of_bounds(self, r, c):
        return r < 0 or r == self.rows or c < 0 or c == self.cols
    
arr = [
    [        
        [1, 2, 2],
        [3, 8, 2],
        [5, 3, 5],
    ]
]
foo = arr[-1]
sol = Solution()
res = sol.minimumEffortPath(foo)
# print(res)