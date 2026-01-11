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
        
        curr = 0
        while x:
            # `fmod` does the same as `mod` but retains the sign
            # in python, `-1 % 10 == 9`
            # but `fmod(-1, 10) == -1`
            last_dig = int(math.fmod(x, 10))
            
            # because `(-123 // 10) is '13, it rounds further away from zero`
            # while `int(-123/10)` truncates the floating point number `-12.3` to `-12`
            x = int(x/10) 
            
            # this checks if `curr` ever becomes greater than (max 32 bit integer minus it's last digit)
            # the reason for minus the last digit is we assume the environment cannot store
            # integers greater than 32 bit
            # so `curr` could become greater, it would have overflown before
            # we could compare it with `MAX`
            MAX_wo_last = MAX // 10
            one = curr > MAX_wo_last
            
            # if `curr` ever equals `MAX_wo_last`
            # check if the next digit to be added is equal to `MAX_last_dig`
            MAX_last_dig = MAX % 10
            two = (curr == MAX_wo_last) and last_dig >= MAX_last_dig
            
            if one or two:
                return 0
            
            # TODO elaborate on the conditions for these guys
            if (curr < MIN // 10 or (curr == MIN // 10 and last_dig <= MIN % 10)):
                return 0
            
            curr = (curr * 10) + last_dig
        return curr
        
        
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