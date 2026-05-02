# https://leetcode.com/problems/parsing-a-boolean-expression/description/

class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        if len(expression) == 1:
            return True if expression == 't' else False
        
        # now i want to find the innermost parenthesis.
        # how do you define this?
        
        # it doesn't necessarily have to be the innermost one
        # it has to be the one that can be resolve first.
        # consider (t)((f))
        # the innermost one is the one with the `f`
        # but (t) can be resolved first and so..
        # i just need to resolve the first opening paren i can close.
        
        # i'd use a stack to track opening indices
        # and the first close i find, i resolve.
        
        # another concern is, you're not just tracking openings.
        # you might want to track the open and the char before it
        # if the char before is !, | or &
        
        # so, on each pass, what i'm tracking in the stack
        # is the indices of opening parens
        # or any of the paren modifiers: !, | or &
        
        dim = len(expression)
        
        # TODO how do you track the bare opens and the opens with modifiers?