# https://leetcode.com/problems/house-robber/

from typing import List

# i'm given an array of integers, `nums`
# each element represent the amount of money in every house on a given street.

# my job is to find the max amount of money i can rob from these houses.
# the constraint is, i can't rob money from two houses, if they're next to each other

# if there are four houses and i rob the first house, 
# i can't rob the second house..
# but the third, fourth houses are fair game
# with the same logic, if i choose the third house, i can't rob the fourth

# in essence, i can summarize, do i rob the first house or the second house?
# how about the third?

# the third isn't too relevant, reason being, if i start from the third..
# i might as well, rob the first house too..

# i wouldn't want to leave money on the table..
# so.. only the first and second are of consideration..

# okay.. say, i'm at the first house, what do i want to know?
# what house do i rob next..
# it's either i rob the third or something after it..
# got a feeling it's a similar pattern to the initial approach..

# starting at first or second and NOT third..
# i'm at the first house,
# i can choose the third..
# i can choose the fourth..
# can i choose the fifth..

# let's draw this out
# [1, 2, 3, 4, 5]
# if i rob first house then fifth house.. i might as well
# rob the third.. i don't want to leave money on the table..
# in essence, at every point, i should only consider the next two houses
# after i skip the next house..

# if i'm robbing house `i`,
# my next house would only ever be houses `i+2` or `i+3`
# this is recursion, since i'm doing the same thing at each house..

# what would be the base case..
# when i go out of bounds..

# also, since at each house, i have two options, i want to maximize the money
# i'd pick the one that gives me the most money..

# a recursive call at each house, and i'd return the total money i robbed at said house..
# do i need to memoize..

# [1, 2, 3, 4, 5]
# seems the same houses can be reached from different paths./
# if i'm at house 1, i can rob house 4
# if i'm at house 2, i can rob house 4

# if i've robbed starting from house 4, it makes sense to cache the result of that exploration.
# so.. let's ball

# what should the recursive arguments be..
# curIdx
# nums
# memo

# oversight, what happens if there's only one house?
# you've hardcoded to check for memo[0] and memo[1]

# i can handle that base case with a check at the start
# `if len(nums) == 1: return nums[0]`

# another error, to get the value at the current index..
# i did `curVal = memo[idx]` instead of getting it from `nums`
# `curVal = nums[curIdx]`

# another mistake, after checking if current index has been memoized..
# i accessed `nums[curIdx]` instead of returning the memoized value
# `memo[curIdx]`

# it works but i remember there being a cleaner way to do it..

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
    
        memo = {}
        self.explore(0, nums, memo)
        self.explore(1, nums, memo)
        
        # print(memo)
        
        return max(
            memo[0],
            memo[1]
        )
        
    def explore(self, curIdx, nums, memo):
        if curIdx in memo:
            return memo[curIdx]
        # if we go out of bounds, that path should return `0`
        # we couldn't rob any houses there
        if curIdx >= len(nums):
            return 0
        
        curVal = nums[curIdx]
        
        nextAvailHouse = self.explore(curIdx + 2, nums, memo)
        secondNextAvailHouse = self.explore(curIdx + 3, nums, memo)
        
        memo[curIdx] = curVal + max(
            nextAvailHouse,
            secondNextAvailHouse
        )
        
        return memo[curIdx]
    
arr = [
    [8,4,3,3,10],
    [6,6,4,8,4,3,3,10],
]
foo = arr[-1]
sol = Solution()
res = sol.rob(foo)

print(res)