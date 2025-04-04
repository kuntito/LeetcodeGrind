# https://leetcode.com/problems/daily-temperatures/description/


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0 for _ in temperatures]

        stack = []
        for idx in range(len(temperatures) - 1, -1, -1):
            temp = temperatures[idx]
            while stack and temp >= stack[-1][0]:
                stack.pop()

            if stack:
                res[idx] = stack[-1][1] - idx
            stack.append((temp, idx))

        return res
    

arr = [
    [30,60,90],
    [73,74,75,71,69,72,76,73],
    [30,40,50,60],
]
foo = arr[-1]
sol = Solution()

res = sol.dailyTemperatures(foo)
print(res)