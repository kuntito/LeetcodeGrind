class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        max_pal = ""

        for i in range(len(s)):
            for j in range(i, len(s)):
                current_substring = s[i:j+1]
                
                if current_substring == current_substring[::-1] and len(current_substring) > len(max_pal):
                    max_pal = current_substring
        
        return max_pal
    
arr = [
    "a",
]
foo = arr[-1]
sol = Solution()
res = sol.longestPalindrome(foo)
print(res)