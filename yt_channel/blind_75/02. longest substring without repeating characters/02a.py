# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        # we need a way to track duplicates, it's giving set
        # we iterate through each character in `s`
        # we'd only add unique characters to the set
        # if the character is a duplicate, track the length so far
        
        # empty the set and add that character # FIXME
        # this way, we'd be tracking a new sub string without repeating characters
        
        # to start, we'd need a variable that tracks the longest so far
        # let's call it longestSoFar
        longestSoFar = 0
        
        # we need our set for unique characters
        # let's call it uniqueChars
        uniqueChars = set()
        
        # now, we ball through the string, `s`
        for ch in s:
            if ch not in uniqueChars:
                uniqueChars.add(ch)
                # we check for updates whenever we add a new char
                if len(uniqueChars) > longestSoFar:
                    longestSoFar = len(uniqueChars)
            else:
                # if the char is a duplicate, clear the set
                uniqueChars.clear()
                uniqueChars.add(ch)
                
        return longestSoFar
    
arr = [
    "pwwkew",
    "bbbbb",
    "abcabcbb",
]
foo = arr[-1]
sol = Solution()
res = sol.lengthOfLongestSubstring(foo)
print(res)
        