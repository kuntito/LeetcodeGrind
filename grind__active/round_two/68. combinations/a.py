# https://leetcode.com/problems/combinations/

from typing import List

# i'm given two integers, `n` and `k`
# i'm to consider the range 1..n

# and return all unique subarrays of size `k`
# within that range.

# and how would this work?
# say i create the range..

# i'd start at the beginning..
# i'd iterate through every number in the range
# and find what subarrays start with that number

# the question doesn't say, but i'd imagine that duplicates can occur..
# well, not really..

# since, i'm defining the range of 1..n
# there are no duplicates..

# so what are we doing..
# say i have..
# [1, 2, 3], k = 2

# well, i'd start with `1`
# start a recursive call from the next index..

# right, it's recursion and backtracking..
# you'd have a tracking array
# and a result array..

# on each recursive call, you want to iterate from
# startIdx to the end..
# adding the current number to the tracking array
# and starting another recursive call

# the base case would be if you go out of bounds
# if you hit `len(trackingArr) == k`
# keep doing this till you explore the entire array

# what args does the recursive call need
# `startIdx`, `trackingArr`
# i can make `k` global
# make `arrRange` global
# make `resultArr` global

# error, for the base case..
# you want to check if len of tracking array is max len
# before checking if `startIdx` is out of bounds..

# reason being.. you could have a valid tracking array
# when `startIdx` is out bounds..

# in which case, you want to add this to the result array

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        pass
        startIdx = 0
        trackingArr = []
        
        self.resultArr = []
        self.maxLen = k
        self.numRange = list(range(1, n + 1))
    
        self.explore(startIdx, trackingArr)
        
        return self.resultArr
        
    def explore(self, startIdx, trackingArr):
        if len(trackingArr) == self.maxLen:
            self.resultArr.append(
                trackingArr[::]
            )
            return
    
        dim = len(self.numRange)
        if startIdx == dim:
            return
        

        
        
        for idx in range(startIdx, dim):
            elem = self.numRange[idx]
            
            trackingArr.append(elem)
            self.explore(idx + 1, trackingArr)
            trackingArr.pop()
            
arr = [
    [4, 2],
]
foo = arr[-1]
sol = Solution()
res = sol.combine(4, 2)
print(res)