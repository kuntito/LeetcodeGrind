# https://leetcode.com/problems/largest-unique-number/description/

class Solution:
    def largestUniqueNumber(self, nums: list[int]) -> int:
        nums.sort()
        
        idx = len(nums) - 1
        while idx >= 0:
            n = nums[idx]

            prev = nums[idx - 1] if (idx - 1) >= 0 else None
            nex = nums[idx + 1] if (idx + 1) < len(nums) else None
            
            if n not in (prev, nex):
                return n
                
            idx -= 1
            
        return -1
    
arr = [
    [5,7,3,9,4,9,8,8,3,1],
    [11, 10, 11]
]
foo = arr[-1]
sol = Solution()
res = sol.largestUniqueNumber(foo)
print(res)