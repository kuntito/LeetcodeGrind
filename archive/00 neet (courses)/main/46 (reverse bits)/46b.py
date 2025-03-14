class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1
            res |= bit << 31 - i

        return res


arr = [
    43261596,
    4294967293,
]
foo = arr[-1]

sol = Solution()
res = sol.reverseBits(foo)
print(res)