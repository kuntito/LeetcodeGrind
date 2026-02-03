# https://leetcode.com/problems/counting-bits/

from typing import List

# i'm given an integer, `n` and want to return a list of integers

# but what happens in between..
# `n` helps me determine the size of the return array.

# the question says, the return array should be of size `n+1`
# okay..

# for each slot in the return array, let's call the array, `res`
# each slot in `res` has an index

# if `n = 2`
# you'd have an array with the indices.. 0, 1, 2

# for each slot, you want it's value to be the hamming weight of it's index.
# hamming weight is the total number of 1's in the binary representation of a number.

# `2` in binary is `10`
# so it's hamming weight is `1`

# how would this go..
# i could calculate the hamming weight of each number and place in the arrat
# but i imagine, there's a simpler approach to this..

# let me do what i know then look up the solution.

# how do you find the hamming weight..
# a combination of AND and bitwise shift..

# any number ANDed with `1` gives you `1`
# if the rightmost bit of the number is `1`

# once we have that, we shift all bits to the right
# effectively eliminating the rightmost bit
# and replacing it with the next rightmost bit.

class Solution:
    def countBits(self, n: int) -> List[int]:
        return [self.getHammingWeight(i) for i in range(n+1)]
    
    def getHammingWeight(self, n):
        
        count = 0
        while n:
            count += (n & 1)
            n >>= 1
            
        return count