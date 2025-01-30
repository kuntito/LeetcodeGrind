# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/description/class Solution:

import math
class Solution:
    def getSumAbsoluteDifferences(self, nums: list[int]) -> list[int]:
        pass
        left_arr = self.get_left_avg(nums)
        right_arr = self.get_right_avg(nums)
        
        dim = len(nums)
        
        arr = [0 for _ in nums]
        
        for idx, n in enumerate(nums):
            left = left_arr[idx - 1] if idx - 1 >= 0 else 0
            right = right_arr[idx + 1] if idx + 1 < dim else 0

            leftDiff = n - left if left else 0
            rightDiff = right - n if right else 0
            
            leftAvg = leftDiff * idx
            rightAvg = (dim - (idx + 1)) * rightDiff
            
            arr[idx] = round(leftAvg + rightAvg)
            
        
        return arr
    
        
    def get_left_avg(self, nums):
        arr = [0 for _ in nums]
        
        total = 0
        for idx, n in enumerate(nums):
            total += n
            avg = total/(idx + 1)
            arr[idx] = avg
            
        return arr
    
    def get_right_avg(self, nums):
        arr = [0 for _ in nums]
        dim = len(nums)
        
        total = 0
        for idx in range(dim-1, -1, -1):
            n = nums[idx]
            total += n
            
            ln = dim - idx
            arr[idx] = total/ln
            
        return arr
            
arr = [
    [2,3,5],
    [1,4,6,8,10],
]
foo = arr[-1]
sol = Solution()
res = sol.getSumAbsoluteDifferences(foo)
print(res)