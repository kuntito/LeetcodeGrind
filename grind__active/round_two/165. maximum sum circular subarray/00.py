from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # for each number explore the biggest line you can form.
        
        dim = len(nums)
        
        wealthiest = nums[0]
        for idx in range(dim):
            groupWealth = self.getRichestGroup(idx, nums)
            if groupWealth > wealthiest:
                wealthiest = groupWealth
                
        return wealthiest
    
    def getRichestGroup(self, startIdx, arr):
        # it's circular so, you start at idx, and go
        # for as many elements left in the array
        # wrap the index
        
        dim = len(arr)
        richestGroup = arr[startIdx]
        
        rollingSum = 0
        for x in range(startIdx, startIdx + dim):
            idx = x % dim
            num = arr[idx]
            
            # you can either take the next number alone
            # or take it along with what you have.
            
            rollingSum = max(
                num,
                rollingSum + num
            )
            
            if rollingSum > richestGroup:
                richestGroup = rollingSum
                
        return richestGroup
            
            
arr = [
    [1,-2,3,-2],
]
foo = arr[-1]
sol = Solution()

res = sol.maxSubarraySumCircular(foo)
print(res)