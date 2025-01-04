# https://leetcode.com/problems/maximum-product-subarray/description/

# TODO https://neetcode.io/solutions/maximum-product-subarray
# write deep's solution 15:08
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_res, min_res = 0, 0
        
        for n in nums:
            if n == 0:
                max_res, min_res = 0, 0
                continue
                
            if max_res == 0:
                max_res = n
            else:
                one = n * max_res
            
            if min_res == 0:
                min_res = n
            else:
                two = n * min_res
            
            max_res = max(max_res, one)
            min_res = min(min_res, two)
            
        return max_res
        
        
    

arr = [
    [-2,0,-1],
    [-2, -3, -4],
    [2,3,-2,10, -2],
    [-3,-1,-1],
    [-2, -3, -5],
    [-2, 10],
    [0,-3,1,1],
    [5, 0, 5],
]

foo = arr[-1]
sol = Solution()
res = sol.maxProduct(foo)
print(res)
