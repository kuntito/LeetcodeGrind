# https://leetcode.com/problems/fixed-point/description/

# TODO, can you solve in log(n)?
class Solution:
    def fixedPoint(self, arr: list[int]) -> int:
        for idx, n in enumerate(arr):
            if idx == n:
                return idx
    
        return -1