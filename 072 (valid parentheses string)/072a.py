# https://leetcode.com/problems/valid-parenthesis-string/description/

# TODO deep solution
class Solution:
    def checkValidString(self, s: str) -> bool:
        pass
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

    

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

