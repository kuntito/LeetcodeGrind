# https://leetcode.com/problems/group-anagrams/

from typing import List

# i'm given an array of strings.
# i want to group anagrams together, and return an array of those groupings.

# a 2d array.

# two words are anagrams, if the contain the same characters.. irrespective of order
# 'san' and 'nas' are anagrams..

# we don't know if two words are anagrams until we check every character..
# i imaging this would be a nested iteration kind of thing.

# first thought is convert each anagram to a form that tells you what letters it contains..
# best i can think of is sorting the letters and using it as a key to a dictionary..

# for each word in the string array
# i'd get a key, a unique identifier for each word..

# since, i know each word is only characters a..z
# i can use a list, for each word,
# map each letter's frequency to the list..

# use the list as an id of the the word..
# i can store this in a dict, as a tuple because lists cannot be dictionary keys..

# this way, every word with the same pattern would have an entry in the dictionary.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        
        for wd in strs:
            lst = [0 for i in range(26)]
            for ch in wd:
                idx = ord('a') - ord(ch)
                lst[idx] += 1
                
            dictKey = tuple(lst)
            if dictKey not in anagramDict:
                anagramDict[dictKey] = []
            anagramDict[dictKey].append(wd)
            
        return list(anagramDict.values())