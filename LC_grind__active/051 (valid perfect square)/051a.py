# https://leetcode.com/problems/valid-perfect-square/description/

# TODO https://neetcode.io/solutions/valid-perfect-square
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # on observation, perfect squares increases by incremental amounts of `2`
        # the first increment is `3`
        # (1) increases by `3` and becomes `4`
        # the increment `3` increases by 2 and becomes `5`
        # (4) increases by `5`, and becomes (9)
        # the increment `5` increases by `2` and becomes `7`
        # (9) increases by `7` and becomes `16`
        # and the cycle continues

        # create a variable, `x` which represents the first perfect square, (1)
        # that runs through a loop mimicing this behavior
        # `x` should run as long as it's <= `num`
        x = 1
        incr = 3
        while x <= num:
            if x == num: return True

            x += incr
            incr += 2

        return x == num

arr = [
    16,
    14,
]
foo = arr[-1]
sol = Solution()
res = sol.isPerfectSquare(foo)
print(res)