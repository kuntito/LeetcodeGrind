# https://leetcode.com/problems/first-missing-positive/description/

from typing import List

# what's the situation?

# i'm given an integer array, `nums`

# i want to return the smallest positive integer that's not present in `nums`

# and what exactly does this mean?
# well, positive integers are number 1, 2, 3, 4, 5, 6, 7...

# so, i want to look in `nums`
# and return the smallest of the positive number sequence
# that is not in `nums`

# my default would be `1`
# but if `1` exists in `nums`, i'd default to `2`
# and `3` and `4`.. until i find the first number that's not in `nums`

# if i sort `nums`, this sorts out the situation.
# however, the question insists i do this in O(n) time
# and use O(1) space.

# the very things i do not need to solve this problem.
# to know the smallest positive integer, i need to see all the numbers in `nums`

# that's the O(n) bit..
# but then to know what numbers i've seen and what i haven't
# is where a `set` would  have been convenient..

# but that would be O(n) at most.

# so the real question is, how can you track the numbers you've seen
# without storing them?

# unless, there's some hidden trick.
# this is fundamentally impossible.

# i need space to store a seen numbers..
# am i losing the plot?

# okay, the hint says O(2n) = O(n)
# this alludes to going through the array twice..

# but how would repeating the same ineffective move twice..
# bring forth something different.

# perhaps, you're not doing the same thing twice?
# consider: [1,2,0]

# bruh, imma just look at the answer.

# one insight, Neetcode had is..
# worst case, the smallest positive integer
# could never exceed `len(nums) + 1`

# how so?
# imagine, every number in `nums` is a consecutive positive integer.
# and `nums` is size `2`
# his insight is, the highest our result can be is `3`

# how's this the case?
# if `nums` is size `2`
# we could have [1, 2]

# and the output would rightly be `3`

# okay but what if we had [4, 5]
# then the answer is `1`

# what if we had [10, 20]
# then the answer is still `1`

# `1` is always the smallest positive integer.
# the only reason, we don't pick `1` is if it exists in the array

# in which case, `2` becomes the next smallest..
# unless, it also exists in the array

# by extension, if every subsequent smallest integer exists in the array
# the only one that wouldn't would be `len(nums) + 1`

# okay, but does this help me solve the question..
# say i look for `len(nums) + 1` within the array
# and don't find it..

# what would this mean, it would mean `len(nums) + 1` is not in the array
# but your answer could still be `1`

# the insight is insightful but doesn't take me anywhere meaningful yet.

# i didn't get the official solution but i think i understand one
# after reading the editorial.

# the idea is to iterate through every number in `nums`
# for each number you find, we want to associate it with it's index.

# in our worst case array, every element would be one integer above it's index.
# i.e. [1, 2, 3] all correspond to index 0, index 1, and index 2

# we know the upper bound for our result is always going to be `len(nums)-1`
# so what we do is for every number we find, we'd place it at it's appropriate index

# which is `number - 1`
# but what if that index is already occupied..
# we take whichever number is there and place it where it should be..

# what if your number is `50` and len(nums) == 3
# then we can convert that slot to `None`.

# the idea here is every number has a slot or becomes `None`
# since the range is 1..len(nums) + 1

# worst case after iteration, 
# the entire array would be filled with numbers
# that way we know the answer is len(nums) + 1

# if not, the first None we encounter tells us the result.
# which would be `idx + 1`

# so a recursive swapping..
# yes.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for idx, n in enumerate(nums):
            if n is None or idx + 1 == n: continue
            
            # so now, i want to place the number at it's index, `n-1`
            self.place(idx, nums)
            
    def place(self, curIdx, nums):
        # what are the conditions for placing..
        # first off, the number must be between 1..len(nums) inclusive..
        # if not it has no slot..
        # and we can just set the current index to `None`
        
        number = nums[curIdx]
        if number < 1 or number > len(nums):
            nums[curIdx] = None
            return
        
        # if the number is within range, we grab it's proper index
        properIdx = number - 1
        # the idea is to assign `nums[properIdx]` to this number
        # if `properIdx` is occupied, call this function on `properIdx`
        # what if there are duplicates..
        
        # what do you mean..
        # say you wanna place `2` at index 1
        # you get there and find a `3`, so you place that `3` at index 2
        # you get to index 2 and find another `2`
        # so now you want to place that `2` at index 1..
        # but we see there's still a `3`
                
        # now we're back where we started..
        # this would be an infinte loop..
        
        # way this should go, the moment you realize
        # you're placing a number elsewhere..
        # you want to make it's previous spot vacant..
        # make it a None..
        
        # so for our example,
        # you wanna place `2` at index 1
        # whatever `2`s previous index was, you convert it to None
        
        # now we take `2` to index `1`
        # we realize, there's a `3` there
        # we convert that position to a None
        # and we take `3` to index 2
        # we get to index 2 and find another 2
        
        # we make index 2 vacant, take 2 to index 1
        # we get to index 1 and we find a None..
        
        # now we can place 2 there..
        # we backtrack and the original call places the same 2 in that index.
        
        # it works out.
        
        # so, first, set the current index to `None`
        nums[curIdx] = None
        
        self.place()