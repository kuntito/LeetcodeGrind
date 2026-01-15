# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# pip install ordered-set
from ordered_set import OrderedSet

# re writing this with ordered dict
# it's easier to verify the path traversed
# since the coordinates tuple is the dict key
# and the value is well, the cell value

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])
        sr, sc = 0, 0
        seen = OrderedSet()
        self.explore(sr, sc, seen)
    
    # what do we need here, we need current coordinates
    # access to the grid, self.heights, will do..
    # we need the set, let's pass it around...
    def explore(self, r, c, seen):
        pos = (r, c)
        if pos in seen or self.is_out_of_bounds(r, c):
            return
        
        seen.add(pos)
        
        if r == self.rows - 1 and c == self.cols - 1:
            print(seen)
            seen.remove(pos)
            return
        
        self.explore(r - 1, c, seen)
        self.explore(r + 1, c, seen)
        self.explore(r, c - 1, seen)
        self.explore(r, c + 1, seen)
        
        seen.remove(pos)
        
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