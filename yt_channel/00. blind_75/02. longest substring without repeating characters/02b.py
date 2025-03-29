# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# TODO is there a simpler solution?
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
        # we need a way to track duplicates, it's giving set
        # we iterate through each character in `s`
        # we'd only add unique characters to the set
        # we'd use a variable `longest` to track the result
        # whenever, we add a new character to the set
        # we check if `longest` needs to be updated
        
        longest = 0
        
        # the kicker is when we encounter a unique character
        # consider `abcc` and `acbc`
        
        # in both strings, the duplicate is the last character
        # in `abcc`, the duplicate is `c` and so we'd start a new substring from that `c`
        
        # however, in `acbc`, we cannot start a new substring from that `c`
        # since we'd be leaving out it's previous unique character `b`
        
        # in essence, once we find a duplicate character
        # starting from the start of the substring, we remove characters until we find the duplicate
        
        # in the case of `abcc`, the duplicate is in position `2`
        # so we'd have to remove every char with idx <= 2
        
        # in thr case of `acbc`, the duplicate is in position `1`
        # so we'd have to remove every char with idx <= 1
        
        # it's giving two pointers
        uno, dos = 0, 0
        
        # we'd ball through the string with `dos`
        # `uno` would represent the start of the substring
        
        # we'd use a set,`seen` to represent the unique characters
        seen = set()
        
        while dos < len(s):
            ch = s[dos]
            if ch in seen:
                while ch in seen:
                    substringHead = s[uno]
                    uno += 1
                    seen.remove(substringHead)
            
            seen.add(ch)
            if len(seen) > longest:
                longest = len(seen)
            
            dos += 1
            
        return longest
        
        
    
arr = [
    "pwwkew",
    "bbbbb",
    "abcabcbb",
    "dvdf",
]
foo = arr[-1]
sol = Solution()
res = sol.lengthOfLongestSubstring(foo)
print(res)
        