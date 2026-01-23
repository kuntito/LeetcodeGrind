# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# i'm given two things. a string, `s`, that only contains uppercase characters
# and an integer `k`

# i'm allowed to replace any character in `s` with any uppercase character i see fit.
# but i can only do that `k` times.

# but why would i want to do it in the first place?
# well, i'm supposed to find the longest substring in `s`
# that has the same characters..

# this is where the replacement comes in.
# say s = AABD
# and k = 1

# if i replace B with A, i can get AAA
# so the longest substring would be of length `3`

# right, so how would this go..
# the longest substring must start at a particular index
# our best shot of the longest substring would be starting at the first index.

# okay.. but what are we trying to do..
# well, we move forward..

# let's use an example 
# `ABAB`

# we start at A, longest substring now is `1`
# we move to AB, longest substring is now `2`, since we can replace one B with A

# but on further inspection, we can do two things here.. either replace B with A
# or replace A with B..



# it's a similar concept to
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass