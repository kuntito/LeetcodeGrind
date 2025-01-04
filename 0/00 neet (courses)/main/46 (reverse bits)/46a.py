# https://leetcode.com/problems/reverse-bits/description/

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for _ in range(32):
            res <<= 1
            res |= (n & 1)
            n >>= 1

        return res


arr = [
    43261596,
    4294967293,
]
foo = arr[-1]

sol = Solution()
res = sol.reverseBits(foo)
print(res)