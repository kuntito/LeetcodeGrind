# https://leetcode.com/problems/extra-characters-in-a-string/

from typing import List

# what am i doing?
# i have two things, a string, `s`
# and an array of strings, `dictionary`

# i want to remove the words in `dictionary` from `s`
# in such a way that leaves `s` as small as possible.

# consider
# s = "jayxnas"
# dictionary = ["ayxn", jay", "nas"]

# all words in `dictionary` exist in `s`
# however, which one or ones do i remove
# so it makes `s` as small as possible..

# if i remove "ayxn" from "jayxnas"
# i'd be left with "jas"

# but, if i remove "jay" and "nas" from "jayxnas"
# i'd be left with "x"

# so that's the best approach.

# how would you do this in code?
# well, i don't know what words from `dictionary`
# exist in `s`

# i'd iterate through `s`
# at each character, i want to check if a word exists
# if it does, i'd jump forward.. and do what i did at the start

# iterate through the rest of `s`
# at each character, check if a word exists
# if it does, i'd jump forward..

# recursion.

# one optimization is i can run through `dictionary` and `s`
# and create a cache for all the words that exist at each index.

# now, i have the word cache.. what am i doing..
# recursion.

# on each call, i want to iterate from start index to the end.
# what am i doing?

# grab all the words that can form from that index.
# for each word, start a recursive call
# with startIdx = startIdx + len(word)
# track the length of the words as you go along
# memoize..

# how would you track the word length as you go along?
# for each recursive call, pass currLen..
# you update this with every call.

# and how do you get the final result?
# global variable.

# error, i returned the total length of the words removed.
# instead of the length of `s` after all those words are removed.

# TODO, algo fails
# see
# s = "dwmodizxvvbosxxw"
# dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
# result should be `7`

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        wordCache = self.getWordCache(s, dictionary)

        memo = {}
        x = len(s) - self.explore(0, s, wordCache, memo)
        print(memo)
        return x
        
    # how do you memoize if you pass curLen
    # every recursive call should return it's own result
    def explore(self, startIdx, s, wordCache, memo):
        if startIdx in memo:
            return memo[startIdx]
        
        dim = len(s)
        bestHere = 0
        for idx in range(startIdx, dim):
            for w in wordCache[idx]:
                exploreRes = self.explore(
                    startIdx + len(w),
                    s,
                    wordCache,
                    memo,
                )
                bestHere = max(
                    bestHere,
                    len(w) + exploreRes
                )
                
        memo[startIdx] = bestHere
        return memo[startIdx]
        
        

        
        
    def getWordCache(self, s, wordsArr):
        # how would this go..
        # at each index, what do i want to do..
        
        # i don't see an optimal way of doing this..
        # if the first character is `a`
        
        # i want to pick all the `a` words from `wordsArr`
        # whichever ones fit the condition..
        
        # i'd append to the wordCache
        # {a's index: [..relevant words]}
        
        # so i need to map each letter of the alphabet to their words in `wordsArr`
        pass
    
        charToWordsMap = self.getCharMapping(wordsArr)
        
        # now i have the map, what next..
        # iterate through `s`..
        
        # for each character, 
        # does it have any words in `wordsArr`
        # if yes, check if those words exist in `s`, 
        # starting from that character onwards, if yes, append to cache
        cache = {}
        for idx, ch in enumerate(s):
            cache[idx] = []
            
            if ch in charToWordsMap:
                matches = self.getMatches(idx, s, charToWordsMap[ch])
                cache[idx].extend(matches)
                
        return cache
                
    def getMatches(self, startIdx, s, candidateWords):
        matches = []
        for w in candidateWords:
            endIdx = startIdx + len(w)
            slice = s[startIdx: endIdx]
            
            if slice == w:
                matches.append(w)
                
        return matches
            
        
    
    def getCharMapping(self, wordsArr):
        charToWordsMap = {}
        
        for word in wordsArr:
            firstCh = word[0]
            
            if firstCh not in charToWordsMap:
                charToWordsMap[firstCh] = []
                
            charToWordsMap[firstCh].append(word)
            
        return charToWordsMap
    
arr = [
    [
        "leetscode",
        ["leet","code","leetcode"]
    ],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.minExtraChar(foo, bar)


# error, when writing the variables, i passed `s` as a list
# ["content"] instead of "content"