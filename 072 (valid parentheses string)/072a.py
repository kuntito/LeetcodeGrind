# https://leetcode.com/problems/valid-parenthesis-string/description/


class Solution:
    def checkValidString(self, s: str) -> bool:
        pass
        # create one stack of size len(s)
        # iterate through `s` with index starting from behind
        # for each index `idx`, store the amount of closing parentheses seen and the amount of asterisks seen (cl, ast)
        
        # iterate through `s` from the start,
        # for every opening seen

    

arr = [
    "(**()",
    "((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()",
    "**************************************************))))))))))))))))))))))))))))))))))))))))))))))))))",
    "************************************************************",
    "**((**"
]
foo = arr[-1]
sol = Solution()
res = sol.checkValidString(foo)
print(res)

# chars = "(((((((((((((((((((((((((((((((((((((((((((((((((())))))))))))))))))))))))))))))))))))))))))))))))))"
# res  = sol.validate(chars)
# print(res)

