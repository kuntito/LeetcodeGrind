# https://leetcode.com/problems/single-number/

from typing import List

# i'm given an array of integers, `nums`
# where every element appears twice except one number

# i'm post to find this number
# and return it.

# i should do this in O(n) runtime and O(1) space
# i'm just going to jump to the solution

# i know this is a bit manipulation question
# and the solution i'm aware of requires me to know something about XOR..

# right, the trick is.. i don't know if you can call it a trick but..

# if you XOR two equal numbers together you get `0`
# i.e. 3 XOR 3 = 0

# secondly, if you XOR any number with `0`, you get that number back.
# i.e. 3 XOR 0 = 3

# this way, since we know every number except one has a duplicate..
# if we XOR all the numbers, the duplicates will cancel each other out to `0`
# which would leave us with `0` and the target number

# if we XOR the target number with `0`
# we get the target number, problem solved.

# if Python, XOR is ^ 

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        res = 0
        
        for n in nums:
            res ^= n
            
        return res