# https://leetcode.com/problems/brightest-position-on-street/description/

from collections import defaultdict
from typing import List
import sys

# i want to implement a function `brightestPosition`
# it takes a 2d integer array, `lights` and returns an integer

# each element of lights is a list of 2 integers, (position, range)

# position indicates a integer on a number line
# that number can be said to represent a lightbulb
# a lightbulb at `position` and covers the range `(position-range, position+range)`

# our job is to find the brightest position on that number line
# what position has the most lights on it

# if there are multiple of such positions, we should return the smallest one

class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        d = defaultdict(int)
        
        for i, dis in lights:
            d[i - dis] += 1  # index at left-end starts covering
            d[i + dis + 1] -= 1  # next index of right-end stops covering
            
        cur, max_idx, max_val = 0, -1, float("-inf")
        
        for idx, val in sorted(d.items()):  # sort by key would be sufficient
            cur += val
            if cur > max_val:  # count maximum brightness
                max_val, max_idx = cur, idx
        return max_idx
