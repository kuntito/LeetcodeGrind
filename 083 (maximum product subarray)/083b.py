# https://leetcode.com/problems/maximum-product-subarray/description/

# TODO https://neetcode.io/solutions/maximum-product-subarray
# write deep's solution 15:08
class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
                continue
            
            tmpMax = curMax * n
            tmpMin = curMin * n
            
            curMax = max(tmpMax, tmpMin, n)
            curMin = min(tmpMax, tmpMin, n)
            res = max(res, curMax)
            
        return res
        
        
    

arr = [
    # [-2,0,-1],
    # [2,3,-2,10, -2],
    # [-3,-1,-1],
    # [-2, -3, -5],
    # [-2, 10],
    # [0,-3,1,1],
    # [5, 0, 5],
    [-2, -3, -4],
]

foo = arr[-1]
sol = Solution()
res = sol.maxProduct(foo)
print(res)
