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
# i'd sort it, check for it's key in the dictionary
# add the key if absent..

# and simply append each word to it's array..
# dunno if there's a simpler or more optimal solution

# `error`, when i sorted each word to get a key
# i didn't know the `sorted` method returns a list..
# lists can't be dictionary keys..
# so i converted the sorted list into a string.

# let me see if there's a more optimal one.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = {}
        
        for wd in strs:
            wordKey = ''.join(sorted(wd))
            if wordKey not in anagramDict:
                anagramDict[wordKey] = []
            
            anagramDict[wordKey].append(wd)
            
        return list(anagramDict.values())