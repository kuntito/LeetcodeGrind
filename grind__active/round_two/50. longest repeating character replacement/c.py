# https://leetcode.com/problems/longest-repeating-character-replacement/

# what's going on?
# i'm given two things, a string, `s` and an integer, `k`

# `s` only contains uppercase alphabet characters, A..Z
# `k` tells me the number of times i can change any characters in `s`
# i.e. if s  = "AA" and k=1
# i can change any character in `s`, i.e. turn s into `AB`

# but why would i want to do that?
# i want to find the longest substring of `s`
# that has the same characters..

# being able to change characters means i can artificially
# increase the longest substring in `s`

# consider:
# s = AABC
# k = 2

# i can change `B` and `C` into `A`
# and have s = AAAA

# right, how would this work in code.

# a sliding window..
# a sliding window? yes.

# what we'd do is start the iteration from the start of `s`
# each character goes into the window..

# as we add characters, we track the frequency of the most occuring character
# okay..
# the window should never be bigger than `frequency of most occuring + k`

# i see your point, this way, we know everything in the window can become
# the most occuring character

# and we can track the max window length as our result
# so what happens if you exceed, `frequency of the most occuring character + k`

# then starting from the left side of the window
# we remove characters until the condition is true again..

# okay.. and this could mean the frequency of the most occuring character could change.
# how do you update to the frequency of the new most occuring character.

# we don't.

# why not? once we hit `frequency of the most occuring character + k`
# we found a character that maxed `k`

# since, we want to find the longest substring, no character we've seen
# would have a greater frequency that the earlier most occuring character..

# so we can leave that character as is..
# and just continue the forward iteration..

# we keep tracking new characters and if we find one
# with a higher frequency and the window is intact..

# that becomes our new result.

# so how would the code go?
# a dictionary, `windowDict`
# the left pointer of the window, `leftIndex`
# the most occuring frequency so far, `mostOccur`
# length of the longest substring, `longestSub`

# error, i wrote the condition wrong.
# i wrote (mostOccur + k) > len(windowDict)

# it should be if the length of the window exceeds (mostOccur + k)

# error, can't use the length of the dictionary..
# if the dictionary has 12 A's, it's length remains one..

# i don't need a dictionary to store the window's values, an array would suffice.
# TODO rewrite this!

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        windowDict = {}
        leftPointer = 0
        mostOccur = 0
        longestSub = 0
        
        # what do you want to do here.. 
        # if you add a new value to the window
        # and the condition becomes False, remove characters starting from the left.
        
        # okay, and at what point do you update the new mostOccur
        # you can do it after the removals, it wouldn't matter since, `mostOccur`
        # would be the most occurred at that particular time.
        
        for idx, ch in enumerate(s):
            windowDict[ch] = windowDict.get(ch, 0) + 1

            if windowDict[ch] > mostOccur:
                mostOccur = windowDict[ch]
            
            while len(windowDict) > (mostOccur + k):
                chAtIdx = s[leftPointer]
                windowDict[chAtIdx] -= 1
                
                if windowDict[chAtIdx] == 0:
                    del windowDict[chAtIdx]
                
                leftPointer += 1

                
            longestSub = max(
                longestSub,
                len(windowDict)
            )
            
        return longestSub
    
arr = [
    ["ABAB", 2],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.characterReplacement(foo, bar)
print(res)