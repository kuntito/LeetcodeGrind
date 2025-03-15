# https://leetcode.com/problems/continuous-subarray-sum/description/

# TODO https://neetcode.io/solutions/continuous-subarray-sum
# TODO deep the solution
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:        
        remainder = {0: -1} # TODO why this?
        total = 0

        for idx, num in enumerate(nums):
            total += num
            
            r = total % k
            if r not in remainder:
                remainder[r] = idx
            elif idx - remainder[r] > 1:
                return True
        
        return False
    
arr = [
    [[23,2,4,6,6], 7]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.checkSubarraySum(foo, bar)

print(res)