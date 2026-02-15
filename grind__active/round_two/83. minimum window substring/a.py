# https://leetcode.com/problems/minimum-window-substring/

# what are we doing here?

# i'm given two strings, `s` and `t`.
# i want to do something with them and return a single string.

# but what is this return string?
# the string i'm returning is the shortest substring of `s`
# that contains all the characters in `t`

# consider:
# s = "tidalat"
# t = "at"

# there's several substrings in `s` that contain all the characters of `t`
# for example:
#   "tida"
#   "tidalat"
#   "alat"
#   "at"

# but the shortest one is "at"
# this is what we want to find.

# the way i see it, i'd have a window moving through `s`
# a sliding window as it's commonly called.

# and this window knows if it contains all the characters in `t`
# initially, the window expands until it contains all the characters in `t`
# or runs out of characters, in which case, we return an empty string.
# no answer was found.

# but in the case where the window reaches a point where it contains
# all the characters in `t`
# what do we do?

# let's re-explore our example:
# s = "tidalat"
# t = "at"

# our first bingo would be "tida"
# at which point, what do we want to do..
# well, we'd store the length of our window at this point

# then we want to shrink the window.
# but by how much?

# starting from the left, you want to remove the first character from `t`
# that you find.

# in our case, we found the window "tida"
# so we shrink leftwards, we remove "t"

# now we have "ida"
# it's apparent, i can still get rid of the "i" and the "d"
# and be left with "a"

# so i can shrink from "tida" to "a"
# removing "tid"

# but what's the point of the shrinking here.
# well, we've found a window.

# we don't know if there's a shorter window.
# perhaps, we can optimize here, if at any point
# we have a valid window of size len(t), return that window.

# but that's an aside.
# most times, we'd have a window longer than len(t)
# so why are we removing the first character from `t`
# we find and every other character that's not in `t`

# i think the idea is you have "tida"
# your target characters are "a" and "t"
# when you remove the first one you find..
# you've made the window invalid...

# you shrunk it, this allows us to start from the next available character
# and expand the window from there.

# in our case, the first character we find is the "t"
# so we remove it, leaving us with "ida"
# now, at this point, "id" is no longer relevant to the window.

# the only reason, we permitted it was because at the time, we were looking
# to complete the window

# keep in mind, we started with "t" -> "ti" -> "tid"
# we kept going, because the window was invalid.
# the moment we had a valid window, "tida"
# we stored the length of that window

# and now we can shrink the window..
# remove every letter leftword up until the second available letter in `t`
# then continue the same iteration.

# what if `t` was only one character
# in which case, our earlier optimization would handle that.

# what if `s` started with a bunch of dummy characters
# say we had "mentidalat" instead and `t` was still "at"

# the first three characters would be irrelevant.
# well, in that case, our iteration should only start from the first
# relevant character we find.

# okay.. this seems like it should work.
# how would the code go?

# well, there's two problems..
# one, knowing when our window is valid
# two, knowing when a character is in `t`

# the second problem is really a hashmap situation.
# the first however..

# it could also be a hashmap, `windowHashmap`
# every time we add a character to `windowHashmap`
# we check if the char count is equal to the the char count in t's hashmap
# if it is, we would increment a variable, `matches += 1`

# the momemnt, `matches` hits `len(t)`, we know our window is valid.

# sounds good, and removing the leftward characters..
# you want to move the left portion of the window forward
# as long as the current character is not in `t`
# the current character is the first character in `t`
# we've seen..

# that way the window is shrunk appropriately.
# sound like a plan? seems so.

# leftPointer
# windowHashmap
# matches
# tHashMap
# shortestWindowLen, initialize this to None, if None after iteration, return ""

# error, when checking if the new window character increases matches
# i should first check if that character is even in `t`
# i ran into a Key error, where i added a character to the window
# and checked if it's char count in window equals to the char count in `t`
# but the char might never have been in `t` from the jump..

# fixed with .. `if ch in tsHashMap and windowHashMap[ch] == tsHashMap[ch]:`

# another error, when i have a valid window and want to shrink
# there's a point where i update matches
# if the character at the left pointer is in tsHashMap
# and matches is still the length of t

# i was comparing the char counts of `ch`, the character from the OG iteration
# i should've been comparing with `currentCh`.. the character at the left pointer

# error, i should've read the question better, perhaps, inputs and outputs, they wanted
# the shortest substring, not it's length..

# TODO, i'd have to rewrite this..
# TODO also, don't forget to test if del char counts with `0` from `windowHashMap` is necessary.

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        leftPointer = 0
        windowHashMap = {}
        
        tsHashMap = self.getHashMap(t)
        
        matches = 0
        shortestWindowLen = None
                
        for idx, ch in enumerate(s):
            windowHashMap[ch] = windowHashMap.get(ch, 0) + 1
            
            if ch in tsHashMap and windowHashMap[ch] == tsHashMap[ch]:
                matches += 1
                
            if matches == len(t):
                # this is when we update `shortestWindowLen`
                windowLen = (idx - leftPointer) + 1
                
                # short circuit..
                if windowLen == len(t):
                    return windowLen
                
                if shortestWindowLen is None:
                    shortestWindowLen = windowLen
                else:
                    shortestWindowLen = min(
                        shortestWindowLen,
                        windowLen
                    )
                    
                
                # then shrink the window
                # what's the condition, while character at the left pointer is not in `t`
                # or matches == len(t)
                # would this work.. what conditions would cause this to break
                # if you move left pointer to a point where 
                # the current character is in `t` but matches != len(t)
                # which would only happen if we've removed the matching character from `t`
                # seems solid, let's do it
                
                # there's a subtle error, i handled by returning
                # windowLen, if it's equal to `len(t)`
                
                # if you had only one character in `t`
                # at the point when you remove `t`
                # the loop runs because `matches == len(t)`
                # at which point, you update matches and move the left pointer forward
                
                # when you run the loop again,
                # you check if `s[leftPointer]` is not in `t`
                # at this point `leftPointer` would have exceeded the windows
                # and if indeed, that character is not in `tsHashMap`
                # the loop continues.. when it should have stopped.
                
                # this would only happen if `t` was a single character though
                # if it were double.. we'd shrink until the character at `leftPointer`
                # is in `tsHashMap` and matches has been reduced.
                
                # returning window len if equal to len of t
                # handles this gracefully.
                
                # another alternative would be to only run the loop 
                # while leftPointer <= idx
                                
                while s[leftPointer] not in tsHashMap or matches == len(t):
                    currentCh = s[leftPointer]
                    windowHashMap[currentCh] -= 1

                    # then i have to update matches too..
                    a = currentCh in tsHashMap
                    b =  windowHashMap[ch] != tsHashMap[ch]
                    if currentCh in tsHashMap and (windowHashMap[currentCh] != tsHashMap[currentCh]):
                        matches -= 1
                    
                    # TODO don't think i need to delete anything, it should work without
                    if windowHashMap[currentCh] == 0:
                        del windowHashMap[currentCh]
                        
                    leftPointer += 1
                    
        return shortestWindowLen
                        
            
            
    def getHashMap(self, chars):
        hashmap = {}
        
        for ch in chars:
            hashmap[ch] = hashmap.get(ch, 0) + 1
            
        return hashmap
    
arr = [
    [        
        "ADOBECODEBANC",
        "ABC",
    ]
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minWindow(foo, bar)
print(res)