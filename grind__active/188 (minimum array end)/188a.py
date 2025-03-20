# https://leetcode.com/problems/minimum-array-end/description/

# TODO
# https://neetcode.io/solutions/minimum-array-end
# 04:00
class Solution:
    def minEnd(self, n: int, x: int) -> int:
        pass
        # to get the result
        # we determine the bit structure of `x`
        
        # for `n` numbers to be ANDED to form `x`
        # it means for each of those `n` numbers
        # they need to have a `1` bit in the same position as `n`s 1 bits
        # and for the other positions, there must be at least one differing bit
        
        # for example, if `n` is `3`
        # in binary, that's `011`
        
        # all three numbers need ...