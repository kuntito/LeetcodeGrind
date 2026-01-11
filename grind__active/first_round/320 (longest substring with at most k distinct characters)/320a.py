# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/

# what are we doing?
# what am i doing?
# i want to implement the function `lengthOfLongestSubstringKDistinct`
# it takes two arguments, a string `s` and an integer `k`

# it returns the length of the longest substring of `s`
# with at most `k` distinct characters

# in otherwords, we want to iterate `s` exploring all substrings
# with unique characters and return the length of the longest one

# i suggest we apply a sliding window
# right from the first character in `s`
# we track it in a set, `seen`

# for every character we find, we add to `seen`
# unless the character is already in seen
# in which case, we move the left pointer

# yes, we'd need a left pointer
# initialized at zero (0)
# while the duplicate exists, we move the left pointer forward

# i swear, i've seen this question before

# not exactly, we're looking for the longest substring with at most k distinct
# the substring can be as long as anything as long as we have at most `k` distinct characters

# i misread the question, practically every time i get full of myself
# i make a silly mistake
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        pass
    
        longest = 0
        leftPointer = 0
        seen = set()
        
        for ch in s:
            while ch in s:
                leftCh = s[leftPointer]
                seen.remove(leftCh)
                
                leftPointer += 1
                
            seen.add(ch)
            
            windowLen = len(seen)
            if windowLen > longest:
                longest = windowLen
                
        return longest
    
arr = [
    
]