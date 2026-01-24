# https://leetcode.com/problems/sqrtx/description/

# i'm given a non-negative integer, `x`
# in clearer terms, x >= 0
# i'm asked to find the square root of `x`
# without using built-in functions..

# let's see.. what do i know about square root..
# the square root of `x` is a number, let's call it `num`
# the square root of `x` is a number when multiplied by itself
# results in `x`

# i.e. `num * num == x`
# okay but how do i find this.. not sure

# another intuition i have is.. the square root of any number
# is at most half of the number, because once if a root exceeds half of it's parent
# if it's multiplied by itself, it must be greater than.. the parent..

# to be fair, i think `4` is the only case where the square root is half..
# every other number has their square root smaller than half..

# the question also, said we only want the integer part of the square root
# i.e. if the root is 2.14, we return `2`

# off the dome.. i'm thinking..
# the square root must exist between `0` and half of the number

# we don't know what it is, but we know one thing..
# i'm not sure how to derive the intuition.. but binary search can work here..

# if i pick the middle number, and check if when multiplied by itself, `midNum * midNum`, results in `x` or something close...

# the something close is what's tricky.. say `x` is `10`
# it's root is 3.16..
# if we do binary search and get `3`, the square is `9`

# if we go higher, and hit `4`, the square is then `16`
# so we're looking for a midNumber where the previous midNumber is less than target..

# let's try ..
# i think absolute difference can help here..
# for each mid number we explore..

# we find it's square..
# we also find the square of it's left and right neighbours..
# if that mid numbers square is the closest to `x`
# then we've found our solution..

# if the right num, has the less absolute difference, we move there..
# what am i talking about..
# if you square mid number, it's one of three things:

# equal to `x`
# greater than `x`
# smaller than `x`

# if the square is equal to `x`, return mid number
# the the square is greater than `x`
# we compare the abs difference between mid number and the number before it..
# if mid number's square is closer to `x` than the number before mid number
# then mid number's square is the closest we'd get to `x`
# return mid number.. if not, continue the binary search..

# now if mid number's square is less than `x`
# compare the abs difference between mid number's square
# and the square of (mid number + 1)
# if mid numbers abs difference is closer to `x`
# then mid number is the closest we'd get to `x`
# return mid number..

# i notice, my writing's not the clearest..
# the abs difference is between midNumber's square and `x`
# i.e. absDiff(midNumber**2 - x)

# actually, what am i talking about..
# if midNumber's square is greater than `x`
# we should always go back..

# actually, if our search window is from 
# 0 to the middle of `x`
# we would never find a mid number whos square is greater than `x`
# it's either equal to `x` or less
# in which case, if less, the natural instinct is to move the mid pointer forward

# but we then compare mid number and mid number + 1
# if mid number's square has the best absolute difference with `x`
# then mid number is the closest we'd get to `x`

# you don't even need absolute difference..
# just difference.. `x - midSquare`

# actually, i'm capping..
# midSquare can actually become greater than `x`

# the statement, the square root can never exceed half of the number is True
# but it doesn't mean half of a number, when squared, can not exceed the number

# consider, x = 10
# x // 2 = 5
# the square root of 10 is `3.16`. so, this follows, the square root doesn't exceed `5`
# but the square of `5` exceeds `10` so.. back to the drawing board..  
# if midSquare is greater than `x`
# we're definitely moving the right pointer towards the left..

# if midSquare is smaller, we check if the next num's square is greater than `x`
# if yes, then the current number is our solution

# made an error, didn't consider when x is 1 or when x is 0
# also another error with the check
# i'd done if midSquare  == x or nextNumSquare > x: return x
# the first part of the condition is valid
# but the next part should be if `midSquare is less than x` and the
# next number square is greater than `x`
# then we have our solution..

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1: return x

        left = 0
        right = x // 2
        
        while left <= right:
            midNum = left + (right - left)//2
            
            midSquare = midNum ** 2
            nextNumSquare = (midNum + 1) ** 2
            if midSquare > x:
                right = midNum - 1
            elif midSquare == x or nextNumSquare > x:
                return midNum
            else:
                left = midNum + 1
