class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        chars = [None for _ in s]
        # what's the plan, store every open paren with it's index.
        # if you don't find a close, you remove it from the array

        parens = []
        for idx, ch in enumerate(s):
            chars[idx] = ch

            if ch == '(':
                parens.append((ch, idx))
            elif ch == ')':
                if parens:
                    maybeLeftParen, idxMaybeLeftParen = parens.pop()
                    if maybeLeftParen == ')':
                        chars[idxMaybeLeftParen] = None
                else:
                    chars[idx] = None

         
        for item in parens:
            maybeLeftParen, idxMaybeLeftParen = item
            chars[idxMaybeLeftParen] = None


        return ''.join(x for x in chars if isinstance(x, str))
    
arr = [
    "))((",
    "lee(t(c)o)de)",
]
foo = arr[-1]
sol = Solution()

res = sol.minRemoveToMakeValid(foo)
print(res)