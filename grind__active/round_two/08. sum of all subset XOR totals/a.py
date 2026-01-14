# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

# we're given an array `nums` and want to perform some operations on it and return an integer.
# what are we doing? we want to find all the subsets of `nums`
# for each subset, we want to XOR all it's elements

# i.e. nums = [1, 2]
# the subsets are [], [1], [2] and [1, 2]
# for each subset, we XOR all the values
# then sum them up

# so how do we find all the subsets,
# from experience, i know recursion works
# for each call, you either pick no element
# or pick the next element

# so for the array [1, 2]
# first call, we pick nothing, []
# then shift the index forward..

# this simply confirms i can explore every subset
# i'd see how to take this further in `b.py`

class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        self.explore([], 0, nums)
        
    def explore(self, arr, idx, nums):
        if idx == len(nums):
            print(arr)
            return
            
        self.explore(arr, idx + 1, nums)
        
        arr.append(nums[idx])
        self.explore(arr, idx + 1, nums)
        arr.pop()
        
arr = [[1, 2, 3]]
foo = arr[-1]
sol = Solution()
res = sol.subsetXORSum(foo)
