# https://leetcode.com/problems/regular-expression-matching/

# well, what do we have here?

# we want to write a function that tells if a string, `s` 
# matches a pattern, `p`

# the pattern, `p`, contains three types of characters
# lowercase english letters,
# '.', and
# '*'

# '.' matches any single character
# '*' matches zero or more of the preceeding element

# consider:
# p =  "a"
# s = "aa"

# we want to check the pattern against the string
# the only character in the pattern, `a`
# matches the first character in the string `s`

# however, we must match all characters in `s`
# in this case we would return False since we could only match the first character in `s`

# consider:
# p = "a*"
# s = "aa"

# we want to check the pattern, `p`, against the string, `s`
# p[0] is `a`
# s[0] is also `a`

# that's a match, so we go to the next character in `p`
# p[1] is a `*`
# what this means is this character can represent `0` or more of the previous character.

# which previous character, `p`'s or `s`'s
# it'd have to be `p`'s since we're matching the pattern against the string

# "It is guaranteed for each appearance of the character '*', there will be a previous valid character to match."

# s[1] is `a`

# they certainly match, since the previous char of `p` is `a`

# at this point we've exhausted the pattern and string
# so we return True


# let's consider another example.
# p = ".*"
# s = "ab"

# p[0] is '.'
# this means it can represent any character
# s[0] is 'a'

# since, '.' can represent any character, this is a match

# we proceed.
# p[1] is '*'
# s[1] is 'b'

# in this case '*' represents 0 or more of the previous character
# in this case p's previous character is '.'

# so technically, p[1] == '*' == p[0] == '.'
# since '.' can match any character, it must be a match for s[1]

# again, we proceed
# at this point, we'd have exhausted `p` and `s`
# so we return True

# the examples seem simple enough but with these things
# it's rarely the case

# the tricky bit would be a situation where we don't know how many
# previous characters '*' represents

# in that case, would we have to explore every possibility?

# consider:
# p = "a*c"
# b = "ac"

# in this case, we'd return True
# since `*` represents 0 previous characters

# what about a situation where it represents multiple
# consider:
# p = "a*"
# s = "aaaaaa"

# p[0] == s[0]
# how about p[1], i know it's '*'
# the previous char is 'a'

# `s` is at index `1`
# the idea is,
# for as many consecutive 'a's from s[1] onwards
# i'd start a recursive function call

# where i increment p's index by 1
# and increment the particular s index i'm at by 1

# might need to draw it out


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pass
        self.chars = s
        self.pattern = p
    
        memo = {}
        return self.explore(0, 0, memo)
    
    def explore(self, chIdx, patIdx, memo):
        mitem = (chIdx, patIdx)
        if mitem in memo:
            return memo[mitem]
        
        isExhaustChars = chIdx == len(self.chars)
        isExhaustPattern = patIdx == len(self.pattern)
        
        if isExhaustChars:
            if isExhaustPattern:
                return True
            
            remPat = self.pattern[patIdx:]
            if len(remPat) == 2 and remPat[0].isalpha() and remPat[1] == '*':
                return True
            
        
        
        if isExhaustChars or isExhaustPattern:
            return False
        
        ch = self.chars[chIdx]
        patCh = self.pattern[patIdx]
        
        # three scenarios
        # if `pat` is a period
        # start and return a recursive call with `chIdx + 1` and `patIdx + 1`

        # if `ch` is an alphabet and is equal to `pat`
        # since `ch` is guaranteed to be an alphabet, i only need to check if it equals `pat`
        
        # start and return a recursive call with `chIdx + 1` and `patIdx + 1`
        # else return False
        if patCh == '.' or ch == patCh:
            memo[mitem] = self.explore(
                chIdx + 1,
                patIdx + 1,
                memo
            )
            return memo[mitem]
        
        # in this case, the pattern character is an alphabet
        # and it is not equal to `ch`
        if patCh.isalpha():
            # ideally, we should return False
            # but what if the next pattern is '*'
            # this could mean we're expecting `0`
            # of the current `patCh`
            if patIdx + 1 < len(self.pattern) and self.pattern[patIdx + 1] == '*':
                memo[mitem] = self.explore(
                    chIdx,
                    patIdx + 2,
                    memo
                )
                return memo[mitem]
            
            # if this isn't the case
            # so, return False
            memo[mitem] = False
            return memo[mitem]
            
        
        # if `ch` is an asterisk,
        
        
        # there are three sub scenarios
        # we don't match `ch`, so me move to the next pattern index
        res = self.explore(chIdx, patIdx + 1, memo)
        if res:
            memo[mitem] = True
            return memo[mitem]

        # before moving on to the other scenarios,
        # we want to ensure the previous pattern char
        # can match the current char
        
        # we need the previous char
        prevPat = self.pattern[patIdx - 1]
        
        # if the prevPat is not a match for `ch`
        # return False        
        if prevPat.isalpha() and prevPat != ch:
            memo[mitem] = False
            return memo[mitem]
        
        # at this point the prevPat is either an alphabet that matches
        # or a period
        # at this point, we can assume there is only one match
        
        # prevPat == ch, and move both pointers forward
        res = self.explore(chIdx + 1, patIdx + 1, memo)
        if res:
            memo[mitem] = True
            return memo[mitem]

        # or there is more than one match. i.e. prevPat matches other characters
        # after self.chars[chIdx]

        # we keep the pattern constant and move the char pointer forward
        memo[mitem] = self.explore(chIdx + 1, patIdx, memo)
        return memo[mitem]
        
        
arr = [
    ["aa", "a"],
    ["ab", ".*"],
    ["aaab", "a*b"],
    ["aab", "c*a*b"],
    ["aa", "a*"],
    ["a", "ab*"]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isMatch(foo, bar)
print(res)
        