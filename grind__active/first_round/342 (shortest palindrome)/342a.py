# https://leetcode.com/problems/shortest-palindrome/description/


# i want to implement a function that returns a string.
# the function is called, `shortestPalindrome`, it takes one string argument.
# `s`

# the idea is we can prepend `s` with any number of characters to form a new string
# what's the least number of characters we can preprend `s` with to form a palindrome??

# in english, what's the shortest palindrome we can get if we add `0` or more characters to the front of `s`? and return the new string.

# i.e. `prependedChars + s`

# i get the question but my explanation could do with some clarity.
# how would i solve this?

# if `s` is a palindrome, we simply return `s`
# if `s` is not a palindrome? what happens?

# worst case scenario, if i reverse `s` and prepend it to itself
# i'd have a palindrome

# i.e. "meet" reversed is "teem"
# joining them, i'd have "teemmeet"

# i can take this a step further
# if i reversed all but the first character and prepended it
# i.e. "meet" reversed all but one, "tee"
# joining them, i'd have "teemeet"

# this also works
# however, consider
# "acat"

# i could reverse the string and get "tacaacat" which is valid
# i could reverse all but the first and get "tacacat", which is also valid
# or.. 
# i could add a `t` and get `tacat` which is also valid
# the last option would be ideal since it gives the least palindrome
# but i'm not sure what the logic is..

# say i've established `s` is not a palindrome.
# i'd take turns prepending `s` with the last chracter in `s`.

# what does that mean?
# say `s` is "act"

# i'd prepend it with the last character, "t"
# "t" + "act", is "tact" a palindrome, no

# i'd add the next last character, "c"
# "tc" + "act"
# is "tcact" a palindrome? yes.

# this idea seems to work but there should be a simpler way to write it
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        
        prepend = ""
        for lastCh in s[::-1]:
            prepend += lastCh
            newString = prepend + s
            if self.isPalindrome(newString):
                return newString
            
    
    def isPalindrome(self, chars):
        left, right = 0, len(chars) - 1
        
        while left <= right and chars[left] == chars[right]:
            left += 1
            right -= 1
            
        return left > right
    
arr = [
    "abcd",
    "aacecaaa",
]
foo = arr[-1]
sol = Solution()
res = sol.shortestPalindrome(foo)
print(res)