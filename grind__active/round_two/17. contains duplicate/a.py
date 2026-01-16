# https://leetcode.com/problems/contains-duplicate/

from typing import List

# we're given an array of numbers and want to return True
# if the array contains any duplicates
# else False...

# a set works nicely for this since.. the approach is to iterate
# through and track all elements seen..

# but first check to see if said element exists..
# if it does, duplicate found.. else add it to the set
# if iteration completes, there were no duplicates, you can return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
    
        return False