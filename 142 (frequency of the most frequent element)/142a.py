# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/

class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        pass
        # brute force approach
        # sort `nums`
        # iterate backwards
        # on each iteration
        # determine the average of `slice = arr[:idx]`
        # if `k/slice + average of slice == arr[idx]`
        #   track the result as the (len of slice + 1)
        # if the condition does not match
        #   increment the left pointer of the slice and recalculate
        
        # once all slices have been explored
        # move the right pointer forward