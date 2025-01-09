# https://leetcode.com/problems/power-of-four/description/

# TODO https://neetcode.io/solutions/power-of-four
# 02:47
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        pass
        # if `n` is <= 0 return False
        if n <= 0: return False
        
        # recursively divide n by 4, if there a remainder
        # return False
        while n > 1:
            n, rem = divmod(n, 4)
            if rem:
                return False
        
        
        return True
    
arr = [
    5,
    1,
    0,
    16,
    20,
]
foo = arr[-1]
sol = Solution()
res = sol.isPowerOfFour(foo)
print(res)