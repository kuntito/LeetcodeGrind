# https://leetcode.com/problems/power-of-two/description/

# TODO https://neetcode.io/solutions/power-of-two
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        pass
        while n > 1:
            n, rem = divmod(n, 2)
            if rem:
                return False
        
        return True
    
arr = [
    1,
    3,
    16,
]
foo = arr[-1]
sol = Solution()
res = sol.isPowerOfTwo(foo)
print(res)