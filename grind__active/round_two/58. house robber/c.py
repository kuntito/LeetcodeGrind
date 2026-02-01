# https://leetcode.com/problems/house-robber/

from typing import List

# i solved this in `b.py`
# but my solution was not the cleanest

# i looked up neetcode's solution and would write it how i understand it.
# at any point, 
# you either want to start the robbery from the house you're at
# or the next one.

# why not the third..
# because the third can be included with the first..

# first, second, third..
# if you rob the third alone, might as well, rob the first..
# since, the aim is to maximize the amount..
# what if you wanted to rob first then fourth..
# or first then fifth.. how do you know which one..

# here's where things can spiral..
# think of it this way..

# at every point, you're trying to find the max you can rob onwards..
# so when you rob first then third..
# you're not robbing the house at third per se..

# you're finding out how much you can make
# if you started the robbery at third..

# if we start the robbery at third..
# we can either pick the third or the fourth house..
# a exact replica of the problem we started with..

# we'd be doing the same thing in every iteration.
# so going back to the first house..

# there's only two things to do..
# either rob the first + the most we can rob at the third
# or get the most we can rob starting at the second house..

# right, so this is how he could summarize the logic..
# at any point in time, we only need two variables..

# the most we can rob from the next house, and 
# the most we can rob from the next next house

# at each iteration, you want to find whichever's higher
# between
# (currentHouse + mostAtNextNextHouse) OR (mostAtNextHouse)

# starting the iteration in reverse, we can implement this..
# having two variables..

# mostAtNext, mostAtNextNext..
# then on each iteration, we do..

# currentMost = max(
#   currentVal + mostAtNext,
#   mostAtNextNext 
# )

# and eventually, we'd get to `nums[0]`
# problem solved..

# error,
# i did added current value with next house instead of nextNextHouse..

# keep in mind you'd have to update `mostAtNext` and `mostAtNextNext` too..
# TODO you can probably do this without reverse iteration..
# i just have to work out why that also works..
class Solution:
    def rob(self, nums: List[int]) -> int:
        mostAtNext, mostAtNextNext = 0, 0
        
        dim = len(nums)
        for i in range(dim-1, -1, -1):
            currentVal = nums[i]
            
            currentMost = max(
                currentVal + mostAtNextNext,
                mostAtNext
            )
            
            mostAtNextNext = mostAtNext
            mostAtNext = currentMost
            
        return mostAtNext
    
    
arr = [
    [1,2,3,1],
]
foo = arr[-1]
sol = Solution()
res = sol.rob(foo)

print(res)