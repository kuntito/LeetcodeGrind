# https://leetcode.com/problems/palindrome-partitioning-ii/description/

# i want to implement a function called `minCut`.
# `minCut` takes one string argument, `s`, and returns an integer.

# my job is to divide `s` into substrings such that every substring
# is a palindrome.

# i want to find the least amount of divisions to achieve this.
# for example:
# s = "aab"

# i can divide `s` into three substrings
# "a", "a" and "b" and each substrings would be a palindrome

# i can also divide `s` into two substrings
# "aa" and "b", and both substrings would be palindromes

# in this case, the second division is better.
# since i only had to divide `s` once

# so my answer is `1`

# how would i approach this?
# one idea is to start at the beginning of the string
# check every starting string for a palindrome
# if i find one, it means i can divide the string at that point

# so i'd start a-

# looks like i'd need recursion, it'd be a recursive function
# where each time, i check the successive starting substrings for palindromes
# once i find one, i start another recursive call with the rest of the string
# i should pass the number of palindromes found so far

# the base case would be when the string ends
# when `chars == ''`, then i track the number of divisions found
# which would be `numOfPalindroms - 1`

# this way, i'd explore every possible palindrome combination and arrive at the answer
# bit slow, but it should work.

# also, say i don't find a palindrome in a recursive loop
# i just return


class Solution:
    def minCut(self, s: str) -> int:
        pass
        # one base case is when len(s) == 1
        # there are no ways to divide this, so we'd return `0`
        
        # i wrote the base case bit before explaining the recursion
        # from the looks of it the recursion should handle strings
        # with one character
        
        self.minDiv = len(s)
        
        self.explore(s, 0)
        
        return self.minDiv
        
    def explore(self, chars, palCount):
        if not chars:
            divs = palCount - 1
            if divs < self.minDiv:
                self.minDiv = divs
            return
        
        dim = len(chars)
        for idx in range(dim):
            slice = chars[:idx + 1]
            if self.isPalindrome(slice):
                restOfString = chars[idx + 1:]
                self.explore(
                    restOfString,
                    palCount + 1
                )
            
    def isPalindrome(self, chars):
        left, right = 0, len(chars) - 1
        
        while left <= right and chars[left] == chars[right]:
            left += 1
            right -= 1
            
        return left > right
        
        
arr = [
    "aab",
    # "a",
    # "ab",
]
foo = arr[-1]
sol = Solution()
res = sol.minCut(foo)
print(res)
