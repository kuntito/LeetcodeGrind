# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

# i want to implement a function, `minRemoveToMakeValid`.
# this functions takes a string argument and returns a string.

# the input string `s` contains lowercase english characters and parentheses, '(' and ')'.

# a sample input is "lee(t(c)o)de)"
# as you can see the characters and parentheses are interspersed

# but our concern, really, are the parentheses
# we want to know if they're valid
# if not, what's the least amount of parentheses we can remove to make them valid.

# if we extract them from the sample, 
# we get "(()))"

# it's immediately clear, there's an extra closing parentheses
# ergo, we can remove any one of them.

# ccording to the question, it doesn't matter which one we remove.
# our return string is the input string minus the selected parentheses.

# it's also possible the parentheses are balanced.
# that means, we wouldn't remove anything, and would return the input string as is.

# it's become clear that i should isolate the parentheses
# so i can focus on making them valid
# since, i'd be removing the invalid parentheses from the input string
# it makes sense to isolate the parentheses with their indices

# this way, i'm in better position to remove them from the input string.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        parens = self.extractParentheses(s)
        print([x for x, y in parens])
        
        # now that i have the parentheses
        # how do i know, which is invalid.
        
        # the rule is every opening must have a closing
        # moving left to right in a string
        # the furthest open paren would pair with the earliest closing.
        
        # once, we match a pair
        # they're valid and so we examine the next
        
        # consider "(()))"
        # i'd match the inner pair first
        # i'd be left with "())"
        # then match the next pair
        
        # and be left with ")"
        # no more matches, so i know i have to remove this one
        # since, i have the index, it makes things simpler
        
        # let's examine a different pairing
        # ")()"
        # this case, i'd remove the first pair
        # furthest open, earliest close
        # and be left with ")"
        
        # still works, what if there's no pair
        # i.e. "))(("
        # my assumption fails here
        # because i can't pair the furthest open with the earliest close
        # since the earliest close comes after the furthest open
        
        # the better assumption is the first valid pair
        # is the furthest open and the next close.
        
        # i think the stack approach works best
        # where i put all the opens in a stack
        # the moment i find a close, i pop the open from the stack
        # i keep doing this till i exhaust the array.
        
        # any opens left at the end of the iteration must be invalid
        # same vein, if i find a close without an open, i'd also remove it
        
        # that said, i might not need extract parenthese.
        # i could iterate through the input in one go
        # tracking the opens and their indices
        # popping the matching ones
        # if i encounter a close without an open
        # i can add it to an array, `closesToRemove`
        
        # at the end of the iteration
        # i'd rebuild the input string by ignoring any leftover opens
        # and any element of `closesToRemove`
        
        closesToRemove = []
        opensToRemove = []
        
        for idx, ch in enumerate(s):
            if ch == '(':
                opensToRemove.append(idx)
                
        
        
    def extractParentheses(self, chars):
        parens = []
        for idx, ch in enumerate(chars):
            if ch in ('(', ')'):
                parens.append((
                    ch,
                    idx,
                ))
                
        return parens
    
arr = [
    "lee(t(c)o)de)",
]
foo = arr[-1]
sol = Solution()
res = sol.minRemoveToMakeValid(foo)