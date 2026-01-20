# https://leetcode.com/problems/combination-sum/

from typing import List

# i'm given two things, an array of integers, `candidates`
# and a number, `target`

# i want to find all the ways i can combine the integers in candidates
# so they sum up to `target`

# when done, i'd return the list of these combinations.

# for example
# candidates = [2, 3, 5]
# target = 5

# there's two ways i can combine elements to get `5`
# they are [2, 3] and [5]

# okay.. so how would this go..
# well, i can start with each element.

# iterate through candidates..
# for each one, i want to find out what other numbers it can combine with to form `target`

# sorting is helpful for this kind of thing..
# it helps me, since, once i start at one number
# i'd know the subsequent numbers can only get larger

# how does this help you?
# well, it helps shorten the iteration..
# say, i start with `2` and want to get a `5`
# the moment, i find `3`, i can stop the iteration
# because i know the `candidates` array is sorted.

# if it wasn't sorted.. i could still continue the iteration
# in case i find three `1`s

# that makes sense..
# right, how do you handle duplicates..
# what do you mean?

# consider:
# candidates = [2, 2, 2]
# target = 4

# using my approach, i'd get [2, 2] and [2, 2]
# that's not a unique combination.

# it seems i should only start from a number once..
# once i start the `2` iteration
# i'd find every combination that ends up with `target`

# makes sense..
# so do you want to track all the numbers you've started from.
# that's certainly an approach, let's go with it..

# i know there's a more optimal one but let's see how it goes.

# how do you deal with multiple combinations starting with the same thing.
# i.e.
# candidates = [2, 2, 2, 4]
# target = 6

# one combination is [2, 2, 2], another is [2, 4]
# think, the way this'd work is once i pick the first two..
# i try to combine with every next index..

# what do you mean..
# the first two is at index = 0

# so the first recursive call, i'd compare 
# `curIdx = 0 with nextIdx = 1`
# in that same recursive call..

# scratch that..
# for each recursive call..
# i'd have the start..

# scratch that..
# each recursive call i'm doing the same thing
# as the parent call

# the parent call is iterating through all of candidates..
# for each element, you deduct said element from target

# start another recursive call with the new target
# newTarget = target - elem

# inside the new call, you repeat..
# worth pointing out, candidate cannot be negative..
# if negative, return

# if zero, you've hit base case..
# track the combination you took here..

# means, i'd need a tracking array.
# this is a recursive backtracking question..


# how about this situation..
#  candidates = 2, 2, 2, 2
#  target = 4

# your idea to use a set wouldn't work here
# if you've said you started with `2`
# and can't start with `2`
# again, how doesn't that work..

# how do you define start..
# the base call..

# well, yes, but you'd still run into the same problem..
# after base call

# you're left with [_, 2, 2, 2]
# which means you can still combine with every other two..

# how'd you do it last time..
# the way it worked.. was for each element, 
# if the next element was the same, we moved current index forward until
# the next element was a different one..

# and how does that help the situation..
# um, let's restart

# [2, 2, 2, 2], base call, target = 4
# you start at 2
# what do you do, a recursive call..

# now, you're at [_, 2, 2, 2], target = 2
# you start another recursive call

# now, you're at [_, _, 2, 2], target = 0
# base case, append [2, 2] to tracking array..
# 

# come back to [_, 2, 2, 2], target = 2
# pop the last element you added, the `2` and `idx = 1`
# now, here's where the magic is..
# the next element you explore wouldn't be a `_, 2`
# you move the current idx forward until it's no longer a `2`

# in this case we'd exhaust the array, and can no longer go anywhere
# so we return to [2, 2, 2, 2], target = 4, trackingArr = [[2, 2]]

# and the same thing happens here.. curIdx's value is `2`
# we move it forward until, next value is no longer `2`
# in this case we explore the entire array..

# and we're done, this way, we'd only have [2, 2] in our tracking array
# okay, but what about a situation where a combination is multiple `2`s
# this situation handles it..

# every recursive call, allows you to add another of the same value
# but only that..

# so even if you had a combination like [2, 2, 2, 2, 2]
# it just means you'd have five recursive calls to get there but no more..
# and if you had [2, 2, 3]
# the fact that you move current index until the next element is different would handle this..

# even if you had [2, 2, 3, 3], it still works, just that each `2` and each `3`
# is added in it's own recursive call, technically, every element is added in it's own recursive call

# not sure, why i'm using that distinction.

# so what do we need.. first off, while loop over for loop
# allows you easily move curIdx

# that said, we need:
# * tracking array
# * result array
# * curIdx
# * target

# that's it..

# one more base case, curIdx going out of bounds..
# this should be checked before checking if target == 0
# hold up, can target be negative.. nah, it can't
# that could've changed the situation..

# we're checking target == 0 first
# because this could be True when curIdx goes out of bounds
# and if didn't check it first, 
# we'd have returned before acknowledging we found a combination

# but i think the while loop handles this..
# the while loop ensures curIdx stays within bounds
# let me finish the function then tweak this description..

# yes, the while loop handles curIdx out of bounds..
# since i never access curIdx's value out of the while loop
# this is safe..

# one more thing, i misread the question..
# need to pay more attention to this.. i was optimizing for something that didn't exist..
# question said all elements in `candidates` are distinct
# so there was no need for the future check of nextElem being different from current element

# also, each element can be used multiple times..
# so each recursive call shouldn't be `curIdx + 1`, it should just be `curIdx`

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        self.resultArr = []
        self.candidates = candidates
        
        trackingArr = []
        curIdx = 0
        self.explore(target, curIdx, trackingArr)
        
        return self.resultArr
    
    def explore(self, target, curIdx, trackingArr):
        if target == 0:
            self.resultArr.append(trackingArr[::])
            return
        
        dim = len(self.candidates)
        if target < 0:
            return
        
        while curIdx < dim:
            curVal = self.candidates[curIdx]
            
            trackingArr.append(curVal)
            self.explore(
                target - curVal,
                curIdx,
                trackingArr
            )
            trackingArr.pop()
            
            # # while the next index is valid and the next value is the same as current value..
            # while curIdx + 1 < dim and self.candidates[curIdx + 1] == curVal:
            #     curIdx += 1
            
            curIdx += 1
            
arr = [
    [[2, 3, 6, 7], 7]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.combinationSum(foo, bar)
