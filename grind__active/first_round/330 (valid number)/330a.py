# https://leetcode.com/problems/valid-number/

# i want to implement a function called `isNumber`.
# it takes a string argument, `s` and returns a boolean.

# the boolean indicates whether `s` is a valid number

# but what is a valid number?
# for one, it'd be the digits 0-9

# but things can get complex with the inclusion
# of decimal points, minus or plus signs, and in our case, exponents
# the question considers "2e2.1" as a valid number

# this is the number `2` raised to the power of `2.1`
# the exponents can be represented as 'e' or 'E' followed by an integer number

# and how do i approach this?
# i'm considering splitting the string into two parts
# based on the presence of an exponent

# the first part would be `preExp` and the second part is `postExp`
# what if there are multiple exponents?
# in that case, return False?

# if the split is possible
# i can define helper functions to validate each split


# TODO rewrite the entire thing and critique the edge cases for each criterion
# what makes a valid decimal point?

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.replace("E", "e")
    
        splitChars = s.split("e")
        if len(splitChars) > 2:
            return False
        
        preExp = splitChars[0]
        postExp = splitChars[1] if len(splitChars) > 1 else None
        
        
        isPreExpValid = self.isPreExpValid(preExp)
        isPostExpValid = self.isPostExpValid(postExp)
        
        return isPreExpValid and isPostExpValid
    
    def isPreExpValid(self, chars):
        if chars == '':
            return False
        pass
        # now, how do we ensure the number is accurate
        # let's iterate through the number
        
        # also, if it starts with a plus or a minus
        # the next char must be an integer
        # any other thing is unacceptable
        
        
        plusMinusFound = False
        decimalFound = False
        for idx, ch in enumerate(chars):
            # it can start with an integer, a plus or a minus
            # any other thing is unacceptable
            if ch == '+' or ch == '-':
                # a plus or minus is only valid at the start of the number
                # only one plus or minus is allowed
                if plusMinusFound or idx > 0:
                    return False
                plusMinusFound = True
                
            if ch == '.':
                # a decimal is can only occur once in the number
                # and must have an integer after it
                if decimalFound:
                    return False
                
                nextVal = "" if idx + 1 == len(chars) else chars[idx + 1]
                if nextVal != "" and (not nextVal.isdigit()):
                    return False
                
                decimalFound = True

        return True               
    
    
    
    def isPostExpValid(self, chars):
        # this indicates there's no exponent
        if chars is None:
            return True
        
        # this indicates there's an exponent char `e`
        # but no values after it
        if chars == '':
            return False
        
        plusMinusFound = False
        decimalFound = False
        for idx, ch in enumerate(chars):
            # it can start with an integer, a plus or a minus
            # any other thing is unacceptable
            if ch == '+' or ch == '-':
                # a plus or minus is only valid at the start of the number
                # only one plus or minus is allowed
                if plusMinusFound or idx > 0:
                    return False
                plusMinusFound = True
                
            
            if ch == '.':
                # a decimal is can only occur once in the number
                # and cannot be the first char
                if decimalFound or idx == 0:
                    return False
                nextVal = "" if idx + 1 == len(chars) else chars[idx + 1]
                if nextVal != "" and (not nextVal.isdigit()):
                    return False
                
                decimalFound = True
                
                
        return True
        
arr = [
    ".",
    "-1E+3",
    "3.",
]
foo = arr[-1]
sol = Solution()
res = sol.isNumber(foo)
print(res)