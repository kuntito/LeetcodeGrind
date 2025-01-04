# https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int):
        self.res = []
        self.n = n

        self.explore(['('], 1, 0)

        return self.res
    

    def explore(self, chars, left_count, right_count):
        if left_count == right_count and left_count == self.n:
            if self.is_valid(chars):
                self.res.append(''.join(chars[::]))
            return
        if left_count > self.n or right_count > self.n:
            return
    
        chars.append('(')
        self.explore(chars, left_count + 1, right_count)
        chars.pop()

        chars.append(')')
        self.explore(chars, left_count, right_count + 1)
        chars.pop()


    def is_valid(self, s: list) -> bool:
        parens = {
            '}' : '{',
            ')' : '(',
            ']' : '['
        }

        arr = []
        for ch in s:
            if ch in parens:
                if not arr or arr.pop() != parens[ch]:
                    return False
            else:
                arr.append(ch)

        return len(arr) == 0
    

arr = [
    2,
    3,
    4,
]

foo = arr[-1]
sol = Solution()
res = sol.generateParenthesis(foo)

for row in res:
    print(row)