# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/


class Solution:
    def maxScore(self, s: str) -> int:
        dim = len(s)
        arr = [0 for _ in range(dim)]

        count = 0
        for idx in range(dim-1, -1, -1):
            ch = s[idx]
            if ch == '1':
                count += 1
            arr[idx] = count

        res = 0
        count = 0
        for idx, ch in enumerate(s):
            if ch == '0':
                count += 1
            
            if idx + 1 < dim:
                res = max(
                    count + arr[idx + 1],
                    res,
                )

        return res


arr = [
    "011101",
    "00000",
    "00111",
    "1111",
]
foo = arr[-1]
sol = Solution()
res = sol.maxScore(foo)
print(res)