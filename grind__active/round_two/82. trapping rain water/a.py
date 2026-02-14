# https://leetcode.com/problems/trapping-rain-water/

from typing import List

# what's the situation?

# i'm given a list of integers, `height`
# where each integer is not less than zero.

# okay, but what does this mean? what am i to do?
# in between two integers, a space can exist.

# what do you mean a space?
# consider:
# height = [1, 0, 1]
# the integers under consideration are at index 0 and index 2
# in between them is a space.

# the space is not neccesarily zero, but a depression in between both extreme integers.
# think of each integer as a pillar of length `1`
# so when you look at [1, 0, 1]
# you have one pillar of length `1`, 
# after, a pillar of length `0`, which is effectively no pillar.
# then a pillar of length `1`

# the `0` is where the space is.

# the same effect can be achieved with
# [2, 1, 2]

# got it, but what am i doing with all this.
# you want to trap rain water in the spaces.

# and return how much rain water you can trap.

# for both [1, 0, 1] and [2, 1, 2]
# we can only trap `1` unit of rainwater inbetween them.

# so, this is what you want to do with the array `height`
# find out the space between pillars, fill it with water
# calculate the total water that can be stored at each point.

# keep in mind, the test cases wouldn't be as simple as the examples.
# you can have [0, 2, 1, 0, 2, 3]
# in which case the total space would be between index 1 (2)
# and the last index with value (3)

# even though there's a depression at index 0, there's no left pillar to form the space.

# in essence, every space, needs a left pillar and a right pillar.
# when you have two pillars of uneven lengths, how do you determine the space between them?

# i.e. [1, 0, 2]
# well, you'd have to priortize the smaller pillar.

# the water can only fill at most size `1`

# i've seen the question before, i'm trying to work my way to a solution
# but i know, the idea is to calculate the space as you go along.
# at each point in `height`

# you're asking the question, what is the furthest relevant pillar to my left,
# what's the furthest relevant pillar to my right.

# using that, i can calulate the space.

# the space would really be the minimum of these two relevant pillars
# we'd sum up the space and everybody's happy.

# okay, but when you say furthest relevant pillar, what do you mean?
# to maximize the space, we want to know the highest pillar on the left, 
# the highest pillar on the right

# the smaller of those pillars minus, whatever you have at current cell
# is the space.

# say you have [5, 3, 6]
# and are at index 1

# the smaller of the two pillars is `5`
# so the space is what's left after you subtract `3`
# from `5`, ergo, `2`

# okay, so how do i know the tallest leftmost pillar
# and tallest rightmost pillar

# you could create two arrays, `leftMostCache` and rightMostCache.
# each position in both arrays contain 
# the tallest leftmost and tallest rightmost pillar
# to that position respectively.

# and so, problem solved.

# error, didn't pass `self` in function arguments for the class `Solution`
# i was too eager to solve the problem, i was just typing away.

# can't believe i got it first time.
# as an optimization, i could probably drop the leftMostCache
# and track the tallest left most as i iterate through the array.

# let's try that in `b.py`

class Solution:
    def trap(self, height: List[int]) -> int:
        leftMostCache = self.getLeftMostCache(height)
        rightMostCache = self.getRightMostCache(height)
        
        totalSpace = 0
        
        for idx, val in enumerate(height):
            leftTallest = leftMostCache[idx]
            rightTallest = rightMostCache[idx]
            
            smallerOne = min(leftTallest, rightTallest)
            curSpace = smallerOne - val
            
            curSpace = max(0, curSpace)
            
            totalSpace += curSpace
            
        return totalSpace
    
    def getLeftMostCache(self, height):
        tallest = 0
        leftMostCache = []
        
        for h in height:
            leftMostCache.append(tallest)
            
            tallest = max(tallest, h)
            
        return leftMostCache
    
    def getRightMostCache(self, height):
        tallest = 0
        rightMostCache = []
        
        dim = len(height)
        for idx in range(dim-1, -1, -1):
            rightMostCache.append(tallest)
            
            val = height[idx]
            tallest = max(val, tallest)
    
        return rightMostCache[::-1]
    

arr = [
    [0,1,0,2,1,0,1,3,2,1,2,1],
]
foo = arr[-1]
sol = Solution()
res = sol.trap(foo)
print(res)
