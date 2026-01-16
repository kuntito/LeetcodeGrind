# https://leetcode.com/problems/search-insert-position/description/

from typing import List

# i'm given an integer array, an asc sorted integer array, `nums` and a target to find in `nums`
# if the `target` exists in `nums`, i should return it's index..

# if not, i should return the index where it would have been..
# i know binary search solves this but i'm not sure why..

# let's consider [1, 5]
# and i'm looking for `4`, eyeballing it, i know it should be in index `1`

#  but let's run through the binary search..
# left pointer = 0
# right pointer = 1
# mid point is:
# left + (right - left)/2 = 
# 0 + (1-0)//2 = 
# 0 + 1//2 = 
# 0 + 0

# mid point is `0`
# mid value is `1`

# how does bin search work, three checks..
# is mid value target? no..
# is mid value greater than target? no
# is mid value less than target? yes, `1` is less than `4`

# so we move left to midPoint + 1
# in our case, left = 0 + 1
# left = 1
# right = 1

# midPoint = 1
# midValue = 5

# is mid value target? no..
# is mid value greater than target? yes
# what do we do? move right to midPoint -1

# right = 1-1 = 0
# left = 1

# rewriting for clarity
# left = 1
# right = 0

# left > right, this breaks the condition for bin search, we end iteration..
# well, it seems `left` is what would indicate the insertion point..

# what if we were looking for a `6` in `[1, 5]`
# left = 0
# right = 1
# midPoint = 0
# midValue = 1

# 6 is greater than mid value, so
# left = midPoint + 1 = 1
# right = 1
# midPoint = 1
# midValue = 5

# `5` is greater than mid value, so
# left = midPoint + 1 = 1 + 1 = 2
# right = 1

# left > right.. so bin search ends..
# again, `left` resides at `2`
# where we should insert..

# what if we wanted to insert `0` in `[1, 5]`
# left = 0
# right = 1
# midPoint = 0
# midValue = 1

# `0` is less than midValue, so
# right = midPoint - 1 = -1
# left = 0

# rewrite for clarity
# left = 0
# right = -1
# left > right, bin Search ends.. again..
# left is where it's at..

# i know it works but it's not intuitive..
# it's intuitive for the greater than.. where we move left += 1
# i get this because the value has to exist after the mid point
# but if the new left is out of range.. then that new left is the value

# but the revers is what's not clear..
# another observation, i can make is before going out of range
# left and right are equal..

# okay, this is more intuitive.. binary search allows you narrow your search..
# and if your search scope becomes 1 number.. and that number isn't target...
# then that's where target would be if it existed..

# the extra step of moving the left or right pointers are unnecessary
# not necessarily so..

# consider, [7] and target = 8
# your logic, left = 0, right = 0
# hence.. the result is left??
# it's not..

# you still need to perform the right steps for binary search which in this case would be..
# moving left = midPoint + 1
# the loop breaks, then you'd have your result..

# your intuition for why left remains the answer when right moves out of bounds was wrong
# the right one is if we're at left = right and the target is smaller than what's at left
# we need to search before left..

# but if right goes out of bounds, it means there's nothing before left..
# hence, left is exactly where the element would be if it existed..
# that's why it works...

# right, the condition for binSearch is `left <= right`
# left and right are allowed to be equal.. i was recalling from memory rather than thinking through
# on that one..

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            midPoint = left + (right - left)//2
            midValue = nums[midPoint]
            
            if target > midValue:
                left = midPoint + 1
            elif target < midValue:
                right = midPoint - 1
            else:
                return midPoint
        
        return left
    
arr = [
    [[1,3,5,6], 2]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.searchInsert(foo, bar)
print(res)