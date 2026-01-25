# https://leetcode.com/problems/combination-sum-ii/

from typing import List

# i'm given two things..
# a list of integers, `candidates`, and..
# a an integer `k`

# i want to find all the unique ways i can combine the numbers in `candidates` to form `k`
# for instance, 
# candidates = [2, 3, 5]
# k = 5

# i can use [2, 3]
# i can use [5]

# how about ..
# candidates = [2, 2, 2, 2]
# k = 4
# in this case,
# i can only use [2, 2]..

# every other two proves nothing useful..
# so how do i approach this..
# for one, i'd say sort the numbers..

# it's easier for me to think of a solution this way..
# it's hard to reason from first principles on this one..
# since i know what the answer looks like..

# in essence, i'm sorting, `candidates`
# and the question is..
# for each candidate, can i get to `k` sum with the other elements in the array..

# i think sorting also helps with damage control..
# if k = 10 and the current candidate is `11`
# because i've sorted, i know there's no way i can combine `11` with any other number in the array
# to form `k`

# negatives don't count since they're not in the array..
# even if they were, the array is sorted.. so every number to right is in
# increasing order..

# okay..
# so what are you doing with each candidate..
# well, i'd deduct candidate from the target, `k - candidate`
# and basically restart the process

# starting at the next number after candidate..
# can i make `k-candidate`..

# this lends itself naturally to recursion..
# okay...
# you keep going till you hit the target..
# or run out of candidates..

# either way you want to keep track of all the elements you found along the way..
# so a `trackingArray`

# but how do you deal with something like..
# candidates = [1, 1, 1, 2], k = 3

# well, we'd start with `1`, k = 2
# next recursive call would be..
#   candidates = [_, 1, 1, 2], k = 2
#   we'd do the same thing, take the next `1`
#   next recursive call would be ..
#       candidates = [_, _, 1, 2], k = 1
#       we'd do the same thing and take the next `1`
#       the next recursive call would be ..
#           candidates = [_, _, _, 2], k = 0
#           at this point k = 0, we save the tracking array. it'd contain [1, 1, 1] here..
#           then go back to parent function..
#       and pop the last element we added, we've explored it, we can let it go..
#       tracking array is currently [1, 1], k = 1
#       the next element here is `2`
#       `2` is greater than k so we don't explore..
#       we can actually explore, realize `k` is negative and have a base case that addresses that..
#       well, i guess this works and is probably cleaner
#       i wanted to run into a problem i don't think i'd find with this example..
#       i'd try again..

# consider
# candidates = [1, 1, 1], k = 2
# for this, we'd select `1, start recursive call with `k-1` and the rest of the array
#   candidates = [_, 1, 1], k = 1
#   we'd select `1`, start recursive call with `k - 1` and the rest of the array..
#       candidates = [_, _, 1], k = 0
#       we'd realize k = 0, base case, append tracking array, `[1, 1]`.. return to parent call
#   back in parent call..
#   candidates = [_, 1, 1], k = 1, since i've explore the `1` at index `1`
#   the rest of the array is now [_, _, 1]
#   this is where trouble emerges.. 
#   i can select the next `1`, but i'd end up with [1, 1] which is not a unique combination..
#   the last tracking array was [1, 1]


# the consensus from my last crack at this.. is once you explore a number..
# you only want to explore the next different number..

# so in the root iteration of [1, 1, 1, 2]
# once i start the recursion of the first `1`.. my next number should be `2`

# okay, but how do you address the situation where you need multiple `1`s
# the details of the recursion allows you do that..

# it allows you to pick the first number
# but avoids the next number, if it's the same as the first number..
# so if you needed three `1s`

# you'd get it at the third recursive call..
# so that way, 

# it's as if you're checking every possible combination of the repeated number..

# the first time.. it's 
# [1].. against every other number that's greater than `1`
# the second call deep.. it's
# [1, 1].. against every other number that's greater than `1`
# the third call deep.. it's..
# [1, 1, 1].. against every other number that's greater than `1`
# and we keep going..

# right, let's do this..
# recursion arguments:
# curIdx, target, trackingArr, candidates, target, resultArr..
# we can make resultArr global..

# i've called the target number `k` throughout my explanation..
# but really, it's `target`

# made an error, 
# i didn't sort the array before writing the rest of the code..


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.resultArr = []
        
        curIdx = 0
        trackingArr = []
        self.explore(curIdx, target, trackingArr, candidates)
        
        return self.resultArr
    
    def explore(self, curIdx, target, trackingArr, candidates):
        if target == 0:
            self.resultArr.append(trackingArr[::])
            return
        
        if target < 0:
            return
        
        dim = len(candidates)
        while curIdx < dim:
            curElem = candidates[curIdx]
            if curElem > target:
                break
            
            trackingArr.append(curElem)
            self.explore(
                curIdx + 1,
                target - curElem,
                trackingArr,
                candidates
            )
            trackingArr.pop()
            
            # next index is the index with a different element to curElem
            while curIdx + 1 < dim and candidates[curIdx + 1] == curElem:
                curIdx += 1
            curIdx += 1