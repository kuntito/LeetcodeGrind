# https://neetcode.io/problems/validate-parentheses

class Solution:
    bracket_map = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    def isValid(self, s: str) -> bool:
        if len(s) == 1: return False

        stack = []
        for idx, ch in enumerate(s):
            if ch in self.bracket_map:
                if not stack or (stack[-1] != self.bracket_map[ch]):
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return len(stack) == 0

foo = Solution()
bar = "([{}])"
bar = "[]"
bar = "(){}}{"

res = foo.isValid(bar)
print(res)