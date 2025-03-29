# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
        # piggybacking of the explanation in `03a.py`
        
        # but this time, we'd track the longest palindrome as a string
        longest = ""
        
        dim = len(s)
        for idx in range(dim):
            oddPal = self.explore(idx, idx, s)
            longest = self.returnLongest(longest, oddPal)
            
            evenPal = self.explore(idx, idx + 1, s)
            longest = self.returnLongest(longest, evenPal)
            
        return longest
            
            
    def returnLongest(self, uno, dos):
        return uno if len(uno) > len(dos) else dos
    
    
    def explore(self, left, right, chars):
        longest = ""
        dim = len(chars)
        while left >= 0 and right < dim and chars[left] == chars[right]:
            longest = chars[left: right + 1]
            left -= 1
            right += 1
            
        return longest
    
arr = [
    "babad",
    "cbbd",
]
foo = arr[-1]
sol = Solution()
res = sol.longestPalindrome(foo)
print(res)