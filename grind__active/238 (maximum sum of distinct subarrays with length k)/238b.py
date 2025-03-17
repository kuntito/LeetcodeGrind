# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        pass
        # create a sliding window of size `k`
        # two pointers, left and right
        
        # initialize them such that left is `0`
        # and right is `0`
        # keep incrementing right, if it's value is the same as the previous index
        
        # keep track of everytime you increment right
        # until you reach the size `k`
        
        left, right = 0, 0
        dim = len(nums)
        
        curSum = 0
        # this way we set the pointers at the first `k` unique elements
        # track the sum along the way
        # such that left is where the window starts
        # and right - 1 is the index the window ends
        count = 0
        while right < dim and count < k:
            val = nums[right]
            curSum += val
            while right + 1 < dim and nums[right + 1] == val:
                right += 1
                
            right += 1
            count += 1
        
        print(left, right)
            
        if count < k: return 0
        
        maxSum = curSum
        while right < dim:
            val = nums[right]
            
            
        
    
arr = [
    [[4,4,4], 3],
    [[1,5,4,2,9,9,9], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maximumSubarraySum(foo, bar)
print(res)