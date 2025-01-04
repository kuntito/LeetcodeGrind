# https://leetcode.com/problems/plus-one/description/


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits) - 1
        
        num = 0
        for idx, dig in enumerate(digits):
            num += dig * 10 ** n
            n -= 1

        num += 1

        return [int(ch) for ch in str(num)]

arr = [
    [1, 2, 3],
]
foo = arr[-1]

sol = Solution()
res = sol.plusOne(foo)
print(res)

