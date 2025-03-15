# https://leetcode.com/problems/build-a-matrix-with-conditions/description/

class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        pass
    
        # determine the row order
        # which numbers need to precede which
        
        # determine the column order
        # which numbers need to precede which
        
        # 1 -> 2
        # 3 -> 2
        
        # the column and row orders should be a reverse relationship
        # 2 -> 1
        # 2 -> 3
        
        # so the lowest guy is the one that doesn't point to anyone
        # it's starting to look like a chronological order problem
        
        # but `2` points to no one
        # so `2` is bottom of the barrel
        # makes sense to place it in the last row
        # above it could either be `1` or `3`
        # since there's no dependency of `1` on `3`