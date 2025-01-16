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
            # `fmod` does the same as `mod` but retains the sign
            # in python, `-1 % 10 == 9`
            # but `fmod(-1, 10) == -1`
            digit = int(math.fmod(x, 10))
            x = int(x/10) 
            # because `(-123 // 10) is '13, it rounds further away from zero`
            # while `int(-123/10)` truncates the floating point number `-12.3` to `-12`
            
            # the penultimate digit in `res` is greater than the penultimate in `MAX`
            # it will go out of bounds
            # if the penultimate digit in `res` equals the penultimate digit in `MAX`
            # check if the ultimate digit in `res` is greater than 
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            
            res = (res * 10) + digit
        return res
        
        
arr = [
    120,
    -123,
    7463847412, # TODO why is the answer to this zero?
]
foo = arr[-1]
sol = Solution()
res = sol.reverse(foo)
print(res)


# print(math.fmod(-123, 10))
# print(-123//10)