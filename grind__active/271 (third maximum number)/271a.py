# https://leetcode.com/problems/third-maximum-number/description/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        pass
        nums.sort(reverse=True)
        maxNum = nums[0]
        
        distinct = 0
        idx = 0
        
        dim = len(nums)
        while idx < dim:
            n = nums[idx]
            
            while idx + 1 < dim and n == nums[idx + 1]:
                idx += 1
                
            distinct += 1
            if distinct ==  3:
                return n
            
            idx += 1
            
        return maxNum
            
arr = [
    [1, 2],
    [3, 2, 1],
    [2, 2, 3, 1],
]
foo = arr[-1]
sol = Solution()
res = sol.thirdMax(foo)
print(res)
        
        