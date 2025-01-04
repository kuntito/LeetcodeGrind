# https://leetcode.com/problems/reverse-integer/description/

import math
# TODO https://neetcode.io/solutions/reverse-integer
# 10:25
# TODO deep solution
class Solution:
    def reverse(self, x: int) -> int:
        pass
        MIN = -2 ** 31
        MAX = abs(MIN) - 1
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x/10)
        
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            
            res = (res * 10) + digit
        return res
        
arr = [
    -123,
    120,
]
foo = arr[-1]
sol = Solution()
res = sol.reverse(foo)
print(res)
