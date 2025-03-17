# https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/description/

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pass
        # find the longest common prefix of `t` in `s`
        
        # use a pointer, `pos`
        # to track the current char in `t` that we're looking for in `s`
        # every time you find a valid char, increment `pos`
        
        # after iterating through `s`
        # `pos` would represent the count of the longest common prefix in `s`
        
        # return len(t) - pos
        
        pos = 0
        
        
        for ch in s:
            if ch == t[pos]:
                pos += 1
            
            if pos == len(t):
                break
         
        
        return len(t) - pos
    
arr = [
    ["coaching", "coding"],
    ["abcde", "a"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.appendCharacters(foo, bar)
print(res)