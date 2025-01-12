# https://leetcode.com/problems/ugly-number/description/

class Solution:
    def isUgly(self, n: int) -> bool:
        pass
        # find all the prime factors of a number
        # if you find a prime factor that's neither 2, 3, 5
        # return False
        low = -2 * 10 **31
        if n == low:
            return False
        
        n = abs(n)
        mains = [2, 3, 5]
        for i in range(1, n//2 + 1):
            if n % i == 0 and i not in mains:
                return False
        
        return True

    
arr = [
    14,
    1,
    8,
    6,
]
foo = arr[-1]
sol = Solution()
res = sol.isUgly(foo)
print(res)