# https://leetcode.com/problems/longest-valid-parentheses/description/

# i want to implement a function, `longestValidParentheses`, 
# that takes a single string argument, `s`

# `s` contains just the characters '(' and ')'
# my job is to return the length of the longest well-formed parentheses

# consider:
# s = (()
# the result would be `2`
# since the longest well-formed parentheses is `s[1:] = ()`


# how do i approach this?
# i'd iterate through `s` with index
# for every opening parenthesis,
# i'd explore it further using a helper function

# this function returns the longest parentheses starting at 
# the index of the openining parenthesis
# and i'd track the longest seen

# it seems there'd be an opportunity for memoization
# however, i'd write the bruteforce first then optimize


# this example invalidates my approach
# "()(()",

# in this case, i'd track the array would look like this
# ["("], i'd add an open
# [], since i found a close and popped the last open
# ["("], i'd add an open
# ["(", "("], i'd add another open
# ["("], i'd find a close and pop the last open

# the problem here is my validCloses is `2`
# but the longest valid parentheses isn't `2*2 = 4`

# the longest valid parentheses is not a measure of how many valid closes
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        maxLen = 0
        for idx, ch in enumerate(s):
            if ch == '(':
                resLen = self.explore(idx, s)
                if resLen > maxLen:
                    maxLen = resLen
                    
        return maxLen
    
    def explore(self, startIdx, chars):
        pass
        # what does a valid parentheses look like?
        # every opening has a closing
        
        # i'd iterate through `chars`
        # storing every opening parenthesis in an array, `arr`
        # for every closing parenthesis, a prior opening parenthesis must exist in `arr`
        
        # if no such parenthesis exist, then that closing parenthesis is invalid
        
        # the loop would have to end there
        # but this doesn't tell me how long the valid parenthesis is?
        
        # consider:
        # ((())
        # in this case, i'd have 3 opens but only
        # two of them get closed
        
        # in other words, i'd track the max opens found
        # and track the valid closes found
        
        # maxOpens - validCloses-
        # actually, i only need to count valid closes
        # is that so?
        
        # yes, it is so.
        # validCloses times 2 is the length of the longest parentheses starting at `startIdx`
        
        validCloses = 0
        arr = []
        dim = len(chars)
        for idx in range(startIdx, dim):
            ch = chars[idx]
            if ch == '(':
                arr.append(ch)
            else:
                if not arr or arr[-1] == ')':
                    break
                arr.pop()
                validCloses += 1
            
        return validCloses * 2

arr = [
    "",
    "(()",
    ")()())",
    "()(()",
]
foo = arr[-1]
sol = Solution()
res = sol.longestValidParentheses(foo)
print(res)