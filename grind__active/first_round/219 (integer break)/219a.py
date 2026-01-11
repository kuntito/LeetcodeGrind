# https://leetcode.com/problems/integer-break/description/

# TODO view solution
class Solution:
    def integerBreak(self, n: int) -> int:
        pass
        # it's looking like a dp problem
        # build from the ground up
        # `2` can be split into `1,1`
        # `3` can be split into `1, 1, 1` or `2, 1`
        # `4` can be split into `1, 1, 1, 1` or `1, 1, 2` or `2, 1, 1` or `2, 2`
        # `5` can be split into `1, 1, 1, 1, 1` or `2, 1, 1, 1` or `2, 2, 1`
        
        # for each one determine the maximum product