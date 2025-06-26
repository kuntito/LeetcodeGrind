# https://leetcode.com/problems/basic-calculator/

# i want to implement a function that returns an integer.
# the function is called calculate and takes a single argument, 
# a string, `s`.

# `s` represents a valid arithmetic expression.
# i.e.
# "1 + 2" 
# -2+(3x5)

# my job is to solve this expression and return the result

# how do i approach this
# the way i see it, the smallest arithmetic expression has three parts.
# left operand, operator and right operand

# using PEMDAS, i'd identify all first set of expressions, solve them
# and replace them in the string with their result

# i.e. s = "2+3*5"
# the first expression is "3*5"
# which results to "15"

# now, i'd replace "3*5" with "15" in `s`
# which results in 2+15
# and this is another arithmetic expression.

# i'd recursively apply the same method till i obtain a single digit
# based on the constraints, we don't need the `E` in PEMDAS
# which means we'd work with PMDAS

# first, we need to find the smallest parentheses
# and solve for the expression within it

# once solved, we explore for all the multiplications
# what if you had 2*3*5

# the first multiplication expression would be 2*3
# if i replaced this with `6`



class Solution:
    def calculate(self, s: str) -> int:
        pass