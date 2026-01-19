# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# i'm given a string `s` and want to find the longest substring in `s`
# that doesn't have duplicate characters..

# how would i go about this? i'm thinking sliding window...
# be more explicit..

# i'm thinking about two pointers, what's wrong with sliding window..
# you're taking a shortcut..

# okay, i want to find the longest substring..
# it would have a start point and an end point..

# the longest substring would be the string itself..
# why can't i just do that..

# well, you don't know if it has duplicates until you explore the entire string..
# and i'm not to excited bout this approach..

# what, you'd start at the extreme ends and work your way inwards? yes.
# and what if you find duplicates.. i briefly had a snapshot of what this'd be like..
# and it's uncomfortably complicated to think about.. so i'd stop exploring..

# a simpler approach, is i know the substring must start somewhere..
# why am i beating around the bush.. i know this is sliding window..

# be patient.. every substring must start somewhere..
# okay, so iterate through the string, `s`
# the question is at each characrer is, what's the longest substring starting here..
# that has no duplicates..

# and how would this go..
# a helper function, well you could..
# you'd use a dict to track the characters.. a set is a better choice..
# less storage.. we only need the characters..
# okay, so a set to track all chars from that index onwards..
# moment we see a duplicate we stop tracking..

# the length of the set is the length of the substring..
# we return this to parent function..
# we'd need a tracker to know the longest substring..

# so, every character, we'd do this and track the longest..
# is there any repeated work.. a few.. well, just one, but it could occur multiple times..

# consider:
# "abdac"

# the first substring check would start at "a" and would continue up until "abd"
# the second substring check would start at "b" and would continue up until "bdac"
# the repeated work here.. is the "bd", we've already tracked it with the check from "a"
# and now, we do it again, with the track from "b", we're doing it again..

# it's starting to become apparent why there's a sliding window..
# so say the substring is at "abd", how do i know to slide..
# well, you stopped at "abd" because the next char is a duplicate..

# so what do we do..
# we need to ensure the tracking substring removes that duplicate..
# and how would we do that..
# what's the duplicate.. "a"
# so we remove "a"

# but do we know where "a" is at this point..
# i mean, we can see it but in code..
# well, we know that the value at `curIdx` exists in `trackingSubstring`
# we know where `trackingSubstring` starts... 
# the idea here is to remove every character from the start of `trackingSubstring`
# until the value `curIdx` no longer exists in `trackingSubstring`..

# it works well for this test case, `abdac`
# and effectively allows us to start another substring iteration from "b"
# however, what if "a" was in a different position

# say "badac"
# okay.. this is a different example..
# yes, but my point is the duplicate is not at the start..

# well, yes.. we'd start at "b" keep going and stop at "bad" because the next char is a duplicate..
# so we remove every first character until this is no longer the case..

# so we'd remove "b", "ad" still has an "a"
# we'd remove "a", now "d" no longer has an "a" and we can continue with the iteration..

# right, this is what i wanted to explore..
# the base algorithm.. was start a substring check starting on every character..
# but with this, 

# our starting string was "badac"

# we started at "b", ran into duplicate, solved it
# and now we're starting at "d"
# we've skipped the check from "a"

# well, yes, but technically, we've also checked it..
# how so.. the check from "b" included the check from "a"
# the moment we ran into a duplicate "a"(index 3), it nullified both checks..

# so we're allowed to start at "d"

# check it, what happens if you did start at "a" (index 1)
# the furthest you'd get is "ad", and we're back where we started..

# the sliding window allows us check from multipl starts
# and we're always optimizing for the earliest start since that gives us the best
# chance at hitting the longest if it exists...

# hence... okay.. i see why it works..
# so during all this tracking, we need to track the longest substring

# right, let's code.. what do we need ..
# left and right pointers, we need to declare left explicitly
# `right` can be the iteration index

# we need a set to track the seen characters
# we need a value to track longest substring 


# turns out i didn't need the `right` pointer..
# it's implicit since i'm iterating through the array from start to end

# the current char always indicates the right pointer..
# i only ever need to remove characters from the start to this point..

# then ball...


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        
        seen = set()
        longest = 0
        
        for right, ch in enumerate(s):
            while ch in seen:
                seen.remove(
                    s[left]
                )
                left += 1
                
            seen.add(ch)
            longest = max(
                longest,
                len(seen)
            )
            
        return longest