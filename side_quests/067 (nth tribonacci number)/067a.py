# https://leetcode.com/problems/n-th-tribonacci-number/description/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0
        if n <= 2: return 1
        
        uno, dos, tres = 0, 1, 1
        
        for _ in range(n-2):
            next_val = uno + dos + tres
            
            uno = dos
            dos = tres
            tres = next_val
            
        return tres
    
arr = [
    25,
    4,
]
foo = arr[-1]
sol = Solution()
res = sol.tribonacci(foo)
print(res)