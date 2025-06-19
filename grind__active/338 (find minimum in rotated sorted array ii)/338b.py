# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List

# how can binary search be applied to this?
# two pointers, left and right

# at the start of the search, `left` is set to the leftmost index `0`
# and right is set to the rightmost index, `len(nums) - 1`

# if the value at the left is less than the value at the right
# it's safe to say all the numbers are sorted

# hence, we can return `nums[left]`


# if the value at the left is equal to the value at the right
# it's safe to assume, it's also sorted
# hence, return `nums[left]`


# however, if the left value is greater than the right value
# it means the starting point is in between `left` and `right`
# so we set???
class Solution:
    def findMin(self, nums: List[int]) -> int:
        pass
    
arr = [
    [1,3,5],
    [2,2,2,0,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findMin(foo)
print(res)