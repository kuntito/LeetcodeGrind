# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/

class Solution:
    def maxScore(self, s: str) -> int:
        one_count = sum(1 for ch in s if ch == '1')

        res = 0
        zero_count = 0
        for ch in s[:-1]:
            if ch == '1':
                one_count -= 1
            if ch == '0':
                zero_count += 1
            res = max(
                res,
                zero_count + one_count
            )

        return res
    

arr = [
    "011101",
    "00000",
    "00111",
    "1111",
    "00111",
]
foo = arr[-1]
sol = Solution()
res = sol.maxScore(foo)
print(res)