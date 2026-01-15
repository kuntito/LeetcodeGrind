# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List

# i want this guy to have O(1) for checking cell position
# you don't really need the cell positions, well, you need to see
# if you've added the cell, a set can handle that..
# use an array to store the sequential cell values, array.pop can help remove items in one go..
# and a custom variable to track max effor so far
class PosTrack:
    def __init__(self, grid):
        self.grid = grid
        self.seen = set()
        self.arr = []
        self.maxEffort = 0
        
    def add(self, pos):
        self.seen.add(pos)
        
        
        r, c = pos
        val = self.grid[r][c]
        
        self.update_max_effort(val)
        self.arr.append(val)
        
    def remove(self, pos):
        self.seen.remove(pos)
        self.arr.pop()
        
    def has(self, pos):
        return pos in self.seen
    
    def print(self):
        print(self.maxEffort, "=>", self.arr)
        
    def update_max_effort(self, val):
        if self.arr:
            diff = abs(self.arr[-1] - val)
            
            self.maxEffort = max(diff, self.maxEffort)            


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        self.rows, self.cols = len(heights), len(heights[0])
        sr, sc = 0, 0

        track = PosTrack(heights)
        self.explore(sr, sc, track)
        
    def explore(self, r, c, track):
        pos = (r, c)
        if track.has(pos) or self.is_out_of_bounds(pos):
            return
        
        track.add(pos)
        
        if r == self.rows - 1 and c == self.cols - 1:
            track.print()
            track.remove(pos)
            return
        
        self.explore(r - 1, c, track)
        self.explore(r + 1, c, track)
        self.explore(r, c - 1, track)
        self.explore(r, c + 1, track)
        
        track.remove(pos)
    
    def is_out_of_bounds(self, pos):
        r, c = pos
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