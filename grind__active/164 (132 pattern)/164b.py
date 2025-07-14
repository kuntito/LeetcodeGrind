# https://leetcode.com/problems/132-pattern/description/

# `find132pattern` is a function, takes an array of numbers, `nums`
# and returns a boolean.

# but what happens in between? what we want is to find if the array contains
# a 132 pattern and what is a 132 pattern you say?

# consider three indices, `a`, `b` and `c`
# a 132 pattern is a subsequence of three integers, `nums[a]`, `nums[b]`, `nums[c]`

# where the middle number, `nums[b]` is the biggest
# the left number,`nums[a]` is the smallest
# leaving `nums[c
# 
# let's rewrite this
# consider three indices, 0, 1, 2

# they appear in increasing order
# and their elements are `elemZero`, `elemOne`, and `elemTwo`
# such that the biggest of these elements is `elemOne`

# the smallest of these elements is `elemZero`
# leaving `elemTwo` as the middle element

# hence, the term, `132`
# biggest element in the middle

# for example,
# nums = [3, 1, 4, 2], would return True
# the 132 pattern here is in `[1, 4, 2]`

# but the numbers don't have to be consecutive
# nums = [1, 3, 4, 2], would also return True
# and the 132 pattern would remain `[1, 4, 2]`

# in a sense, the question we want to ask for at every index is
# what's the largest number on right that's less than you?
# we'd call that `largestRight`

# now, we need a number on the left
# that is less than `largestRight`
# we can call that `largestLeft`

# once we can find a number on both sides
# problem solved.

# as far as the left side is concerned, i only need the smallest number
# i can simply track the smallest number ever seen
# and ensure it's less than `largestRight`

# but how would i have find `largestRight`, i can't just store the highest number seen
# since i want to cap it at the `current number - 1`

# not sure a bruteforce is helpful, i could try it out then simplify

class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        pass
    
        lowestEver = float("inf")
        
        for idx, n in enumerate(nums):
            lowestEver = min(n, lowestEver)
            
            # TODO this function should return the largest number in the range
            # [idx + 1: ] that's less than `n`
            largestRight = self.getLargestRight(n, idx + 1, nums)
            
            if lowestEver < largestRight:
                return True
            
        return False