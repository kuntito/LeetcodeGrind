# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = ""

        for idx in range(len(num)-2):
            if num[idx] == num[idx+1] == num[idx+2]:
                res = max(res, num[idx:idx+3])

        return res
    
arr = [
    "6777133339",
    "2300019",
    "42352338",
]
foo = arr[-1]
sol = Solution()
res = sol.largestGoodInteger(foo)
print(res)