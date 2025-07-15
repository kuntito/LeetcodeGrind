# https://leetcode.com/problems/jump-game-vii/

# what's the situation? i want to implement, `canReach`.
# it takes three arguments and returns a boolean.

# but what happens in between?
# `s` is a string containing 0s and 1s
# we're told that we start at index 0
# i.e. idx == 0

# and we can jump `idx + minJump <= otherIdx <= min(idx + maxJump, s.length - 1)`
# but what does this mean? 
# 
# for starters it means we can jump from`idx` to `otherIdx`
# the equality signs simply describe the nature of `otherIdx`

# it states `minJump <= otherIdx <= min(idx + maxJump, s.length - 1)`

# if we break it down, `minJump <= otherIdx`
# otherIdx is greater than or equal to `minJump`

# the second half of the description is `otherIdx <= min(idx + maxJump, s.length - 1)`
# which means `otherIdx` is less than or equal to `min(idx + maxJump, s.length - 1)`
# it makes sense to simply this before going further.

# `min(idx + maxJump, s.length - 1)`
# the minimum of `idx+Jump` and `s.length - 1`
# since, `s.length - 1` represents the last index in `s`

# the statement simply means we can't jump out of bounds
# going back to `otherIdx`

# `otherIdx` is such that is greater than or equal to `minJump`
# and less than or equal to `idx + maxJump` with the condition that `idx + maxJump` does not exceed the length of `s`

# in essence, we can only jump between a range of values.
# the question is, starting at zero, is it possible to jump to the end of `s`

# i.e. can we jump from s[0] to s[-1]

# actually, i'm slightly mistaken, the conditions for jumping are correct
# in the sense of `idx` to `otherIdx` where `otherIdx` is `minJump <= otherIdx <= min(idx + maxJump, s.length - 1)`

# but there's an extra condition, we can only jump to `otherIdx` if the value at `otherIdx` 
# is `0`

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        pass