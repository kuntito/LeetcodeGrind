# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for w in words:
            if self.is_palindrome(w):
                return w
            
        return ""
    
    def is_palindrome(self, w):
        l, r = 0, len(w)-1

        while l <= r:
            if w[l] != w[r]:
                return False

            l += 1
            r -= 1

        return True