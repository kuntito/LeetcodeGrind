# https://leetcode.com/problems/maximum-product-subarray/description/

# TODO https://neetcode.io/solutions/maximum-product-subarray
# write deep's solution 15:08
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        uno, dos = 1, 1
        
        for n in nums:
            if n == 0:
                uno, dos = 1, 1
                continue
            
            tmpUno = uno * n
            tmpDos = dos * n
            
            uno = min(tmpUno, tmpDos, n)
            dos = max(tmpUno, tmpDos, n)
            
            res = max(res, dos)
            
        return res
        
        
    

arr = [
    # [-2,0,-1],
    # [2,3,-2,10, -2],
    # [-3,-1,-1],
    # [-2, -3, -5],
    # [-2, 10],
    # [0,-3,1,1],
    # [5, 0, 5],
    [-2, 1, -3, -4],
    [-2, -3, -4],
]

foo = arr[-1]
sol = Solution()
res = sol.maxProduct(foo)
print(res)
