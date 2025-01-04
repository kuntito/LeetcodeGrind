# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            n = self.transform(n)
            if n == 1:
                return True

        return False

    def transform(self, n):
        res = 0

        while n:
            digit = n % 10
            res += digit ** 2
            n //= 10

        return res

arr = [
    19,
    2
]
foo = arr[-1]
sol = Solution()
res = sol.isHappy(foo)
print(res)