# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

from typing import List

# what's the situation here?
# i'm given a 2d grid, `matrix`

# of dimensions `m` rows by `n` columns

# from each cell in the grid, i can move:
# up, down, left and right..

# while doing so, i want to find the length
# of the longest increasing path within the grid.

# and how would this work?
# the longest increasing path has to start at a particular cell.

# okay.. but how do we find that cell?
# we check every cell.

# right, and at each cell, what are we doing..
# explore all four directions if increasing..
# each direction is it's own recursive call

# each returning their longest increasing path
# the longest one is what we're concerned with.
# way i see it, we can cache the result from each cell

# (r, c) => longestPathFomCell

# this way, if we iterate through the grid
# we can determine the longest increasing path.

# and how would the recursion go..
# well, you'd pass
# rowIdx, colIdx
# valueOfParent
# cache

# at each call, 
# if current value is less than or equal to valueOfParent
# return 0

# error, the first exploration.. should have a really small parent value.
# so it classes the first exploration as an increasing path
# even if it technicall doesn't have a parent.

# as the code is written, i pass the valueOfParent as the same value at `[ri][ci]`
# and the function would rightly class this as an invalid exploration

# so, `float("-inf")` should be the default `valueOfParent` for every first exploration

# another error, i accessed `self.matrix[ri][ci]` before i checked for out of bounds..
# i'd initially placed the access after `ri < 0 or ri == rows.. ` check.

# however, i later realized, i had to reuse the current value, so i thought to extract
# into a variable not realizing.. extracting it, meant i needed to separate it from
# the existing boolean check.

# it works.. my first hard in less than 30 mins.

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        pass
        self.matrix = matrix
        cache = {}
        
        longestIncrPath = 0
        
        for ri, row in enumerate(matrix):
            for ci, val in enumerate(row):
                exploreRes = self.explore(ri, ci, float("-inf"), cache)
                
                longestIncrPath = max(
                    longestIncrPath,
                    exploreRes
                )
                
        return longestIncrPath
    
    def explore(self, ri, ci, parentVal, cache):
        rows, cols = len(self.matrix), len(self.matrix[0])
        is_out_of_bounds = ri < 0 or ri == rows or ci < 0 or ci == cols
        
        if is_out_of_bounds:
            return 0
        
        currentVal = self.matrix[ri][ci]
        if currentVal <= parentVal:
            return 0
        
        mitem = (ri, ci)
        if mitem in cache:
            return cache[mitem]
        
        downRes = self.explore(ri + 1, ci, currentVal, cache)
        upRes = self.explore(ri - 1, ci, currentVal, cache)
        rightRes = self.explore(ri, ci + 1, currentVal, cache)
        leftRes = self.explore(ri, ci - 1, currentVal, cache)
        
        resHere = 1 + max((downRes, upRes, rightRes, leftRes))
        cache[mitem] = resHere
        
        return cache[mitem]
    
arr = [
    [[9,9,4],[6,6,8],[2,1,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.longestIncreasingPath(foo)

print(res)