# https://leetcode.com/problems/longest-palindromic-substring/

# FIXME misread the question, they want the substring not it's length
class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
        # the idea here is to explore all possible palindromes
        # it's more optimal to explore a palindrome from it's center
        # start at the center and keep expanding and tracking the length
        # until the substring is no longer a palindrome or you go out of bounds
        
        # lengthwise, a palindrome can be even or odd
        # why's this important, the center for an even-lengthed palindrome is different
        # from an odd-lengthed palindrome
        
        # i.e.
        # the center for "abba" is "bb"
        # the center for "aba" is "b"
        
        # this said, every single character in `s` could potentially be a center
        # for an odd-lengthed palindrome
        
        # every contiguous pair of characters in `s` could potentially be a palindrome's center
        
        # let the code begin
        longest = 0
        for idx, ch in enumerate(s):
            # for each index, we'd explore for single center palindromes
            singLen = self.exploreSingle(idx, s)
            if singLen > longest:
                longest = singLen
            # and explore for double center palindromes
            doubLen = self.exploreDouble(idx, idx + 1, s)
            if doubLen > longest:
                longest = doubLen
                
        return longest
            
    def exploreSingle(self, idx, chars):
        palLength = 0
        
        # to track the palindrome, we'd define two pointers
        left, right = idx, idx
        # in this case both of them are `idx`
        
        # while the values at these indices are equal
        # expand them, move left leftwards
        # move right, rightwards
        
        # also make sure the indices are in bounds
        # before checking if their values are equal
        dim = len(chars)
        while left > 0 and right < dim and chars[left] == chars[right]:
            subStringLength = (right + 1) - left
            if subStringLength > palLength:
                palLength = subStringLength
            
            left -= 1
            right += 1
            
        return palLength
    
    def exploreDouble(self, left, right, chars):
        palLength = 0
        # we can see that the functions for single and double are identical
        # this is an opportunity to apply DRY
        dim = len(chars)
        while left > 0 and right < dim and chars[left] == chars[right]:
            subStringLength = (right + 1) - left
            if subStringLength > palLength:
                palLength = subStringLength
            
            left -= 1
            right += 1
            
        return palLength
    
arr = [
    "cbbd",
    "babad",
]
foo = arr[-1]
sol = Solution()
res = sol.longestPalindrome(foo)
print(res)