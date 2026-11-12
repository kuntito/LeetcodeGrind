class Solution:
    def minCut(self, s: str) -> int:
        # at each point,
        # you do two things.
        
        # you check if what you have is a palindrome
        # if it is, explore the rest of the string for palindromes.
        
        # then you add the next character to what you have.
        
        # it's recursive, and you're carrying a substring.
        # if the substring you have is a palindrome
        # then you explore the rest of the substring
        # till you end all palindromes.
        
        # if the substring isn't a palindrome, you stop exploring.
        # so, is it not just one thing you're doing?
        
        # well, consider "aaa"
        
        # you take the first character.
        # it's a palindrome, so you can explore "aa" on that thread.
        
        # back to the initial call, you took "a" then had to explore "aa"
        # but you'd also continue the substring.
        
        # i see the pattern
        # at each point, you want to keep adding characters
        # to your substring.
        
        # on every character you add, check if the rest of the string is a palindrome.
        
        # track the number of splits.
        
        idx = 0
        chars = s
        substr = []
        
        self.leastSplits = float("inf")
        
        self.checkPalindrome(idx, chars, substr, 0)
        
        return self.leastSplits
    
    def checkPalindrome(self, start_idx, chars, substr, curSplit):
        dim = len(chars)
        if start_idx == dim:
            if curSplit < self.leastSplits:
                self.leastSplits = curSplit
                
            return
        
        
        for idx in range(start_idx, dim):
            ch = chars[idx]
            substr.append(ch)
            
            if self.isPalindrome(substr):
                last_idx = dim - 1
                isSplit = idx < last_idx
                
                self.checkPalindrome(
                    idx + 1,
                    chars,
                    [],
                    curSplit + (1 if isSplit else 0)
                )
        
        
    def isPalindrome(self, chars):
        left, right = 0, len(chars) - 1
        
        
        while left <= right:
            a, b = chars[left], chars[right]
            
            if a != b:
                return False
            
            left += 1
            right -= 1
            
        return True
            
            
arr = [
    "a",
    "aab",
    "ab",
]
foo = arr[-1]
sol = Solution()
res = sol.minCut(foo)
print(res)