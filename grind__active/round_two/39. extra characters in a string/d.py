# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

# what are we doing here?
# i've got two things, a string `s` and an array, `dictionary`

# `dictionary` is an array of strings.

# what i want to do is reduce the characters in `s`
# and how do i do this?

# `dictionary` contains words, some of these words exist in `s`.
# i want to pick the right words from `dictionary` such that

# when i remove those words from `s`, `s` becomes as small as possible.

# for example..
# s = "jayxnas"
# dictionary = ["ayxn", "nas", "jay"]

# now, which dictionary words do i remove from `s`?

# say, i remove "ayxn" from `s`
# i'm left with "jas", three characters, not too bad.

# say, i remove "jay" from `s`
# i'm left with "xnas", four characters.

# but wait, i can still remove one more word..
# "nas", if i remove "nas" from "xnas"

# i'm left with "x", one character, that's great.

# this illustration has shown two things:
#   the first removal isn't necessarily the best
#   we might have to remove multiple characters

# so what can i do with this?
# it's definitely a recursive solution..
# i'd find a word in `s`
# remove it, `s` becomes shortened..

# then i do it again..
# can i remove the same word multiple times?

# i have to assume i can
# if s = "aa" and dictionary = ["a"]
# i can remove "a" twice.

# okay, but how would the code go..
# iterate through `s`

# for every position, check if a word can be removed.
# if it can, remove it, start a recursive call with the shortened `s`

# one question, are we breaking up `s`
# or searching the rest of `s`

# what do you mean?
# consider:
# s = "nnasas" 
# dictionary = ["nas"]

# if i hit position `1`, i can remove "nas"
# then i'd be left with "n___as"
# do i stich the rest?

# nah, the question says i have to break `s` into one or more
# non-overlapping substrings, which means each substring should be it's own word.

# in this case, the substrings left would be "n" and "as"
# because, we iterated `s` from the beginning of the string
# if "n" was any good, we'd have found out.

# so we want to check the rest of the string
# for any words.. i.e. "as"

# this is looking much simpler..
# what if there are multiple words starting at a position..

# we'd have to explore all of them..
# so one check for all the words at this position..
# for each word, start a recursive call with a new slice..

# and how do you track the words removed.
# each recursive call should have a property, `removedCount`
# the number of characters removed from the previous call

# and how would this work? what would be the base case?
# say "nnasas" and `dictionary = ["nas"]`

# you remove "nas"..
# start a recursive call with `removedCount = 3`
# and s = "as"
# you run through both positions, "a" and "s".. no matches..
# what do you do with recursive count?

# yeah, i don't know about this one..
# perhaps, each function should just return it's `removedCount`
# this way the parent collates with the child call.

# in our case, for "as", we'd return `0`
# it gets back to parent..

# parent has it's own `removedCount`
# which for this exploration would be
# len("nas") + child exploration..

# each call should have a variable that tracks bestRemovedCount..
# with this, i can get the removed count for each position.

# and simply return the result from the first call.
# is there a need for memoization?
# yes, every position does the same work so..

# error, i currently return the bestRemoved i.e. the most characters
# i could remove from `s`
# i should be returning the shortest length `s` can be
# which would be `len(s) - self.explo...`

# i should probably memoize.. since every version of `s` returns the same result?
# but when would you see the same version of `s` twice?

# s = "metrobooming"
# dictionary = ["me", "tro", "metro"]
# in this case, we'd explore "booming" twice.

# once when we explore "me" then "tro"
# another when we explore "metro"

# memo, it is.

# works like a charm

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordCache = {}
        for wd in dictionary:
            firstCh = wd[0]
            if firstCh not in wordCache:
                wordCache[firstCh] = []
            wordCache[firstCh].append(wd)
        
        memo = {}
        return len(s) - self.explore(s, wordCache, memo)
    
    def explore(self, s, wordCache, memo):
        if s in memo:
            return memo[s]
        
        bestRemoved = 0
        for idx, ch in enumerate(s):
            # now i want to know if any word starts at this index..
            # how's that possible?
            
            # for one, i could create a cache
            # for characters and words
            
            # what? for every word in `dictionary`
            # create a mapping, of first character to a list.
            
            # say dictionary contained = ["apple", "act", "bat"]
            # our mapping would be 
            # `a => ["apple", "act"]`
            # `b => ["bat"]`
            
            # this way for each `ch` in the iteration we know
            # if a word thats with this, with the trick of slicing
            # we can tell if the word exists in this position onwards
            
            # might be beneficial to re-use this cache
            # i'd declare it in the parent variable and pass it to
            # every recursive call.
            
            # i renamed cache to `wordCache`, more descriptive.
            
            if ch not in wordCache: continue
            
            # for every word, i want to compare the relevant slice 
            # of `s` with the word, if it's a match, another recursive call
            for wd in wordCache[ch]:
                endRange = idx + len(wd)
                relevantSlice = s[idx:endRange]
                if wd == relevantSlice:
                    exploreRes = self.explore(
                        s[endRange:],
                        wordCache,
                        memo
                    )
                    bestRemoved = max(
                        bestRemoved,
                        len(wd) + exploreRes
                    )
                    
        memo[s] = bestRemoved
        return memo[s]
            
arr = [
    [
        "leetscode",
        ["leet","code","leetcode"]
    ],
    [
        "dwmodizxvvbosxxw",
        ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"],
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minExtraChar(foo, bar)
print(res)