# https://leetcode.com/problems/binary-search/

# using binary search, check if `target` exists in the array, `nums`
# if it does, return it's index.
# otherwise, return -1

# how to go about this?
# we're guaranteed, the array, `nums`, is sorted in ascending order
# this way, i know binary search would find target if it exists..

# how do you implement binary search
# two pointers, `left` and `right`, placed at the extreme ends of the array
# we find the mid point between said pointers

# then what, we compare the value at midpoint, `midPointValue` with `target`
# if `midPointValue == target`, return index.

# if the `midPointValue > target`, since the array, `nums`, is sorted in ascending order
# it means `target` is before the `midPointValue`

# so what do you do, you shift the right pointer inwards
# right pointer beomes midPoint -1

# and we repeat the same process.. until you find target or the left pointer exceeds the right pointer i.e. left > right
# i'm making a leap here but it's only because i know it works..

# how do you address odd and even lengths in between both pointers.
# from what i remember, it didn't seem to matter but i'd have to write it out to be clear

# say we had
# 0 1 2 3
# L     R

# mid point is (0 + 3)/2
# this case, 1.5, because integer, 1

# 0 1 2 3
# L M   R

# say `target = 0.5`
# we'd move right pointer to mid point - 1
# which would be where `L` is 

# 0 1 2 3
#LR 

# we do the same thing, calculate mid point, (0+0)/2 = 0
# mid point is `0` here, but we want 0.5
# in this case, we move left pointer to midpoint + 1
# which is `1`

# 0 1 2 3
# R L

# now, we have an invalid state, so it means `target` doesn't exist within array.
# and if it was odd
# say we had
# 0 1 2 3 4
# L       R

# mid point would be (4+0)/2 = 2
# 0 1 2 3 4
# L   M   R

# we want 0.5, so R = M-1
# 0 1 2 3 4
# L R

# we want 0.5, so R moves again,
# midpoint = (0 + 1) / 2 = 0.5 = 0 because integer division

 
# 0 1 2 3 4
#LM R

# midpoint is at L, in this case, we want 0.5, so L moves to M + 1

# 0 1 2 3 4
#  LR

# now, L, R are the same, midpoint is also the same point
# the value is not 0.5
# we move R to M-1

# 0 1 2 3 4
# R L
# now, we're at an invalid state, `target` does not exist.
# now the code

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            halfwayPoint = (right - left)//2
            midIdx = left + halfwayPoint
            midValue = nums[midIdx]
            
            if midValue == target:
                return midIdx
            elif midValue > target:
                right = midIdx - 1
            elif midValue < target:
                left = midIdx + 1
                
        return -1
    
arr = [
    [[-1,0,3,5,9,12], 9],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.search(foo, bar)
print(res)