# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/

# TODO https://neetcode.io/solutions/greatest-common-divisor-of-strings
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        pass
        # largest common repeating unit in both strings
        
        # for each substring in the shorter substring
        # explore if the substring can be found in the longest one
        # if yes, update res as the longest divisor
        
        short, longg = (str1, str2) if len(str1) < len(str2) else (str2, str1)
        
        res = ""
        dim = len(short)
        for i in range(dim):
            sub_len = i + 1
            
            # if the sub string can't fit in either string continue
            if len(longg) % sub_len or len(short) % sub_len:
                continue
            
            sub = short[:sub_len]
            if self.does_it_divide(sub, longg) and self.does_it_divide(sub, short):
                res = sub
            
        return res
    
    def does_it_divide(self, sub, chars):
        left, right = 0, len(sub)
        dim = len(sub)
        
        while right <= len(chars):
            if sub != chars[left: right]:
                return False
            left = right
            right += dim    
                
        return True
    
    
arr = [
    ["ABABAB", "ABAB"],
    ["ABCABC", "ABC"],
    ["AAAAAAAAA", "AAACCC"],
    ["TAUXXTAUXXTAUXXTAUXXTAUXX", "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"],
]
foo, bar = arr[-1]
sol = Solution()
res = sol.gcdOfStrings(foo, bar)
print(res)