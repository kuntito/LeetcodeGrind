# https://leetcode.com/problems/repeated-substring-pattern/


# i want to implement a function, `repeatedSubstringPattern`, that takes a string
# and returns a boolean.

# what happens in between is we find out if the string `s` can be broken into multiple
# parts where every part is the same.

# for example: "abab" can be broken into "ab" and "ab"
# each part is a substring of `s`

# one intuition is, the substring, if it exists, must start `s`
# in other words, i can continuously pick each character that starts `s`
# and ask, is `s` made up of multiples of this?

# the questions would look like:
# is `s` made up of multiple `s[0]`?
# is `s` made up of multiple `s[:2]`?
# is `s` made up of multiple `s[:3]`?

# the question now becomes, given a `substring`
# how do i find out, if the rest of `s` is made up of multiples of `substring`

# the simpler way to look at this is the `substring` must start the rest of the string
# using recursion, i can keep passing the substring and the rest of the string
# until i either exhaust the string or find out the substring no longer matches the start of the string.


import math

# TODO failed the testcase "a", why?
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        pass

        # so how do i grab each substring
        # i only need to iterate to the middle of `s`
        dim = math.ceil(len(s) / 2)
        for idx in range(dim):
            endSlice = idx + 1
            substring = s[:endSlice]
            if self.explore(substring, s[endSlice:]):
                return True
            
        return False

    def explore(self, substring, chars):
        # this would check is `substring` starts chars
        # if yes, explore substring and the rest of chars

        # if chars is empty, we've hit jackpot
        if chars == "":
            return True

        return chars.startswith(substring) and self.explore(
            substring, chars[len(substring) :]
        )

arr = [
    "abab",
    "abcabcabcabc",
    "aba",
]
foo = arr[-1]
sol = Solution()
res = sol.repeatedSubstringPattern(foo)
print(res)