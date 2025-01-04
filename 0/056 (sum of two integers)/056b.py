# https://leetcode.com/problems/sum-of-two-integers/submissions/
def to_bin(num):
    return f'{num:b}'

# TODO https://www.youtube.com/watch?v=gVUrDV4tZfY
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while (b != 0):
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a


arr = [
    [-3, 2],
    [122, 1],
    # [-1, 1]
]
foo, bar = arr[-1]
sol = Solution()
# res = sol.getSum(foo, bar)
print((2 & 3) << 1)

