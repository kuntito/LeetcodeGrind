# https://leetcode.com/problems/sqrtx/description/

# TODO https://neetcode.io/solutions/sqrtx
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = -1, 2**31

        # use binary search
        # get the mid point value, `a`
        # and the next value `b`
        # if `a**2` > x
        #   right = mid point - 1
        # if `a**2` <= x and `b**"` > x:
        #   return `a`
        # else:
        #   left = mid point + 1

        while left <= right:
            mid_point = (left + right)//2
            a = mid_point ** 2
            b = (mid_point + 1) ** 2

            if a > x:
                right = mid_point - 1
            elif a <= x and b > x:
                return mid_point
            else:
                left = mid_point + 1

            
arr = [
    1,
    0,
    2,
    4,
    2147395599,
]
foo = arr[-1]
sol = Solution()
res = sol.mySqrt(foo)
print(res)