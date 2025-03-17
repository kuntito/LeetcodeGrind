# https://leetcode.com/problems/count-the-number-of-k-free-subsets/description/

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        pass
    
        # sort nums
        # put all numbers in a set
        # iterate through nums, check if `n + k` exists in the set
        # if yes, decrement `initDim -= 1`
        
        # such that at the end of this, none of the elements in the set can combine to form `k`
        
        # then do the math to find out how many subsets you can determine from `initDim`
        
        # TODO does the answer include an empty set?