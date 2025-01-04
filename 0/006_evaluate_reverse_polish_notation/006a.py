# https://leetcode.com/problems/evaluate-reverse-polish-notation/


class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b)
        }

        res = []
        for t in tokens:
            if t in operations:
                b, a = res.pop(), res.pop()
                item = operations[t](
                    a,
                    b,
                )
            else:
                item = t

            res.append(int(item))


        return res[0]
    
arr = [
    ["2","1","+","3","*"],
    ["4","13","5","/","+"],
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"],
]
foo = arr[-1]

sol = Solution()
res = sol.evalRPN(foo)
print(res)

