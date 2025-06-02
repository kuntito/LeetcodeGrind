# https://leetcode.com/problems/greatest-common-divisor-traversal/

from typing import List

# we have an array of integers, `nums`
# we want to explore every distinct pair of indices in `nums`

# and return a boolean if they all match a certain condition.

# the condition, for every pair of indices (i, j) where i != j
# we want to find out if we can travel from `i` to `j`

# but, we travel in a specific way. to travel from one index to another,
# the values at both indices, source and destination must have a greatest common divisor that's greater than `1`

# you can go from `i` to `j` directly if they have a gcd > 1
# or you can hop between intermediary indices to get to `j`

# consider the following:
# nums = [2, 6]
# there's only one pair (0, 1)
# you can travel from nums[0] to nums[1] because they have a gcd > 1 which is `2`

# also consider:
# [2, 3, 6], there's three pairs of indices (0, 1), (0, 2), (1, 2)
# but we'd zero in on the first pair `(0, 1)`

# the values at nums[0] and nums[1] are `2` and `3` respectively
# their greatest common divisor is `1`
# therefore, you can't directly travel between them

# however, you can go from `nums[0] => nums[2] => nums[1]`
# i.e. 2 => 6 => 3

# how would i implement this?
# i think a graph would suffice

# a graph of every index
# each node is an index and it's neighbours are the indices with whom
# it has a gcd > 1 with

# this way, i can explore every pair
# and check if i can go from `i` to `j`

# might be inefficient but it's a start

from collections import defaultdict
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        
        graph = self.getGraph(nums)
        
        for k, v in graph.items():
            print(k, v)
        
        
    def getGraph(self, nums):
        graph = defaultdict(list)
        
        dim = len(nums)
        for idxOne, numOne in enumerate(nums):
            for idxTwo in range(idxOne + 1, dim):
                numTwo = nums[idxTwo]
                
                if self.hasGcd(numOne, numTwo):
                    graph[idxOne].append(idxTwo)
                    graph[idxTwo].append(idxOne)
                    
        return graph
    
    def hasGcd(self, uno, dos):
        for cand in range(2, min(uno, dos) + 1):
            isUnoFactor = uno % cand == 0
            isDosFactor = dos % cand == 0
            
            if isUnoFactor and isDosFactor:
                return True
            
        return False
    
arr = [
    [2, 3, 6],
]
foo = arr[-1]
sol = Solution()
sol.canTraverseAllPairs(foo)
