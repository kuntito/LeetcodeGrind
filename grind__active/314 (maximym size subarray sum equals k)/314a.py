# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

from typing import List

# what's the situation? i want to implement a function `maxSubArrayLen`
# that takes two arguments, a integer array, `nums` and an integer `k`

# we want to find the length of the longest subarray that sums up to `k`
# how do we define a subarray? is it contiguous? yes

# how do we approach this? the longest we can get is the sum of the entire array
# can i use a two pointer approach where i sum up all the elements of the array
# then adjust the left and right pointers to see if i hit the sum `k`?

# in essence, i'm exploring all the possibilities, but because i'm starting from len(nums) downwards, i might not have to explore all the possibilities

# is there a faster way? not sure
# let's implement this first
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pass
        total = sum(nums)
        if total == k:
            return len(nums)
        
        # how do i approach the two pointer approach
        # can i use a loop?
        # i think recursion is cleaner
        # you'd have two pointers at the extremes and the currsum
        # you'd want to return the first instance where you decremented the pointer
        # and the currSum becamee k
        
        # let's make `k` global and `nums` global
        # the recursive function would only have `currSum` and the pointers
        
        # this recursive approach is problematic, since it takes a depth first approach
        # but what we want is a breadth first approach to solve this
        self.nums = nums
        self.k = k
        
        left, right = 0, len(nums) - 1
        return self.explore(left, right, total)
    
    def explore(self, left, right, currSum):
        # what's the base case?
        # if currSum == self.k
        # what if we never reach this, we return `0`
        # and if we do, we return the length (right - left) + 1
        
        if left > right:
            return 0
        
        if currSum == self.k:
            return (right - left) + 1
        
        leftSide = self.explore(
            left + 1,
            right,
            currSum - self.nums[left]
        )
        if leftSide > 0:
            return leftSide
        
        return self.explore(
            left,
            right - 1,
            currSum - self.nums[right]
        )
        
arr = [
    [[1,-1,5,-2,3], 3],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maxSubArrayLen(foo, bar)
print(res)