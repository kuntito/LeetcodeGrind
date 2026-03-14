# https://leetcode.com/problems/split-array-largest-sum/description/

from typing import List

# what's the situation?
# i'm given two things, an array of integers, `nums`
# and an integer, `k`.

# what am i doing with them?
# i want to split the `nums` into `k` sub arrays
# such that no subarray is empty and the largest sum of any subarray is minimized.

# what does largest sum of any subarray is minimized?
# say `k` is `3`

# this would mean, i'd have to split `nums` into three parts
# three subarrays, each containing one or more values
# of these subarrays, one would have the largest total sum

# there's multiple ways, i can split.. `nums` into 3 parts
# and each of those ones would have their own largest subarray sum

# of all those largests, i want to return the smallest one.

# for notes, a subarray is a group of back to back elements of `nums`
# a single element is also a subarray.

# way i see it, i'd have to consider every set of splits.
# then find the minimum largest subarray sum.

# consider:
# nums = [1, 2, 3]
# k = 2

# i can split nums in the following ways
# [1] and [2, 3]
# [1, 2] and [3]

# in the first split, the largest subarray is [2, 3], a total of `5`
# the the second split, the largest subarray is [1, 2] and [3], they both total `3`

# in this case, my final answer would be `3`
# that's the smallest largest subarray split.

# i don't see a way without exploring all splits.
# i can't sort the array, so i'd have to take it as it is.

# so how would the function go?
# i'm thinking recursion..

# if `k` is more than `1`
# i'd start the first subarray with `1` element
# then start a recursive call with `k-1` and `restOfNums`

# at which point, i'd repeat the same logic.
# when `k` becomes `1`, i know to take the entire array as is

# i'd say, it's at this point, i can know the largest subarray
# in the current path.

# yeah, but how would the tracking of that value go?
# if you go back to the root call..

# to form the first subarray,
# say you pick `1` element, you'd have one largest subarray after exploration.
# say you pick `2` elements, you'd have another largest subarray after exploration.

# i'd say the final decision, the decision to determine the smallest
# largest, should be done at the root call.

# each subarray split returns it's largest subarray sum in it's path
# and you can compare all to know which one is the smallest.

# which would mean what?
# each recursive call returns the the largest split it'd seen so far.

# the base case, k == 1, would return the sum of the array slice at that point
# it's parent call, would compare the sum of it's own array slice with what the base case returned.
# and the parent call, would return whichever is bigger of the two.

# i see an opportunity for memoization here..
# a combination of `starting index` and `k`

# we would always do the same thing, if we had the same `starting index`
# and the same `k`

# but in what scenario would this be useful?

# [1, 2, 3, 4, 5]
# i don't know how it could happen though?

# for you to have `k` at a value, it must mean `x` amount of splits preceeded it.
# there's only one unique way to have `x` amount of splits before hitting `k` splits left

# what comes before and what comes after must sum up to the initial `k`
# not sure memoization helps here.. but let me write without it
# see what happens

# what would i need..
# not much really..

# recursive function needs

# startingIndex
# splitsLeft

# and the root call..
# iterate through 1..k splits.. determine the largest along each path
# use a variable `smallestLargestSplit` to compare the results

# return `smallestLargestSplit`

# error, in the recursive call..
# while exploring every subarray size.. from 1 element to however many..
# i'd used `count` as the name for the iterator..

# i was iterating from (startIdx, ..)
# the concern here.. was `for count in (startIdx, ...)`
# wasn't descriptive..

# i'd done it in the root call and that worked, 
# because the loop was `for count in range(1, ...)`

# but for the the recursive call..
# i was iterating from the index onwards.. so the iterating variable is
# the current index, the count would be `currentIndex - startIndex`


# TODO not sure, if it'd be more efficient if i used slices
# as opposed to passing indices, try this too..

# TODO, the code fails this test case
# `[2,3,1,2,4,3]`
# k = 5

# the answer should be `4`, my code returns `5`

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k == 1:
            return sum(nums)
        
        # what's the range for the first exploration
        # if you have `k` splits.. it means you can
        # take a subarray of size `1` up to.. worst case..
        
        # worst case is every other subarray gets one element
        # in which case, len(nums) - (k - 1)
        # that's the biggest subarray you can take.
        
        # so selection range at any point is
        # `1` until len(nums) - (k-1)
        
        smallestLargest = None
        
        maxSelection = len(nums) - (k - 1)
        for count in range(1, maxSelection+1):
            # so if we select `count` from the array
            # we'd have nums[count:] left.
            currentSelection = nums[:count]
            
            largestHere = self.explore(count, nums, k - 1)
            
            largestHere = max(
                sum(currentSelection),
                largestHere
            )
            
            if smallestLargest is None:
                smallestLargest = largestHere
            else:
                smallestLargest = min(
                    smallestLargest,
                    largestHere
                )
                
        return smallestLargest
        
    
    def explore(self, startIdx, nums, splitsLeft):
        if splitsLeft == 1:
            return sum(nums[startIdx:])
        
        # here, same thing, we can make `1` selection
        # up until (how many elements left in nums - (splitsLeft-1))
        elemsLeft = len(nums) - startIdx
        maxSelection = elemsLeft - (splitsLeft-1)
        
        largestAlongPath = None
        
        endRange = startIdx + maxSelection
        for curIdx in range(startIdx, endRange):
            
            curSelection = nums[startIdx: curIdx + 1]
            
            largestHere = self.explore(
                curIdx + 1,
                nums,
                splitsLeft - 1
            )
            
            largestHere = max(
                largestHere,
                sum(curSelection)
            )
            
            
            if largestAlongPath is None:
                largestAlongPath = largestHere
            else:
                largestAlongPath = max(largestAlongPath, largestHere)
                
        return largestAlongPath
    
arr = [
    [[1,4,4], 3],
    [[2,3,1,2,4,3], 5],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.splitArray(foo, bar)
print(res)