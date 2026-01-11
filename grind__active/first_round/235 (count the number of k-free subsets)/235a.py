# https://leetcode.com/problems/count-the-number-of-k-free-subsets/description/

class Solution:
    def countTheNumOfKFreeSubsets(self, nums: list[int], k: int) -> int:
        pass
    
        # put all numbers in a set
        validNums = set(nums)
        
        # sort nums
        nums.sort()
        
        # iterate through nums, check if `n + k` exists in the set
        # if yes, decrement `initDim -= 1`
        for n in nums:
            if n not in validNums:
                continue
            complement = n + k
            if complement in validNums:
                validNums.remove(complement)
        
        # at the end of this `validNums` would contain all numbers that cannot form a subset
        
        print(validNums)
        
        # do the math to find out how many subsets you can determine from `len(validNums)`
        
        # TODO does the answer include an empty set?
        

arr = [
    [[5,4,6], 1],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.countTheNumOfKFreeSubsets(foo, bar)
# print(res)