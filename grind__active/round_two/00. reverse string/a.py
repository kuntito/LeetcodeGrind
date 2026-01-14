# https://leetcode.com/problems/reverse-string/description/

# we're given an array of characters
# we want to reverse the order of said characters without creating a new array

# we're guaranteed, the array has at least one element.
# i'm thinking two pointers

# `left` and `right`
# start at opposing ends of the array `s`
# they move towards each other, swapping their values until the pointers
# meet or go out of bounds.

# [1, 2, 3, 4, 5]
#  L           R
# they swap values, it becomes 
# [5, 2, 3, 4, 1]
#  L           R
# they move closer
# [5, 2, 3, 4, 1]
#     L     R
# swap again
# [5, 4, 3, 2, 1]
#     L     R
# move closer again
# [5, 4, 3, 2, 1]
#       LR
# now, they've met so no more swapping..

# if the array was an even number, the pointers would cross
# i.e. 
# [4, 3, 2, 1]
#     R  L

# hence, the check would be if left < right
# once we've reversed, we can concatenate the string.

class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1
        
        while left < right:
            s[left], s[right] = s[right], s[left]
            
            left += 1
            right -= 1
            
            
        return "".join(s)