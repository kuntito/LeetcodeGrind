# https://leetcode.com/problems/number-of-1-bits/description/

# i'm given an integer and asked to return it's number of set bits

# in english, if you converted the number to base 2, how many `1`s would it have?
# i imagine Python has a base 2 method, and i can simply count the `1`s 

# but i doubt, that's the approach, the question wants me to take..
# let me do it, confirm it works, then delve into the details
# of what's required of me..
 
# i'd write the base 2 conversion to challenge myself..
# how's it go again..

# you mod a number by 2
# and track the remainders..

# for instance, `n = 3`

# 3 mod 2 = 1
# now n becomes..

# actually, we divmod, not mod..
# you divmod the number by `2`
# the quotient becomes the new number
# the remainder becomes the bits..

# you do this until quotient hits `0`

# for example
# 3 divmod 2 = 1 rem 1, we track, [1], now..
# 1 mod 2 = 0 rem 1, we track, [1, 1]..
# 0 mod 2 = 0 rem 0, we end..

# i believe we reverse the tracking array?
# um.. let me do `2` to confirm..

# 2 divmod 2 = 1 rem 0, track, [0]
# 1 divmod 2 = 0 rem 1, track, [0, 1]
# then we end since n = 0

# yeah, we reverse the bits..
# to be fair, i could do the conversion and only track the `1`s
# better yet, use a counter..

# a counter sum..
# just keep adding the remainders..

# didn't think i'd come up with this..
# but here we are...

# it works but let's see deeply..
 
class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counterSum = 0
        
        while n:
            quo, rem = divmod(n, 2)
            
            counterSum += rem
            n = quo
        
        return counterSum