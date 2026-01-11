# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # declare a variable, `mult` to keep track of the product
        # iterate through `nums`
        # if you hit `zero`, restart the logic, set `mult = 1`
        
        currStreak = 1
        # there's no way you have a negative result
        # when the array contains more than two numbers 
        res = 0
        
        # representing the first neg result and it's index
        firstNeg = [None, None]
        
        # keep track of all products for all non-zero numbers
        
        # the first time you encounter a negative number
        # store the product at that point as `firstNeg`
        for idx, n in enumerate(nums):
            currStreak *= n
            
            res = max(res, currStreak)
                        
            if n < 0 and firstNeg[0] is None:
                firstNeg = [currStreak, idx]
            
            # if the product is negative
            # and the first negative streak has been found
            # and the current negative streak is not the first negative
            firstNegVal, firstNegIdx = firstNeg
            if currStreak < 0 and firstNegVal and idx != firstNegIdx:
                res = max(res, currStreak//firstNegVal)
            
            if currStreak == 0:
                firstNeg = [None, None]
                currStreak = 1
                
        return res
    

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
