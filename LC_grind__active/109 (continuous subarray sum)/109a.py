# https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        pass
        # sum up all the elements in nums
        # if during the sum you come across a multiple of `k`
        # return true
        
        temp = 0
        for idx, n in enumerate(nums):
            temp += n
            if temp % k == 0 and idx > 0:
                return True
            
            
        self.nums = nums
            
        # recursively remove the values of the bookend indices
        # left and right
        return self.explore(temp, 0, len(nums)-1, k, {})
    
    def explore(self, curSum, left, right, k, memo):
        mitem = (left, right)
        if mitem in memo:
            return memo[mitem]
        
        dist = (right - left) + 1
        if dist < 2:
            return False

        if curSum % k == 0:
            return True
        
        leftVal, rightVal = self.nums[left], self.nums[right]
        
        res = self.explore(
            curSum - leftVal,
            left + 1,
            right,
            k,
            memo
        ) or self.explore(
            curSum - rightVal,
            left,
            right - 1,
            k,
            memo
        )
        
        memo[mitem] = res
        return memo[mitem]
    
    
arr = [
    [[23,2,4,6,7], 6],
    [[23,2,6,4,7], 6],
    [[23,2,6,4,7], 13],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.checkSubarraySum(foo, bar)
print(res)