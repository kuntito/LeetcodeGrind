# https://leetcode.com/problems/contains-duplicate-iii/description/

from typing import List


# i want to implement a function that returns a boolean.
# the function is called `containsNearbyAlmostDuplicate`.
# it receives three arguments, an integer array, `nums`, and two integers, `indexDiff` and `valueDiff`.

# we want to find out if there exists two indices, `i` and `j`, such that the absolute difference between the indices is less than `indexDiff` i.e. abs(i - j) < indexDiff

# several index pairs can fit the description. of the fitting pairs, we want to find out if at least one has values whose absolute difference are less than `valueDiff`.

# i.e. abs(nums[i] - nums[j]) < valueDiff.

# i suggest a sliding window of size `indexDiff`

# i'd move the sliding window rightwards till i reach the end.
# checking the numbers in the window if any of them have an absolute value difference less than `valueDiff`

# the moment i find one, return True.

# rewrite, TLE
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        pass
    
        left, right = 0, indexDiff
        
        self.nums = nums
        self.valueDiff = valueDiff
        dim = len(nums)
        while True:
            if self.hasValidValues(left, right):
                return True
            left += 1
            right += 1
            
            if right == dim:
                break
            
        return False
    
    def hasValidValues(self, left, right):
        # i want to explore every pair
        
        dim = len(self.nums)
        end = min(dim, right + 1)
        
        for i in range(left, end):
            valOne = self.nums[i]
            for j in range(i + 1, end):
                valTwo = self.nums[j]
                if abs(valOne - valTwo) <= self.valueDiff:
                    # print(valOne, valTwo)
                    # print(left, end)
                    return True
                
        return False
    
arr = [
    [[1,2,3,1], 3, 0],
    [[1,5,9,1,5,9], 2, 3],
]
foo, bar, baz = arr[-1]
sol = Solution()
res = sol.containsNearbyAlmostDuplicate(foo, bar, baz)
print(res)