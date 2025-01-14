# https://leetcode.com/problems/ugly-number/description/

# TODO how's the actual code different from what you were trying to do in the comments
import math
class Solution:
    def isUgly(self, n: int) -> bool:
        # if n <= 0: return False

        # end = n + 1
        # for i in range(2, end):
        #     while n % i == 0:
        #         if i not in [2, 3, 5]:
        #             return False
        #         n //= i
        #     if n == 1: break
                
        # return True
        
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0:
                n //= p
        
        return n == 1


    
arr = [
    1,
    8,
    6,
    14,
    -1000,
    -2147483648,
    905391974, # TODO TLE look at solution
]
foo = arr[-1]
sol = Solution()
res = sol.isUgly(foo)
print(res)