class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2

        ult, penult = 1, 2

        for _ in range(3, n+1):
            temp = penult
            penult += ult
            ult = temp

        return penult


foo = Solution()
res = foo.climbStairs(5)

print(res)
