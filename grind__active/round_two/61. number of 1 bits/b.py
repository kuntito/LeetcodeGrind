# https://leetcode.com/problems/number-of-1-bits/description/

# i'm given an integer and asked to return it's number of set bits

# in english, if you converted the number to base 2, how many `1`s would it have?
# i imagine Python has a base 2 method, and i can simply count the `1`s 

# but i doubt, that's the approach, the question wants me to take..
# looking at a previous solution..

# the answer was a combination of using the `AND` bitwise operator
# and a bit shift

# any integer `AND`ed with `1`
# returns the that integer's right most bit..

# consider:
# n = 2
# in binary `2` is `10`

# and when you do `2 AND 1`
# you get `0` 

# that's where the bit shift comes in..
# `>>` allows us to remove the rightmost bit from any number

# we know `2` is `10`
# if we did `2 >> 1`, this means remove `1` rightmost bit..
# we'd get `1` 

# if we did `2 >> 2`, this means remove `2` rightmost bits..
# and we'd be left with zero..

# so.. if we keep ANDing by `1`
# we can count the number of `1` bits
# and we can keep shifting rightwards till we run out..

# problem solved...

 
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counterSum = 0
        
        while n:
            counterSum += (n & 1)
            
            n >>= 1
            
        return counterSum
    
