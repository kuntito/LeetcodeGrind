# https://leetcode.com/problems/wildcard-matching/

# i want to implement a function, `isMatch`,
# that takes two string arguments, `s` and `p`

# `s` contains only lowercase english letters
# while, `p` contains lowercase english characters and two special characters,
# '?' and '*'

# `p` represents a pattern
# and my job is to return a boolean that tells us
# if the string `s` matches the pattern `p`

# what the special characters in `p` mean are:
# '?' matches any single character
# '*' matches any sequence of characters including an empty sequence

# the idea is to ensure every character in `s`
# follows the pattern sequence in `p`

# meaning i'd have to iterate through `s`
# and ensure it matches `p`

# if i reach the end of `s` and exhaust `p`
# i return True

# any other outcome, i return False

# so how do i solve it
# i'd compare the first characters in `s` and `p`
# if they are the same, i'd move on to the next characters in both strings

# this seems right until you think about it
# consider:
# s = "ab" and p = "ab"
# in this case, comparing each character works
# "a" maps to "a"
# "b" maps to "b"

# what about
# s = "aa" p = "*"
# in this case, the first characters would be
# "a" and "*"

# the wildcard "*" can mean 0 or more characters
# how then would i know if how many characters i'm matching
# might just have to explore all the possibilities

# but what would that look like?
# for zero matches, 
# i'd be mapping "a" => ""

# in this case the exploration can't proceed
# because the characters don't match

# what about matching one character
# "a" => "*"
# in this case the exploration can proceed
# i'd move to the second "a" and i'd exhaust `p`
# in this case the exploration also ends
# since i exhausted `p` and still have `s`

# the third case, i'd match two characters
# "aa" => "*"
# by proceeding, i'd exhaust `s` and exhaust `p`
# and return True

# via this explanation, there's the repeated logic
# of comparing two characters from both strings
# and moving forward

# it lends itself naturally to recursion
# where i can pass the character indices as function arguments
# and proceed from there

# ["aa", "*"], TODO why does this fail?

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
        self.ess = s
        self.pee = p
        
        return self.explore(0, 0)
        
    def explore(self, essIdx, peeIdx):
        isExhaustEss = essIdx == len(self.ess)
        isExhaustPee = peeIdx == len(self.pee)
        if isExhaustEss and isExhaustPee:
            return True
        
        if isExhaustEss or isExhaustPee:
            return False
        
        uno, dos = self.ess[essIdx], self.pee[peeIdx]
        
        if dos.isalpha():
            if uno == dos:
                self.explore(essIdx + 1, peeIdx + 1)
            else:
                return False
        
        
        if dos == '?':
            self.explore(essIdx + 1, peeIdx + 1)
        
        # explore `0` matches
        if self.explore(essIdx, peeIdx + 1):
            return True
        
        return self.explore(essIdx + 1, peeIdx)
    
arr = [
    ["aa", "a"],
    ["cb", "?a"],
    ["aa", "*"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isMatch(foo, bar)
print(res)
        
        