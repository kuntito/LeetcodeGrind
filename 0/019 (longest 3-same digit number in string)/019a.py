# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/

class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = None
        streak = 1

        for idx, ch in enumerate(num):
            if idx == 0:
                continue

            if ch == num[idx - 1]:
                streak += 1
            else:
                streak = 1

            if streak == 3:
                dig = int(ch)
                if res is None:
                    res = dig
                else:
                    res = max(
                        res,
                        dig,
                    )
        
        return "" if res is None else str(res) * 3


arr = [
    "6777133339",
    "42352338",
    "2300019",
]
foo = arr[-1]
sol = Solution()
res = sol.largestGoodInteger(foo)
print(res)