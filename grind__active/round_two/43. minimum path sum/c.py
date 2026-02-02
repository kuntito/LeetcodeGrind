# https://leetcode.com/problems/minimum-path-sum/

from typing import List

# right, remind me what we doing?
# you have a grid of integers, all greater than or equal to `0`

# you start at topLeft and want to reach bottomRight
# you want to find the lowest path sum..

# path sum is the sum of all the cells along the path you took
# from `topLeft` to `bottomLeft`

# 'pparently, this can be solved using dynamic programming
# at every point in the cell, we're asking one question.

# am i better off going right, or going down.
# it's also sounding like recursion.

# each point's result is determined.
# which ever path is less.

# ultimately, we'd explore until we go out of bounds.
# when we do, the sum of the out of bounds cells is `0`

# i wonder if the recursion is better than 
# the down to up iteration neetcode suggested

# TODO, i think you have an approach here, 
# but it currently doesn't check if each path reaches bottomRight
# i'm not sure what it's doing..
# but fix it then compare with neetcode's down to up approach

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        return self.explore(0, 0, grid, memo)
    
    def explore(self, r, c, grid, memo):
        mitem = (r, c)
        if mitem in memo:
            return memo[mitem]
        
        rows, cols = len(grid), len(grid[0])
        if r < 0 or r == rows or c < 0 or c == cols:
            return 0
        
        val = grid[r][c]
        
        right = self.explore(r, c + 1, grid, memo)
        down = self.explore(r + 1, c, grid, memo)
        
        memo[mitem] = val + min(right, down)
        
        return memo[mitem]
        

    
arr = [
    [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ],
]
foo = arr[-1]
sol = Solution()
res = sol.minPathSum(foo)
print(res)