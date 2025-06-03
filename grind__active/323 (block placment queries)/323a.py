# https://leetcode.com/problems/block-placement-queries/description/

from typing import List

# there's a number line
# that starts at zero and goes on till positive infinity

# there's a two type of queries
# type 1 - [1, x]
# type 2 - [2, x, sz]

# for type1 queries i.e. [1, x]
# when called, i should build an obstacle at distance `x` from the origin `0`
# they've guaranteed that when the query is called, there would be no obstacle at distance `x`

# in english, mark the position `x` with a value
# since, the number line is positive, every `x` is always from the origin

# for query type 2 i.e. [2, x, sz]
# i want to know if i can place a block of size `sz` anywhere in the range
# (0, x)

# a block cannot intersect with any obstacle but it may touch it.
# in english, say we have a query type 1 [1, 5]

# we can represent the number line as:

# 0, 1, 2, 3, 4, 5
# -, -, -, -, -, &

# where `&` represents the obstacle.
# say we have a query 2, [2, 5, 3]
# it means i want to place a block of size `3`
# in the range (0, 5)
# which also happens to be the range of our type 1 query

# a block of size `3` requires `3 + 1` consecutive free spaces
# so i could do (0, 3) or (1, 4) or (2, 5)

# note `(2, 5)` touches the obstacle but it doesn't cross it.
# touching is acceptable but don't cross

# i want to implement a function `getResults` that takes an array of queries, both type 1 and type 2 queries in the same array.
# 
# my job is to return a boolean array with the same size as the queries array
# such that for every type 2 query that is successful i.e. the block is placed without crossing obstacles

# the result at that index should be `True`
# every other value should be `False`, type 1 queries and unsuccessful type 2 queries

# ok. how to implement this?
# for one, i'd need to track the obstacles.
# i'd use an array for now.

# storing shouldn't be difficult.
# the problem is figuring out if there's enough consecutive slots to place 
# a type 2 query block.

# consider t2q of [2, 3, 3]
# the first element just tells me it's a type `2` query
# my concern is the second and third elements

# in this case, i want to place a block of size `3`
# in the range (0, 3)

# in this case, the range is the same size as the block
# i'm seeing three possibilities.

# range > block
# range == block
# range > block

# if range is less than block, automatic false
# if range is equal to block, return `obstacle in range`
# if range is greater than block, ???

# `range > block` is just a collection of `range == block`
# so if you can figure out `obstacle in range`

# you can solve this

# given a range where the two end points match the block size.
# what would make that range valid?

# well, if no obstacle exists within it.
# how would you find out if no obstacle existed within it?

# search through every position? okay

# i think we can solve it? place all obstacle indices in a `set`
# for every type2, we check if range < block and return False
# if it is the case

# else, we can combine `range == block` and `range > block`
# using a sliding window of size block that moves through range 

# TODO TLE 
# 738 / 744 testcases passed
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        
        self.obstacleMap = set()
        res = []
        
        for type, *rest in queries:
            
            # place obstacle in hash set for O(1) access
            if type == 1:
                idx = rest[0]
                self.obstacleMap.add(idx)
            else:
                flag = False
                idx, blockSize = rest
                if self.canPlaceBlock(idx, blockSize):
                    flag = True
               
                res.append(flag)
            
        return res
    
    def canPlaceBlock(self, idx, blockSize):
        if blockSize > idx:
            return False
        
        start = 0
        for end in range(blockSize, idx + 1):
            if not self.hasObstacle(start, end):
                return True
            start += 1
            
        return False
    
    
    def hasObstacle(self, start, end):
        # i intentionally end the range at `end` not `end + 1`
        # because an obstacle at the tail end does not prevent a block from being placed
        # that said i shoud do (start + 1, end) instead
        # since an obstacle at `0` doesn't prevent block placement
        for idx in range(start + 1, end):
            if idx in self.obstacleMap:
                return True
            
        return False
    
arr = [
    [[1,2],[2,3,3],[2,3,1],[2,2,2]],
    [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]],
]
foo = arr[-1]
sol = Solution()
res = sol.getResults(foo)
print(res)