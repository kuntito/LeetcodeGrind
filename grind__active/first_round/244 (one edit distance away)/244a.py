# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return self.isOneEditDistance(t, s)
        
        diff = len(t) - len(s)
        if diff > 1: return False
        
        
        for i in range(len(s)):
            chOne, chTwo = s[i], t[i]
            if chOne != chTwo:
                if diff == 0:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1:]
        
        
        return len(s) + 1 == len(t)
    
arr = [
    ["a", "ba"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.isOneEditDistance(foo, bar)