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
        # taking a breadth first approach, we'd use a list
        # each list item would have (currSum, left, right)
        # if currSum == k: return length
        # if not, add new entries to the list
        # (currSum - nums[left], left + 1, right)
        # (currSum - nums[right], left, right - 1)
        
        # if left > right, don't add a new one
        left, right = 0, len(nums) - 1
        lst = [(total, left, right)]
        
        while lst:
            temp = []
            while lst:
                currSum, left, right = lst.pop()
                if currSum == k:
                    return (right - left) + 1
                
                if left == right:
                    continue
                
                temp.append((
                    currSum - nums[left],
                    left + 1,
                    right
                ))
                
                temp.append((
                    currSum - nums[right],
                    left,
                    right - 1
                ))
            lst = temp

        return 0

        
arr = [
    [[1,-1,5,-2,3], 3],
    # [[-2,-1,2,1], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.maxSubArrayLen(foo, bar)
print(res)