# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/description/


# i want to implement a function that returns an integer.
# the function is called `minSwaps`, it takes a single argument.

# a string called `s`.
# `s` only contians square brackets, i.e. '[' and ']'
# `s` is an even lengthed string. half of it's characters are open square brackets. the other half, naturally, are closed square brackets.

# the brackets can exist within `s` in any particular order
# my job is to find out the minimum swaps it would take to make `s` balanced.

# what that means is, what's the minimum swaps i need to make in `s`
# to ensure every open square bracket has a valid closed bracket.

# an empty string is also classed as balanced.

# consider the example
# s = "][]["

# how would you approach this?
# for one, i know `s` can't start with a closed bracket

# i'd need to swap it with an open bracket
# but which one? there's two of em'

# do i explore both situations?
# i think i'd have to explore both.

# the question's lending itself to backtracking.
# say i explore the first open bracket i find
# i'd have

# "[]]["

# at this point the first character of `s` is valid
# so i'd move to the next, a closed bracket
# this is also valid since right before it is an open bracket

# i think i'd apply the valid bracket algorithm here
# when i encounter an invalid bracket, i know i need to switch with something ahead which opens up another recursive chain.
class Solution:
    def minSwaps(self, s: str) -> int:
        pass



arr = [
    "[]",
    "][][",
    "[[[][[]][[[][][]]]]]",
    "]]][[[",
]
foo = arr[-1]
sol = Solution()
res = sol.minSwaps(foo)
print(res)