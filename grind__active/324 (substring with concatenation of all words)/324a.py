# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/

from typing import Counter, List

# we want to implement a function `findSubstring`
# with two arguments, a list of strings, `words`
# a string `s`

# `words` is a list of strings
# where all the strings are of the same length

# and the second argument, `s`
# may contain a "concatenatedstring"
# we want to find and return the starting indices of all the concatenated strings in `s`

# but what is a concatenated string?
# a concatenated string is the result of combining all the strings in `words`
# i.e. words = ["apple", "juice"]
# a concatenated strings would be "applejuice"

# also, the order doesn't matter. "juiceapple" is also a concatenated string

# an test case could be:
# s = "applejuicemangojuiceapple"
# words = ["apple", "juice"]

# our job is to find the starting indices of any concatenated strings in `s`
# there's two of them, one at index = 0 and another at index..
# lemme count it

# it's at index 15
# so our result would be [0, 15]

# now, we've understood the problem
# how do we solve it

# well, we need to explore s to find a concatenated string
# perhaps, it might be simpler, if we replaced each string in words with a different character in `s`

# like replaceing "apple" with "j"
# and replacing "juice" with "k"

# so the string becomes "jkmangokj"
# it makes things easier

# but the problem is addressing overlaps
# consider:
# `words = ["ee", "ee"] and s = "eeeee"`
# which one are you replacing?

# it's looking like i'd need recursion.
# possibly, but that's not the main thing.

# say i'm tracking substrings of `s`
# how do i know i've found a word.

# with every char i add to the substring, i check if it's a word
# if it is, i remove the word and restart the the substring streak
# i can store the words using a hashmap, i'd keep going until
# i exhaust the words in the hashmap.
# at this point, i'd know i have a concatenation string.

# and if i couldn't exhaust the hashmap but ran out of `s`
# i'd know i couldn't find one
# i'd backtrack.

# however, say i find a concatenation string
# how do i know where it started?
# all elements of `words` are equal length.
# if you find a concatenation string, you can calculate where the start would be

# also, i might not need a substring window
# since all elements of `words` are equal length, `x`

# my first substring is always a slice, s[:x]
# not really, the concatenated substring can start from any position
# so picking the first `x` chars might result in missed strings

# might just have to iterate through all the values
# the upside is for every idx, you can slice and check if you have a word.
# if so, then explore that path...

# TODO, you're on to something but you'd have to rewrite it
# every path should only continue if the words are contiguous
# say i explore 0 and three calls down the line, i find an answer
# that third call shouldn't continue it's loop since that would create a gap in the words

# you might not even need recursion
# a while loop might suffice
# for each word you find, check if the next `n` words
# after it are the remaining words required
# where `n == len(words) - 1`
from collections import defaultdict
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        self.res = []
        
        if words:
            self.chars = s
            self.singleWordLen = len(words[0])            
            self.totalLen = self.singleWordLen * len(words)
            
            self.wordsMap = defaultdict(int)
            for w in words:
                self.wordsMap[w] += 1
            
            self.explore(0)
        
        return self.res
    
    def explore(self, currIdx):
        
        if not self.wordsMap:
            concatStart = currIdx - self.totalLen
            self.res.append(concatStart)
            return True
            
        # i want to iterate from `currIdx` to the last index in `chars`
        # i'd take a slice of each word
        # if it exists in the map, i'd decrement it's frequency
        # start another recursive function with the endIdx of said word
        
        dim = len(self.chars)
        for idx in range(currIdx, dim):
            wordEndIdx = idx + self.singleWordLen
            if wordEndIdx > dim:
                break
            
            word = self.chars[idx: wordEndIdx]
            if word in self.wordsMap:
                self.wordsMap[word] -= 1
                if self.wordsMap[word] == 0:
                    del self.wordsMap[word]
                
                res = self.explore(wordEndIdx)
                self.wordsMap[word] += 1
                if res:
                    break
                
arr = [
    ["barfoothefoobarman", ["foo","bar"]],
    ["wordgoodgoodgoodbestword", ["word","good","best","word"]],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.findSubstring(foo, bar)
print(res)