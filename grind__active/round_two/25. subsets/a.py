# https://leetcode.com/problems/subsets/description/

from typing import List

# i'm given an array of unique numbers and asked to return all it's subsets.
# they call it the power set..

# the solution must not contain duplicates i.e. [1, 2] and [2, 1]
# are the same thing..

# so how would i go about this..

# i'm tempted to try the two path recursion thing..
# since that gives all the subsets.. i remember this from the XOR question..

# on each recursive call, we have the current index and the tracking array
# on each call, there's two branches..
# one where you append the element at current index to the tracking array
# another where you leave the array as is..

# but in both scenarios, you move the current index forward..
# it's trivial enough that i can continue implementing from here..
# base case is when current index goes out of bounds...

# okay but how do we want to track this..
# we don't just want to find the subset, we want to return an array of all subsets..
# so, this case requires one more array, i'd call it `res`
# once i hit base case, `res` would append..

# the tracking array, or rather a copy of the tracking array..
# the algorithm reuses the same array for all subsets..
# so i need a copy of it, a snapshot for each subset..
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        pass
        res = []
        tracking = []
        curIdx = 0
        
        self.nums = nums
        self.explore(curIdx, tracking, res)
        
        return res
    
    def explore(self, curIdx, tracking, res):
        if curIdx == len(self.nums):
            res.append(tracking[::])
            return
        
        self.explore(curIdx + 1, tracking, res)
        
        tracking.append(
            self.nums[curIdx]
        )
        self.explore(curIdx + 1, tracking, res)
        
        tracking.pop()