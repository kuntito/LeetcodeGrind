# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

from typing import List

# i want to implement a function, `findMin`
# this function returns an integer and takes one argument, 
# an integer array, `nums`.

# `nums` is a rotated sorted array. this means it's elements are sorted from smallest
# to largest in a circular manner.

# consider the array, `[3, 4, 1, 2]`
# the sorted order is 1, 2, 3, 4
# but in this case the order starts at index 2
# and wraps around to the start of the array

# index 2 => 1
# index 3 => 2
# index 0 => 3
# index 1 => 4

# my job is to return the smallest number in this array.
# keep in mind, the array can contain duplicates.

# my first idea is to run through the array and return the first number that's
# smaller than the previous number

# if i can't find that number, it would mean the smallest number is the first number.

# it works but i'm not sure this approach warrants the hard tag.
# i imagine it must be something to do with binary search

class Solution:
    def findMin(self, nums: List[int]) -> int:
        for idx, curNum in enumerate(nums):
            prevNum = nums[idx - 1] if idx - 1 >= 0 else None
            
            if prevNum and curNum < prevNum:
                return curNum
        
        
        return nums[0]
    
arr = [
    [1,3,5],
    [2,2,2,0,1],
]
foo = arr[-1]
sol = Solution()
res = sol.findMin(foo)
print(res)