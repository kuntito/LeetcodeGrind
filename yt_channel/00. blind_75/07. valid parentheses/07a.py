# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        pass
        # every open must close
        # every close must have an open
        # and the open close order must be maintained
        # you can't have `[')', '(']`
        
        # insight 0:
        # the ending parentheses must be a pair?
        # cap!
        # "()[]{}"
        
        # let's work backwards
        # the solution works by identifying the first connecting pair
        # the proceed with throat cut procedures
        
        # say we have a couple of open parentheses
        # [(, (, (, (, ), ), ), )]
        # if the input is valid,
        # one thing is certain, the parentheses would close at some point
        
        # ****************
        
        # keep a dictionary to pair opens and closes
        parens = {
            ')' : '(',
            ']' : '[',
            '}' : '{',
        }
        
        arr = []
        for ch in s:
            if ch in parens:
                # since we paired `closing -> opening`
                # it means `ch` is a closing
                # in other words, the golden rule is that 
                # for a valid set of parens, 
                # every closing must be preceeded by it's corresponding open
                
                # since we've tracked all the opens so far
                # we can simply check if the previous value in `arr` is the corresponding open
                # if it is, we remove it from the stack
                # and if it isn't, it means the `parens` are invalid
                # so we can return `False`
                
                # since we've matched closes to opens
                # we can get the open for `ch` by using the hashmap
                # but what if the array is empty? use `arr and arr[-1]...`
                if arr and arr[-1] == parens[ch]:
                    arr.pop()
                else:
                    return False
            else:
                # we track all the opens
                arr.append(ch)
                
        # if we've done our job right, we should have popped all the valid opens
        # not necessarily, consider:
        # `[(,), (]`
        
        # in this case `arr = [(]` at the end of the iteration
        # heck we could have multiple opens at the end
        # since the opens are only popped when we find a close
        
        # in this case, our return value should be whether `arr` is empty
        
        return not arr
        
        