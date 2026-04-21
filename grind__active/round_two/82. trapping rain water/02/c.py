# https://leetcode.com/problems/trapping-rain-water/

from typing import List


# 'pparently, Navdeep has an O(1) space solution.
# i want to understand it, he uses two pointers
# four pointers really

# but let's start with the first two `l` and `r`
# placed at extreme ends of the array

# then we have another two pointers, `leftMax` and `rightMax`
# which i imagine are the tallestLeft and tallestRight pointers at each point

# but let's find out

# we start a while loop based on `l < r`
# if the `leftMax`
# if the lefmost tallest pillar is less than the right most tallest pillar
# we move `l` forward..
# update leftMax to be the bigger of whatever it was
# and the new position at `l`

# then update the space at that point to be 
# leftMax - height[l]

# but why?
# what does moving tell me..

# if i compare the pointers at the extreme ends
# and i find the left is the shorter, i move it

# but you're not comparing the pointers..
# maxRight is a misnomer..
# it's not the max right, it's simply the extremeRight pointer

# maxLeft is an accurate name.
# so we compare the maxLeft with the extremeRight pointer
# if maxLeft is less..
# what would this mean..
# it would mean, this pillar is what would determine a space..

# if that space existed.
# so we move the left pointer forward.
# ..

# TODO deep the O(1) solution..
# https://www.youtube.com/watch?v=ZI2z5pq0TqA
# 15:37

# [1, 0, 0, 2]
class Solution:
    def trap(self, height: List[int]) -> int:
        pass