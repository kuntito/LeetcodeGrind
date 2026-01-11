# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/description/

# TODO https://neetcode.io/solutions/special-array-with-x-elements-greater-than-or-equal-x
# TODO implement solution then compare with 032a.py
class Solution:
    def specialArray(self, nums: list[int]) -> int:
        pass
    
        # are there any `n` numbers in `nums` such that
        # those `n` numbers are the only numbers in `nums` greater than `n`
        
        # if we sort the array, we guaranteed that for every `i`
        # where `0 < i < len(nums)`
        
        # every number in `nums[i:]` is in ascending order
        # so we could get the len of `nums[i:]`
        # and check 
        
        # let's say the length is `5`
        # we want to confirm, that the five numbers in that slice
        # are the only five numbers greater than five
        
        # to confirm that check nums[i-1] if `i-1` is valid
        # if `i-1` is not valid, it means those are the only five numbers greater
        # than five
        # if `nums[i-1]` is less than `5`, it means those are the only five numbers greater
        
        
        # else keep going

        


    
arr = [
    [0,0],
    [0,4,3,0,4],
    [3,5],
    [0,3,6,7,7],
]
foo = arr[-1]
sol = Solution()
res = sol.specialArray(foo)
print(res)