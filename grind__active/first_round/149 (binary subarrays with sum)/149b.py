# https://leetcode.com/problems/binary-subarrays-with-sum/description/

# TODO check 149a.py
# TODO https://neetcode.io/solutions/binary-subarrays-with-sum
# TODO 06:18
# TODO how does this work? start from `tg.py`
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:

        a = self.getCountSubarraysLTE(goal, nums)
        b = self.getCountSubarraysLTE(goal - 1, nums)
        return a - b
    
    # get subarrays less than or equal to `target`
    def getCountSubarraysLTE(self, target, nums):
        if target < 0:
            return 0
        
        subArrCount = left = curSum = 0
        
        dim = len(nums)
        
        for idx in range(dim):
            curSum += nums[idx]
            
            while curSum > target:
                curSum -= nums[left]
                left += 1
            
            # print('left is', left)
            winLen = (idx - left + 1)
            # print(winLen)
            subArrCount += winLen
            
        return subArrCount

    
arr = [
    [[0, 0, 0, 0, 0, 1], 0],
    [[0, 0, 0, 0, 0], 0],
    [[0, 0, 0], 0],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.numSubarraysWithSum(foo, bar)
print(res)