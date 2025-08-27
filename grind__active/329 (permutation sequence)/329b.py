# https://leetcode.com/problems/permutation-sequence/description/

# want to implement a function that takes two arguments.
# the first argument, `n`, is the first one we'd discuss.

# `n` is an integer that's less than or equal to `9`

# to understand our task, i'd use an example.
# let's say `n` is `3`
# we want a string containing numbers from `1` up to `n`
# in our case, the string would be "123"

# this is the starting string, let's call it `stringOne`
# we now want to find all possible permutations of this string.
# and we want to do it in order.

# what would this look like:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

# working backwards, the order demands the first character follows the order of numbers in the starting string, "123"
# so we start with:

# "1" and we're left with "23"
# after picking the first character, what else

# at this point, "23" is the main string
# we want to pick the first character of the main string
# in this case "2" and we're left with "3"

# "3" becomes the main string
# in this case, we pick the first character, "3" and we're left with nothing

# TODO see thought train



class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        pass