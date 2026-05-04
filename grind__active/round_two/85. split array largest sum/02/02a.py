# https://leetcode.com/problems/split-array-largest-sum/description/

from typing import List


class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # and how would this go?
        # well, i want to explore every way i can pick the first chunk
        
        # how big can the first chunk get?
        # well, i'd assume, the biggest it can get is when
        # every other chunk is of size 1
        
        # so if i assume every other chunk is size 1
        # and take those out, whatever's left of k is the biggest size for that chunk
        
        
        maxSize = len(nums)
        maxChunkSize = maxSize - (k-1)
        
        # so, i have max chunk size
        # now, i want to explore every first chunk
        # starting from the one with size `1`
        
        for sz in range(1, maxChunkSize + 1):
            chunk = nums[:sz]
            chunkSum = sum(chunk)
            
            # now, i have the first chunk
            # what next? i want to find the next chunk
            # how would that go..
            
            # well, at this point whatever's left of the array
            # i want to explore every next chunk and see what happens..
            
            # this scenario, is similar to my starting conditions
            # difference is the start of the array...
            # and one less chunk to worry about..
            
            # i can call this function on itself..
            # and the base case?
            
            # when mazSize is `1`
            
            # okay, but what am i doing in this exploration..
            # i want to track the largest sum i've seen...
            # and how would this work?
            
            # i can pass the chunk sum through every recursive call
            # and when i reach the base case, i'd know i have seen the sum for the largest chunk
            
            # and i can store it, or at least..compare it with the other largest sums
            # and see which is the smallest.
            
            # it'd help if the recursion wasn't on the function itself
            # why not, i think, it's simpler to declare the global smallest max sum
            # in the main function and have something else that recurses.
            
            # if i placed the global smallest max sum in here, how would it go?
            
            # i'm not ready to find out..
            # let me just start with this.. 