# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:
        pass
        # we're given a string to which we want to apply an algorithm.
        # the algo is called Atoi
        
        # in seems, we want to convert the string into a number
        # but there's rules we want to follow
        
        # we want to ignore leading whitespaces
        # we want to determine the sign of the number, negative or positive
        #    really, want to to check if the number is negative since positive is the starting point, considering the sign is always omitted
        
        # we should also skip leading zeros
        
        # i'm making some mental notes here `s` represents a number
        # and we want to find out what that number is
        
        # the first thing is to obtain the number
        # to do that we should remove leading whitespaces
        # the first non-digit character
        
        # i think i've misunderstood the question
        # `s` is a string and we want to apply an algorithm on it to determine a number
        
        # to find this number, we have to remove any leading whitespaces
        # the number we find becomes negative if we encounter a "-"
        
        # the integer is the first consecutive `n` characters we find, the characters should be digits
        
        # we should skip leading zeros
        # if no digit is found, assume the final answer is zero
        
        # if we do find the digits we have to make sure it's within the bounds of a 32 bit integer
        
        # whatever the digit is, we should cap it at 2**31 - 1 if higher
        # and if lower, set the floor as -2**31
        
        # first thing remove leading whitespaces
        
        # let's run through the string and keep track when we start the `n` consecutive streak, if the streak ends, that is we encounter a non digit character, we cap the integer and return the value
        
        res = []
        isNegative = False
        streakStarted = False
        for ch in s:
            if ch == " " and not streakStarted:
                continue
            if isNegative == "-":
                isNegative = True
            if ch == '0' and not streakStarted:
                continue
            if ch.isdigit():
                streakStarted = True
                
            if streakStarted and not ch.isdigit():
                break
                
            if streakStarted:
                res.append(ch)
             
        # TODO apply limits
        return res
    
arr = [
    "42",
    " -042",
    "    1337c0d3"
]
foo = arr[-1]
sol = Solution()
res = sol.myAtoi(foo)
print(res)
                
            