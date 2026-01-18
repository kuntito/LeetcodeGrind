# https://leetcode.com/problems/unique-paths-ii/description/

from typing import List

# i'm given a grid, 
# starting at `top left`, i want to find the unique paths i can take to `bottom right`

# the caveat is, the grid cells contain obstacles, each grid cell is either `0` or `1`
# the `1`s are the obstacles, the `0`s are free space.

# a path is only valid if it contains no `1`s.

# and i can only move down or right..

# every cell, i'm doing the same thing, down or right.
# hence, recursion..

# at each recursive call, what am i doing?
# i'm starting two new calls.. the down path and the right path..
# and when they return..

# what are they returning..
# each call returns the number of unique paths it would take from itself to `bottom right`

# so, i'd have to sum up the `downCount` with `rightCount`

# seems simple enough..
# base case..
# if you hit `bottom right`
# if you go out of bounds or hit an obstacle..

# memoize, definitely.. since at each cell, we do the same thing..
# we can memoize it's result, so we don't have to re-do it

# what do i want to return at base case..
# since, i'm collating the number of ways..
# if i hit base case, bottom right, i should return `1`
# if i go out of bounds or hit an obstacle, i should return `0`

# as is, it fails 
# `[
#   [0,0],
#   [0,1]
# ]`

# i don't know how to feel about this.. the edge case is that
# bottom right is an obstacle, so we can't reach it..
# to solve this, when i compare current position with bottom right,
# i added a check to ensure `bottomRight == 0`

# i guess, i should consider this.. they did say any grid cell can be `0` or `1`
# that said, how does my code pass the edge case where the origin is an obstacle

# oh, i already return `0` if the current position is an obstacle.


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.grid = obstacleGrid
        self.rows, self.cols = len(obstacleGrid), len(obstacleGrid[0])
        
        origin = (0, 0)
        memo = {}
        return self.explore(origin, memo)
    
    def explore(self, pos, memo):
        r, c = pos
        if r == self.rows - 1 and c == self.cols - 1 and self.grid[r][c] == 0:
            return 1
        
        if r < 0 or r == self.rows or c < 0 or c == self.cols or self.grid[r][c]:
            return 0
        
        if pos in memo:
            return memo[pos]
        
        rightCount = self.explore((r + 1, c), memo)
        downCount = self.explore((r, c + 1), memo)
        
        totalPathsHere = rightCount + downCount
        memo[pos] = totalPathsHere
        
        return memo[pos]
    
arr = [
    [[0,0],[0,1]],
    [[1, 0]],
]
foo = arr[-1]
sol = Solution()
res = sol.uniquePathsWithObstacles(foo)
print(res)