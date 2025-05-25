# https://leetcode.com/problems/brightest-position-on-street/description/

from collections import defaultdict
from typing import List

# i want to implement a function `brightestPosition`
# it takes a 2d integer array, `lights` and returns an integer

# each element of lights is a list of 2 integers, (position, range)

# position indicates a integer on a number line
# that number can be said to represent a lightbulb
# a lightbulb at `position` and covers the range `(position-range, position+range)`

# our job is to find the brightest position on that number line
# what position has the most lights on it

# if there are multiple of such positions, we should return the smallest one

# right, so how would this work
# i thinking of a double loop solution
# where for each light, i explore all the numbers in it's reach

# use a hashmap to store each number and increment it's count for every time the light touches that position

# i'd also keep a global variable to check for the most lit position so far
# let's see if it works

# TODO memory limit exceeded
class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        pass
    
        # sort lights based on starting position
        lights.sort()
    
        mostLit = None
        posMap = defaultdict(int)
        
        for startPos, rng in lights:
            for pos in range(startPos - rng, startPos + rng + 1):
                posMap[pos] += 1
                
                if mostLit is None:
                    mostLit = pos
                elif posMap[pos] > posMap[mostLit]:
                    mostLit = pos
                    
        return mostLit
    
arr = [
    [[-3,2],[1,2],[3,3]],
    [[1,0],[0,1]],
    [[1,2]],
    [[5,2],[-4,2],[1,1]],
]
foo = arr[-1]
sol = Solution()
res = sol.brightestPosition(foo)
print(res)