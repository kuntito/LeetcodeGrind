# https://leetcode.com/problems/longest-common-prefix/description/

from typing import List

# i'm given a list of strings, `strs`.
# i want to find the longest common prefix among them.

# how would this go?
# for one, i could sort the strings by length..
# the longest common prefix is at most the shortest string..

# yeah, but why're you doing this?
# what problem are you trying to solve?

# to know the prefix in each string, you'd have to see each string.
# this is where the shortest word comes in..

# you can initialize the longest common prefix as the shortest word..
# then as you iterate through words..

# you compare prefixes and update the longest common prefix as needed.

# say your shortest word is `mist`
# and your next word is `misadventure`

# the only matches are ... `mis`
# now that i think about it..

# you can slice each word.. make each word only as long as the current
# longest common prefix..

# this sounds like implementation detail.
# your first approach is spot on.

# update longest common prefix as you go..
# if no prefixes, return empty string

# else return longest common prefix
# so how do you obtain the shortest word..

# there a function or we doing it the manual way.

# error, i iterated for each word using `longestCommonPrefix`
# i did `for word in longestCommonPrefix` instead of `for word in strs`

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortestString = min(strs, key=len)
        
        longestCommonPrefix = shortestString
        
        for word in strs:
            longestCommonPrefix = self.updateLCP(word, longestCommonPrefix)
            
            if longestCommonPrefix == '':
                return longestCommonPrefix
            
        return longestCommonPrefix
    
    def updateLCP(self, wordOne, wordTwo):
        lcp = []
        
        for chOne, chTwo in zip(wordOne, wordTwo):
            if chOne != chTwo:
                break
            
            lcp.append(chOne)
        
        return "".join(lcp)