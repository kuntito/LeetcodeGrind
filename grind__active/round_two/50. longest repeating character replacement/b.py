# https://leetcode.com/problems/longest-repeating-character-replacement/description/

# i'm given two things. a string, `s`, that only contains uppercase characters
# and an integer `k`

# i'm allowed to replace any character in `s` with any uppercase character i see fit.
# but i can only do that `k` times.

# but why would i want to do it in the first place?
# well, i'm supposed to find the longest substring in `s`
# that can have the same characters..

# say i have
# s = AABD

# the longest substring with the same characters is AA
# but it can be longer..

# this is where `k` comes in

# say s = AABD
# and k = 1

# if i replace B with A, 
# i can get AAA
# so the longest substring would be of length `3`

# right, so how would this go..
# the longest substring must start at a particular index
# our best shot of the longest substring would be starting at the first index.

# okay.. but what are we trying to do..
# well, we move forward..

# let's use an example 
# `ABAB`
# k = 2

# we start at A, longest substring now is `1`
# we move to AB, longest substring is still `1`

# but since k=2, we can replace either character
# either replace B with A, and get `AA`
# or replace A with B, and get `BB`

# let's consider both scenarios..
#   say we replace B, and now have AA
#   we move on and have `AAA`
#   looks like a good choice

#   say we replaced A, and now have BB
#   we'd have moved forward to get to BBA
#   and now have to spend another replacement,
#  for now it seems like the A replacement was the good choice..

# i'm not sure i should continue with this line of reasoning..
# i have an intuition for the solution, i just don't know how to work my way to it..

# what i should be doing is grab a sliding and expanding window..
# starting at the first index..
# the property i care about in the sliding window is..
# it's length.

# it's should never have more replacement gaps than `k`
# okay, but what are you replacing..
# well, the most frequent number in the window..

# the idea is you always track, the most occuring element in the window.
# based on this, you know the amount of gaps left in the window..
# if the gaps ever exceed `k`, shrink the window until, it's stable again

# the question would be how would you track the most occuring element
# could use a hashmap, and a variable, `mostFreqElem`
# with every element we add to the hashmap, we compare it's frequency with `mostFreqElem`
# and update where necessary..

# and if the gap is insufficient..
# we reduce the window from the left..
# meaning, we'd need a left pointer for the window..
# yes,
# but how do you still track the most frequent element if you're removing from the left?

# what do you mean?
# consider:
# `AACBB`
# where so far, you've kept `A` as the most frequent element
# k = 3

# so the window works out, next element is a `D`
# `AACBBD`
# so now, you're at a deficit,
# most frequent element is `2`, k is `3`, window is `6`
# you need to shrink the window.. starting from the left.

# you take out A
# now, you have, `ACBBD`
# technically, this window is valid..
# because, now the most frequent element is B, occurs twice
# and the gaps equal `3`

# but the question is.. how do we know it's B..
# do we iterate through the entire dictionary again..

# peeped Neetcode's video.
# we don't need to know it's B..
# we only care, that we've removed the copies of A that make the window invalid

# which would leave us at `ACBBD`
# at this point, the max frequency we've seen is .. `2`
# meaning our max window is `5`

# knowing this we keep shifting the window
# at first, we try to expand the window, can it become 6?
# well, we check the new entry, does this cause our max frequency
# to become greater than A's frequency, if not..

# we shift the window.. if we do find a value that increases max frequency
# we update the maxFreq and window length..

# in summary, we increase the window until we can't no more
# tracking what max frequency is..
# no need to shrink the window, since we're optimizing for the longest substring..

# we only need to maintain it's current size and check if we add
# any more elements that increase the max frequency.

# it's a similar concept to
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass
        # let's ball,
        # what do we need..
        # leftPointer
        # slidingWindow dictionary
        # maxFreqElem
        
        # we're iterating through every character in `s`
        # so what are we doing.. we add a character to `slidingWindow`
        
        # if character frequency is greater than max frequency
        # and len(window)..
        
        # actually this logic only kicks in when we have to shrink the window..
        # at first, we're simply just adding elements
        # while the window is valid..
        
        for idx, ch in enumerate(s):
            pass