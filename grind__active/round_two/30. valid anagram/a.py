# https://leetcode.com/problems/valid-anagram/description/

# i'm given two strings and want to find out if they're anagrams..
# what are anagrams, two strings with the same characters

# i.e. 
# "jay" and "jay"
# "caat" and "atac"

# okay, how would this work? sort the characters..
# nah, i'd use a dic to track the characters in the first string
# then iterate through the second string..

# be more explicit.. let's call the strings, `firstOne` and `secondOne`
# i'd track all the characters in `firstOne` using a dictionary..

# then iterate through `secondOne` to see if every of it's characters exist
# in the dictionary..

# why a dictionary, without it, to check if `secondOne`'s character exists in `firstOne`
# i'd have to search `firstOne` every time, a dictionary allows know instantly.

# okay, so how are you using this dictionary, for each character in `secondOne`
# the question is:
#  * does this character exist in the dictionary..
#  if yes, deduct it's count from dictionary
#  if no, return False..

# also, with every deduction, if we hit zero, return False..
# edge case, if len(firstOne) is greater and all the characters of `secondOne` are in `firstOne`
# the iteration would complete without returning False..

# what then..
# i'd say the return should be a check for an empty dictionary..
# alternatively, i could just check from  the jump
# if both strings are equal lengthed, since this is a requirement for anagrams

# alreet, seems like you've got this..
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        trackDict = {}
        for ch in s:
            trackDict[ch] = trackDict.get(ch, 0) + 1
            
        for ch in t:
            if ch not in trackDict:
                return False
            
            trackDict[ch] -= 1
            if trackDict[ch] == 0:
                del trackDict[ch]
                
        return True