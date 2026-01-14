# https://leetcode.com/problems/contains-duplicate-ii/description/

# we're given an array of numbers called `nums`
# we want to find out if the array, `nums`, has two different slots
# containing the same value

# and the indices of both slots, their absolute difference is less than or equal to a given number `k`

# in simpler terms, we're given two things..
# an array of numbers, `nums`
# and an integer `k`

# we want to find out if, within `nums`, there are two indices, `i` and `j`
# whose absolute difference, `abs(i - j)`, is less than or equal to `k`

# and not just that, the values at `i` and `j`, need to be the same.
# i.e. `nums[i]` == `nums[j]`

# it's sounding like a nested iteration
# for each index in `nums`, we explore the next `index + k` indices
# we start our exploration from `index + 1` up until `index + k`, where `index + k` is inclusive
# this second iteration is our `j`

# once, we find two values that match, return True
# else, we keep going..

# Time Limit Exceeded, 'nother solution
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dim = len(nums)
        
        for i in range(dim):
            endRange = min(
                dim,
                i + k + 1,
            )
            for j in range(i + 1, endRange):
                if nums[i] == nums[j]:
                    return True
        
        return False