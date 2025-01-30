# https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/description/

# TODO https://neetcode.io/solutions/maximum-nesting-depth-of-the-parentheses
class Solution:
    def maxDepth(self, s: str) -> int:
        pass
        # loop through `s`, storing each character in an array `arr`
        # append every opening parentheses in the array
        # track it's length in `res`
        # every time you encounter a closing parentheses, pop from `arr`
        # `res` represents the most opening parentheses in the string `s`
        
        res = 0
        count = 0
        for ch in s:
            if ch == '(':
                count += 1
                res = max(res, count)
            elif ch == ')':
                count -= 1
        
        return res
    
    
arr = [
    "()(())((()()))",
    "(1)+((2))+(((3)))",
    "(1+(2*3)+((8)/4))+1",
]
foo = arr[-1]
sol = Solution()
res = sol.maxDepth(foo)
print(res)