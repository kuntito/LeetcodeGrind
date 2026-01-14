# https://leetcode.com/problems/unique-paths/description/

# i'm given a grid, `rows x columns`
# a robot, starts at (0, 0), first row, first column
# and wants to get to last row, last column..

# the robot can only move right or down at any time..
# how many unique ways can the robot get from (0, 0) to (rows-1, columns-1)

# this is basically `climbing stairs`, at least the pattern..
# at each point in the grid, there's two paths..
# move down, or move right.. whichever one you take, you're faced with the same situation
# move down, or move right.. that's recursion right there..

# the path that moves right, then down, ends up in the same place as
# the path that moves down, then right,.. that's memoization right there..

# the base case would going out of bounds
# or hitting (rows-1, columns-1)

# if we go out of bounds, we stop exploration, return 0
# if we hit base case, return `1`, collate the scores in the parents..
# memoize, return the value

# oh, and what are we memoizing? the grid position, the row and the column
# usually, i use a tuple (r, c), since it's immutable..
# could use a string f"{r}-{c}", whatever works best.. i'll try both
# see which is faster..

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.memo = {}
        self.rows = m
        self.cols = n
        return self.explore(0, 0)
        
    def explore(self, r, c):
        mitem = (r, c)
        if mitem in self.memo:
            return self.memo[mitem]
        
        if r == self.rows or c == self.cols:
            return 0
        
        if r == self.rows - 1 and c == self.cols - 1:
            return 1
        
        pathOne = self.explore(
            r + 1,
            c,
        )
        
        pathTwo = self.explore(
            r,
            c + 1,
        )
        
        self.memo[mitem] = pathOne + pathTwo
        return self.memo[mitem]