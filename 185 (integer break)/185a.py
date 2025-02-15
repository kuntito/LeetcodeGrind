# https://leetcode.com/problems/integer-break/description/

class Solution:
    def integerBreak(self, n: int) -> int:
        pass
        # possibly a dynamic programming problem
        # you calculate all the possiblities for every number
        # and memoize it
        # the possiblity range is (1, n//2)
        #
        
        # loop from 1 to n//2
        # for each number, explore `i`
        
        # when exploring `i`
        # you want to do the same thing
        # the base cases are i == 1 and i == 2