# https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: list[int]) -> int:
        pass
        # each bar is only concerned with bars after it that are greater than itself
        # you can't expect to this check for every bar
        
        # scratch that
        # the idea is to use two pointers
        # initially set at the extremes of `height`
        
        # we calculate the area between them
        # and move one of the pointers towards the other
        
        # but which one?
        # we want to find the largest area
        # in between those indices
        # what would the largest area look like
        # well, it would definitely have heights long enough to offset
        # the loss of distance
        
        # in english please, the larger area would require it's pillars
        # to be higher than what we've seen so far
        
        # so which pointer do we move
        # ideally, both pointers would have to move to find a larger area
        # but we can't move both pointers at the same time
        # why not? consider:
        # [1, 20, 3, 20]
        # left = 1, right = 20
        # 
        
        
        # TODO
        
        # i know the answer is move the pointer with the smaller value
        # i just don't know how to justify it