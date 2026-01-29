# https://leetcode.com/problems/longest-repeating-character-replacement/

# i'm given two things, a string, `s` and an integer `k`

# `s` contains only uppercase english characters.

# i'm allowed to change any character in `s` to any uppercase character i want.
# but i can only do this `k` times.

# why's this important? i'm asked to return the longest substring of `s`
# containing the same letter.

# right.. so the idea is to manipulate `s`, so i get the longest substring
# with the same characters

# and how would this work?
# well, starting from the basics, we know the longest substring will start somewhere and end somewhere..
# okay, so why not start from the first character..
# move forward until you exhaust `k` or exhaust any more the starting character

# once, that ends, record the furthest you got..
# and move on to the next character..

# while it's likely inefficient, it would work for most cases..
# but what if the longest substring requires you to add characters before..

# consider:
# s = ABB, k = 1

# when i start at A, the furthest i'd get is AA and i'd have used up `k`
# when i start at B, the furthest i'd get is BB and i'd still have `k=1`
# meanwhile, if i'd iterated backwards..

# i'd have BBB, okay so what? iterate forward and backwards..
# narrowing this down.. there's three scenarios for every character..
# either the longest requires you to move forward alone..
# or requires you to move backwards alone..
# or requires you to move in both directions..

# those are your three options.. intuition says, i'm treading the wrong path..

# damn.. this the kind of questions that throw you off your game.
# i'd have to read the solution, i can attempt but i not convinced i'd end up anywhere positive.

# i disagree, i'll try first, fail, then look at the answer.

# back to the drawing board.
# the longest substring has to start somewhere so bruteforce means
# i'd try every position..

# but what am i looking for at every position?
# the substring could start at any character.

# then i'd check every character.
# as an aside.. subtle optimization is to check for all the characters that exist in the string
# so this way, i wouldn't have to check all 26 characters at every position.

# okay.. so what are you doing at every position in `s`
# we explore every character we know is in `s`
# we assume, they're the longest string and they start at that position.

# say the character is `main`
# we move forward as long as:

# there's somewhere to move to, and, the next position is the same char as `main` or
# `k > 0`, while this is the case, we track the length our movement.

# once we run out of places to move to, we note how far we got and repeat..
# it's undeniably efficient but it's a start.

# ok.. it works but TLE.. so now, we optimize..


# what's the repeated work..
# i peeped the solution and now have an intuition, on to `b.py`

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        uniqueChars = set(s)
        
        # longest is at least `k`
        self.longest = k
        self.k = k
                
        dim = len(s)
        for idx in range(dim):
            self.exploreEveryChar(idx, s, uniqueChars)
            
        return self.longest
    
    def exploreEveryChar(self, idx, chars, uniqueChars):
        for char in uniqueChars:
            self.longest = max(
                self.longest,
                self.getFurthest(char, idx, chars)
            )
            
            
    def getFurthest(self, mainChar, startIdx, chars):
        dim = len(chars)
        
        replacements = self.k
        furthest = 0
        
        for idx in range(startIdx, dim):
            curChar = chars[idx]
            
            if curChar != mainChar:
                if replacements == 0: 
                    return furthest
                replacements -= 1
            
            furthest = (idx - startIdx) + 1
                        
        return furthest