# https://leetcode.com/problems/sliding-window-maximum/

from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        # iterate through the first window
        # note the highest number
        # store numbers in the max heap
        
        # start iteration from the number after the first window's last number.
        
        # remove the earliest number
        # if it's at the top of the heap, pop it.
        # if not, add it to a set `to_be_removed`
        
        # then add the new number to the maxHeap
        # update largest number.
        # the update should always take the first number from the maxHeap
        # that's not in `to_be_removed`