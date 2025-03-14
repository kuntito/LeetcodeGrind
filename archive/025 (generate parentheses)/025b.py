# https://leetcode.com/problems/generate-parentheses/description/


class Solution:
    def generateParenthesis(self, n: int):
        self.res = []
        self.n = n

        self.explore(['('], 1, 0)

        return self.res

    def explore(self, arr, left_count, right_count):
        if left_count > self.n or right_count > self.n:
            return
        if left_count == right_count and left_count == self.n:
            self.res.append(''.join(arr))
            return
        
        arr.append('(')
        self.explore(arr, left_count + 1, right_count)
        arr.pop()

        if left_count > right_count:
            arr.append(')')
            self.explore(arr, left_count, right_count + 1)
            arr.pop()
        

arr = [
    2,
    3,
    # 4,
]

foo = arr[-1]
sol = Solution()
res = sol.generateParenthesis(foo)

for row in res:
    print(row)