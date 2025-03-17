# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        pass
        # create a sliding window of size `k`
        # use a set to ensure all the elements in the window are unique
        # if you find a duplicate element, increase the window start
        # until duplicates no longer exist
        # every time the window reaches size `k`, update max sum
        
        maxSum = 0
        curSum = 0
        
        left, right = 0, 0
        
        seen = set()
        dim = len(nums)
        while right < dim:
            n = nums[right]
            
            while n in seen:
                self.removeNum(left, nums, seen)
                curSum -= nums[left]
                left += 1
        
        
            seen.add(n)
            curSum += n
                
            if len(seen) == k:
                maxSum = max(
                    curSum,
                    maxSum
                )
                self.removeNum(left, nums, seen)
                curSum -= nums[left]
                left += 1
            
            right += 1
            
        return maxSum
    
    def removeNum(self, idx, nums, seen):
        num = nums[idx]
        seen.remove(num)
        
    
arr = [
    [[4,4,4], 3],
    [[1,5,4,2,9,9,9], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maximumSubarraySum(foo, bar)
print(res)