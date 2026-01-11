# https://leetcode.com/problems/palindrome-partitioning-ii/description/

# there's some repeated work going on here
# 
# since, i check every palindrome
# some repetitive work could occur

# TODO, explore the results of memoizing `explore` on TLE
class Solution:
    def minCut(self, s: str) -> int:  
        self.minDiv = len(s)
        self.explore(s, 0)
        
        return self.minDiv
        
    def explore(self, chars, palCount):
        if not chars:
            divs = palCount - 1
            if divs < self.minDiv:
                self.minDiv = divs
            return
        
        dim = len(chars)
        for idx in range(dim):
            slice = chars[:idx + 1]
            if self.isPalindrome(slice):
                restOfString = chars[idx + 1:]
                self.explore(
                    restOfString,
                    palCount + 1
                )
            
    def isPalindrome(self, chars):
        left, right = 0, len(chars) - 1
        
        while left <= right and chars[left] == chars[right]:
            left += 1
            right -= 1
            
        return left > right
        
        
arr = [
    "aab",
    # "a",
    # "ab",
]
foo = arr[-1]
sol = Solution()
res = sol.minCut(foo)
print(res)
